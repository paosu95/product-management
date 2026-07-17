<template>

    <Teleport to="body">

        <div
            v-if="modelValue"
            class="modal-overlay"
            @click.self="close"
        >

            <div class="modal-container">

                <button
                    class="close-button"
                    @click="close"
                >
                    ✕
                </button>

                <header
                    v-if="$slots.header"
                    class="modal-header"
                >
                    <slot name="header" />
                </header>

                <section class="modal-body">
                    <slot />
                </section>

                <footer
                    v-if="$slots.footer"
                    class="modal-footer"
                >
                    <slot name="footer" />
                </footer>

            </div>

        </div>

    </Teleport>

</template>

<script setup>

defineProps({
    modelValue: Boolean
})

const emit = defineEmits([
    'update:modelValue'
])

function close() {
    emit('update:modelValue', false)
}

</script>

<style scoped src="./base-modal.css"></style>