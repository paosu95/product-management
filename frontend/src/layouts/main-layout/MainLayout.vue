<template>
  <div class="app-layout">

    <aside class="sidebar">
      <Sidebar />
    </aside>

    <div class="main-content">

      <Navbar />

      <main class="content">
        <RouterView />
      </main>

    </div>

  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'

import Sidebar from '@/components/layout/sidebar/Sidebar.vue'
import Navbar from '@/components/layout/navbar/Navbar.vue'
</script>

<style src="./main-layout.css"></style>