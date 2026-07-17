<template>
  <span
    class="status-badge"
    :class="status ? 'active' : 'inactive'"
  >
    {{ status ? "Activo" : "Inactivo" }}
  </span>
</template>

<script setup>
defineProps({
  status: {
    type: Boolean,
    default: false,
  },
});
</script>

<style scoped src="./status-badge.css"></style>