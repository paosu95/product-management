<template>

<div class="sidebar-container">

    <div class="logo">

        <i class="bi bi-box-seam"></i>

        <span>Product Manager</span>

    </div>

    <nav>

        <RouterLink to="/products">

            <i class="bi bi-box"></i>

            Productos

        </RouterLink>

        <RouterLink to="/history">

            <i class="bi bi-clock-history"></i>

            Historial

        </RouterLink>

    </nav>

</div>

</template>

<script setup>
</script>

<style src="./sidebar.css"></style>