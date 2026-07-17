<template>
  <aside class="sidebar">

    <div class="logo">

      <div class="logo-icon">
        <i class="bi bi-box-seam-fill"></i>
      </div>

      <div>
        <h3>Nova</h3>
        <span>Inventory</span>
      </div>

    </div>

    <nav class="menu">

      <RouterLink to="/" class="menu-item">

        <i class="bi bi-grid-fill"></i>

        Dashboard

      </RouterLink>

      <RouterLink to="/products" class="menu-item">

        <i class="bi bi-box-fill"></i>

        Productos

      </RouterLink>

      <RouterLink to="/history" class="menu-item">

        <i class="bi bi-clock-history"></i>

        Historial

      </RouterLink>

    </nav>

    <div class="sidebar-footer">

      <img
        src="https://i.pravatar.cc/100"
        class="avatar"
      >

      <div>

        <h5>Administrador</h5>

        <span>Nova Inventory</span>

      </div>

    </div>

  </aside>
</template>

<style scoped src="./sidebar.css"></style>