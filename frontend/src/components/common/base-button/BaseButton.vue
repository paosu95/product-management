<template>

    <button
        class="base-button"
        :type="type"
        :disabled="disabled"
    >

        <slot />

    </button>

</template>

<script setup>

defineProps({

    type:{
        type:String,
        default:'button'
    },

    disabled:{
        type:Boolean,
        default:false
    }

})

</script>

<style scoped src="./base-button.css"></style>