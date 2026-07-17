<template>
  <header class="navbar">

    <div class="navbar-left">
      <h2>¡Bienvenida! 👋</h2>
      <p>Gestiona tu inventario de manera eficiente.</p>
    </div>

    <div class="navbar-right">

      <div class="search-box">
        <i class="bi bi-search"></i>
        <input
          type="text"
          placeholder="Buscar..."
        />
      </div>

      <button class="icon-btn">
        <i class="bi bi-bell"></i>
      </button>

      <div class="profile">

        <img
          src="https://i.pravatar.cc/100?img=32"
          alt="Avatar"
        />

        <div>
          <h4>Administrador</h4>
          <span>Nova Inventory</span>
        </div>

      </div>

    </div>

  </header>
</template>

<style scoped src="./navbar.css"></style>