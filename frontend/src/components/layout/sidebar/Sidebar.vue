<template>
  <div class="sidebar-container">

    <div class="logo">

      <div class="logo-icon">
        <i class="bi bi-box-seam"></i>
      </div>

      <div>
        <h2>Nova Inventory</h2>
        <span>Management System</span>
      </div>

    </div>

    <nav>

      <RouterLink to="/products">
        <i class="bi bi-box-seam"></i>
        <span>Productos</span>
      </RouterLink>

      <RouterLink to="/history">
        <i class="bi bi-clock-history"></i>
        <span>Historial</span>
      </RouterLink>

    </nav>

    <div class="sidebar-footer">

      <div class="avatar">

        <i class="bi bi-person-circle"></i>

      </div>

      <div>

        <strong>Administrador</strong>

        <p>Online</p>

      </div>

    </div>

  </div>
</template>

<script setup>
</script>

<style src="./sidebar.css"></style>