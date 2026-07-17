<template>
  <div class="history-view">
    <div class="history-header">
      <div class="history-title">
        <h1>Historial de cambios</h1>

        <p>Consulta todas las acciones realizadas sobre los productos.</p>
      </div>
    </div>

    <div class="history-stats">
      <div class="history-card total">
        <span>Total eventos</span>

        <h2>{{ historyStore.history.length }}</h2>
      </div>

      <div class="history-card created">
        <span>Creados</span>

        <h2>{{ created }}</h2>
      </div>

      <div class="history-card updated">
        <span>Actualizados</span>

        <h2>{{ updated }}</h2>
      </div>

      <div class="history-card deleted">
        <span>Eliminados</span>

        <h2>{{ deleted }}</h2>
      </div>
    </div>

    <HistoryTable :history="filteredHistory" />
  </div>
</template>

<script setup>
import { onMounted, computed } from "vue";
import { useHistoryStore } from "@/stores/history.store";

import HistoryTable from "@/components/history/history-table/HistoryTable.vue";

const historyStore = useHistoryStore();

onMounted(async () => {
  await historyStore.fetchHistory();
});

const created = computed(
  () =>
    historyStore.history.filter((item) => item.action.includes("creado"))
      .length,
);

const updated = computed(
  () =>
    historyStore.history.filter((item) => item.action.includes("actualizado"))
      .length,
);

const deleted = computed(
  () =>
    historyStore.history.filter((item) => item.action.includes("eliminado"))
      .length,
);

const filteredHistory = computed(() => historyStore.history);
</script>

<style scoped src="./history-view.css"></style>
