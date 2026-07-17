<template>
  <div class="history-table-container">
    <div class="history-table">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Producto</th>
            <th>Acción</th>
            <th>Fecha</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in history" :key="item.id">
            <td>{{ item.id }}</td>

            <td>
              {{ item.product_name ?? item.product_id }}
            </td>

            <td>{{ item.action }}</td>

            <td>
              {{ formatDate(item.created_at) }}
            </td>
          </tr>

          <tr v-if="history.length === 0">
            <td colspan="4">No hay registros.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
defineProps({
  history: {
    type: Array,
    default: () => [],
  },
});

function formatDate(date) {
  return new Date(date).toLocaleString();
}
</script>
<style scoped src="./history-table.css"></style>
