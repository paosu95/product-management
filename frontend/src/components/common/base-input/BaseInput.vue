<template>

    <div class="base-input-container">

        <label
            v-if="label"
            class="base-input-label"
        >
            {{ label }}
        </label>

        <input
            class="base-input"
            :type="type"
            :placeholder="placeholder"
            :value="modelValue"
            @input="updateValue"
        >

    </div>

</template>

<script setup>

defineProps({

    modelValue:{

        type:[
            String,
            Number
        ],

        default:''

    },

    label:String,

    placeholder:String,

    type:{
        type:String,
        default:'text'
    }

})

const emit = defineEmits([
    'update:modelValue'
])

function updateValue(event){

    emit(
        'update:modelValue',
        event.target.value
    )

}

</script>

<style scoped src="./base-input.css"></style>