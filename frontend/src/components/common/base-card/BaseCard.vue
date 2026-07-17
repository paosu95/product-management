<template>
  <div class="base-card" v-bind="$attrs">
    <slot />
  </div>
</template>

<script setup>
defineOptions({
  inheritAttrs: false,
});
</script>

<style scoped src="./base-card.css"></style>