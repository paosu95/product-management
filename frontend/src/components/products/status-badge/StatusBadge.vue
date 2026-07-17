<template>
  <span
    class="badge"
    :class="status ? 'active' : 'inactive'"
    @click="$emit('toggle')"
  >
    {{ status ? "Activo" : "Inactivo" }}
  </span>
</template>

<script setup>
defineProps({
  status: Boolean
})

defineEmits(["toggle"])
</script>

<style scoped src="./status-badge.css"></style>