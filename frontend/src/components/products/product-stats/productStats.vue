<template>
    <div class="stats-grid">

        <BaseCard
            v-for="stat in stats"
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
import BaseCard from '@/components/common/base-card/BaseCard.vue'

const stats = [
    {
        title: 'Productos',
        value: 154,
        icon: 'bi-box-seam'
    },
    {
        title: 'Activos',
        value: 120,
        icon: 'bi-check-circle-fill'
    },
    {
        title: 'Inactivos',
        value: 34,
        icon: 'bi-x-circle-fill'
    },
    {
        title: 'Inventario',
        value: '$58.420',
        icon: 'bi-currency-dollar'
    }
]
</script>

<style scoped src="./product-stats.css"></style>