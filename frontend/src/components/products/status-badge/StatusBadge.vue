<template>

    <span
        class="status-badge"
        :class="active ? 'active' : 'inactive'"
    >

        {{ active ? 'Activo' : 'Inactivo' }}

    </span>

</template>

<script setup>

defineProps({

    active:Boolean

})

</script>

<style scoped src="./status-badge.css"></style>