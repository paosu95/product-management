<template>
  <div class="layout">

    <Sidebar />

    <div class="main-content">

      <Navbar />

      <main class="page-content">
        <router-view />
      </main>

    </div>

  </div>
</template>

<script setup>
import Sidebar from '../../components/layout/sidebar/Sidebar.vue'
import Navbar from '../../components/layout/navbar/Navbar.vue'
</script>

<style scoped src="./main-layout.css"></style>