<template>

    <div class="search-toolbar">

        <div class="search-toolbar__search">

            <BaseInput
                v-model="search"
                type="text"
                placeholder="Buscar productos..."
            />

        </div>

        <div class="search-toolbar__actions">

            <BaseButton @click="handleCreate">

                <i class="bi bi-plus-lg"></i>

                <span>Nuevo Producto</span>

            </BaseButton>

        </div>

    </div>

</template>

<script setup>
import { ref, watch } from 'vue'

import BaseButton from '@/components/common/base-button/BaseButton.vue'
import BaseInput from '@/components/common/base-input/BaseInput.vue'

const emit = defineEmits([
    'create',
    'search'
])

const search = ref('')

function handleCreate() {
    emit('create')
}

watch(search, (value) => {
    emit('search', value)
})
</script>

<style scoped src="./search-toolbar.css"></style>