<template>

    <form
        class="product-form"
        @submit.prevent="handleSubmit"
    >

        <BaseInput
            v-model="form.name"
            label="Nombre"
            placeholder="Nombre del producto"
        />

        <BaseInput
            v-model="form.category"
            label="Categoría"
            placeholder="Categoría"
        />

        <BaseInput
            v-model.number="form.price"
            type="number"
            label="Precio"
            placeholder="0"
        />

        <BaseInput
            v-model.number="form.stock"
            type="number"
            label="Stock"
            placeholder="0"
        />

        <div class="form-group">

            <label>

                Estado

            </label>

            <select v-model="form.active">

                <option :value="true">

                    Activo

                </option>

                <option :value="false">

                    Inactivo

                </option>

            </select>

        </div>

        <div class="buttons">

            <BaseButton
                type="button"
                @click="$emit('cancel')"
            >

                Cancelar

            </BaseButton>

            <BaseButton
                type="submit"
            >

                {{ isEditing ? 'Actualizar' : 'Guardar' }}

            </BaseButton>

        </div>

    </form>

</template>

<script setup>

import { reactive, watch } from 'vue'

import BaseInput from '@/components/common/base-input/BaseInput.vue'
import BaseButton from '@/components/common/base-button/BaseButton.vue'

const props = defineProps({

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

    'save',

    'cancel'

])

const form = reactive({

    id:null,

    name:'',

    category:'',

    price:0,

    stock:0,

    active:true

})

watch(

    () => props.product,

    (product)=>{

        if(product){

            form.id = product.id

            form.name = product.name

            form.category = product.category

            form.price = product.price

            form.stock = product.stock

            form.active = product.active

        }else{

            resetForm()

        }

    },

    {

        immediate:true

    }

)

function resetForm(){

    form.id = null

    form.name = ''

    form.category = ''

    form.price = 0

    form.stock = 0

    form.active = true

}

function handleSubmit(){

    if(

        form.name.trim() === '' ||

        form.category.trim() === ''

    ){

        alert('Complete todos los campos.')

        return

    }

    emit(

        'save',

        {

            ...form,

            id: form.id ?? Date.now()

        }

    )

    resetForm()

}

</script>

<style scoped src="./product-form.css"></style>