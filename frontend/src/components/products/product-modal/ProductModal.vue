<template>

    <BaseModal
        :modelValue="modelValue"
        @update:modelValue="closeModal"
    >

        <template #header>

            <h2>

                {{ isEditing ? 'Editar Producto' : 'Nuevo Producto' }}

            </h2>

        </template>

        <ProductForm
            :product="product"
            :isEditing="isEditing"
            @save="saveProduct"
            @cancel="closeModal"
        />

    </BaseModal>

</template>

<script setup>

import BaseModal from '@/components/common/base-modal/BaseModal.vue'
import ProductForm from '../product-form/ProductForm.vue'

const props = defineProps({

    modelValue:{

        type:Boolean,

        default:false

    },

    product:{

        type:Object,

        default:null

    },

    isEditing:{

        type:Boolean,

        default:false

    }

})

const emit = defineEmits([

    'update:modelValue',

    'save'

])

function closeModal(){

    emit('update:modelValue', false)

}

function saveProduct(product){

    emit('save', product)

    closeModal()

}

</script>

<style scoped src="./product-modal.css"></style>