<template>

    <div class="table-actions">

        <button @click="$emit('edit')">

            <i class="bi bi-pencil-square"></i>

        </button>

        <button @click="$emit('delete')">

            <i class="bi bi-trash"></i>

        </button>

    </div>

</template>

<script setup>

defineEmits([
    'edit',
    'delete'
])

</script>

<style scoped src="./table-actions.css"></style>