<template>

    <div class="stats-grid">

        <BaseCard
            v-for="stat in cards"
            :key="stat.title"
            class="stat-card"
        >

            <div class="icon-container">

                <i
                    class="bi"
                    :class="stat.icon"
                ></i>

            </div>

            <div class="stat-content">

                <h3>{{ stat.value }}</h3>

                <span>{{ stat.title }}</span>

            </div>

        </BaseCard>

    </div>

</template>

<script setup>

import { computed } from 'vue'

import BaseCard from '@/components/common/base-card/BaseCard.vue'

const props = defineProps({

    stats:{

        type:Object,

        required:true

    }

})

const cards = computed(() => [

    {

        title:'Productos',

        value:props.stats.total,

        icon:'bi-box-seam'

    },

    {

        title:'Activos',

        value:props.stats.active,

        icon:'bi-check-circle-fill'

    },

    {

        title:'Inactivos',

        value:props.stats.inactive,

        icon:'bi-x-circle-fill'

    },

    {

        title:'Stock Total',

        value:props.stats.totalStock,

        icon:'bi-boxes'

    }

])

</script>

<style scoped src="./product-stats.css"></style>