<template>

    <BaseModal
        :modelValue="modelValue"
        @update:modelValue="close"
    >

        <template #header>

            <h2>

                Eliminar Producto

            </h2>

        </template>

        <p class="message">

            ¿Está seguro de eliminar el producto

            <strong>

                "{{ product?.name }}"

            </strong>?

        </p>

        <template #footer>

            <BaseButton
                @click="close"
            >

                Cancelar

            </BaseButton>

            <BaseButton
                @click="confirmDelete"
            >

                Eliminar

            </BaseButton>

        </template>

    </BaseModal>

</template>

<script setup>

import BaseModal from '@/components/common/base-modal/BaseModal.vue'
import BaseButton from '@/components/common/base-button/BaseButton.vue'

const props = defineProps({

    modelValue:Boolean,

    product:Object

})

const emit = defineEmits([

    'update:modelValue',

    'confirm'

])

function close(){

    emit('update:modelValue', false)

}

function confirmDelete(){

    emit('confirm', props.product)

    close()

}

</script>

<style scoped src="./delete-modal.css"></style>