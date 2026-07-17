<template>
  <div class="stats-grid">
    <div
      v-for="stat in cards"
      :key="stat.filter"
      class="base-card stat-card"
      @click="selectFilter(stat.filter)"
    >
      <div class="icon-container">
        <i class="bi" :class="stat.icon"></i>
      </div>

      <div class="stat-content">
        <h3>{{ stat.value }}</h3>
        <span>{{ stat.title }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from "vue";

import BaseCard from "@/components/common/base-card/BaseCard.vue";

const props = defineProps({
  stats: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["filter"]);

const selectedFilter = ref("all");

function selectFilter(filter) {
  console.log("Click:", filter);

  selectedFilter.value = filter;
  emit("filter", filter);
}

const cards = computed(() => [
  {
    title: "Productos",
    value: props.stats.total,
    icon: "bi-box-seam",
    filter: "all",
  },
  {
    title: "Activos",
    value: props.stats.active,
    icon: "bi-check-circle-fill",
    filter: "active",
  },
  {
    title: "Inactivos",
    value: props.stats.inactive,
    icon: "bi-x-circle-fill",
    filter: "inactive",
  },
  {
    title: "Stock Total",
    value: props.stats.totalStock,
    icon: "bi-boxes",
    filter: "stock",
  },
]);
</script>

<style scoped src="./product-stats.css"></style>
