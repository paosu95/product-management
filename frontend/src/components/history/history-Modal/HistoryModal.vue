<template>
  <Teleport to="body">
    <div
      v-if="modelValue"
      class="modal-overlay"
      @click.self="closeModal"
    >
      <div class="history-modal">

        <div class="modal-header">

          <div>

            <h2>Historial del producto</h2>

            <p>{{ product?.name }}</p>

          </div>

          <button
            class="close-btn"
            @click="closeModal"
          >
            <i class="bi bi-x-lg"></i>
          </button>

        </div>

        <div
          v-if="history.length"
          class="timeline"
        >

          <div
            v-for="item in history"
            :key="item.id"
            class="timeline-item"
          >

            <div
              class="timeline-dot"
              :class="getActionClass(item.action)"
            ></div>

            <div class="timeline-content">

              <h4>{{ item.action }}</h4>

              <small>{{ formatDate(item.created_at) }}</small>

            </div>

          </div>

        </div>

        <div
          v-else
          class="empty-history"
        >

          <i class="bi bi-clock-history"></i>

          <p>No existen registros para este producto.</p>

        </div>

      </div>
    </div>
  </Teleport>
</template>

<script setup>

const props = defineProps({

  modelValue: Boolean,

  product: Object,

  history: {
    type: Array,
    default: () => []
  }

});

const emit = defineEmits([
  "update:modelValue"
]);

function closeModal(){

  emit("update:modelValue", false);

}

function formatDate(date){

  return new Date(date).toLocaleString("es-MX",{

    dateStyle:"medium",

    timeStyle:"short"

  });

}

function getActionClass(action){

  const text = action.toLowerCase();

  if(text.includes("creado")) return "created";

  if(text.includes("actualizado")) return "updated";

  if(text.includes("eliminado")) return "deleted";

  if(text.includes("estado")) return "status";

  return "";

}

</script>

<style scoped src="./history-modal.css"></style>