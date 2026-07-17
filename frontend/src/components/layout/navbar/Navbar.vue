<template>

<header class="navbar">

    <div>

        <h2>Dashboard</h2>

        <p>Gestiona el inventario de productos.</p>

    </div>

    <div class="navbar-right">

        <div class="date">

            <i class="bi bi-calendar3"></i>

            {{ currentDate }}

        </div>

        <div class="user">

            <i class="bi bi-person-circle"></i>

            Administrador

        </div>

    </div>

</header>

</template>

<script setup>

const currentDate=new Date().toLocaleDateString("es-CO",{

    weekday:"long",

    year:"numeric",

    month:"long",

    day:"numeric"

})

</script>

<style src="./navbar.css"></style>