<template>
  <ProductStats :stats="stats" @filter="filterByStatus" />

  <SearchToolbar @create="openProductModal" @search="handleSearch" />

 <ProductTable
  :products="paginatedProducts"
  @edit="editProduct"
  @delete="confirmDelete"
  @history="openHistory"
  @toggle-status="toggleStatus"
/>

  <div class="pagination" v-if="totalPages > 1">
    <button @click="currentPage--" :disabled="currentPage === 1">
      ← Anterior
    </button>

    <span> Página {{ currentPage }} de {{ totalPages }} </span>

    <button @click="currentPage++" :disabled="currentPage === totalPages">
      Siguiente →
    </button>
  </div>

  <ProductModal
    v-model="showModal"
    :product="selectedProduct"
    :isEditing="isEditing"
    @save="saveProduct"
  />

  <DeleteModal
    v-model="showDeleteModal"
    :product="selectedProduct"
    @confirm="confirmDelete"
  />

  <HistoryModal
    v-model="showHistoryModal"
    :product="selectedProduct"
    :history="selectedHistory"
  />
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import Swal from "sweetalert2";

import { useProductStore } from "@/stores/product.store";
import { useHistoryStore } from "@/stores/history.store";

import ProductStats from "@/components/products/product-stats/ProductStats.vue";
import SearchToolbar from "@/components/products/search-toolbar/SearchToolbar.vue";
import ProductTable from "@/components/products/product-table/ProductTable.vue";
import ProductModal from "@/components/products/product-modal/ProductModal.vue";
import DeleteModal from "@/components/products/delete-modal/DeleteModal.vue";
import HistoryModal from "@/components/history/history-modal/HistoryModal.vue";

const productStore = useProductStore();
const historyStore = useHistoryStore();

const showModal = ref(false);
const showDeleteModal = ref(false);
const showHistoryModal = ref(false);

const isEditing = ref(false);
const selectedProduct = ref(null);

const search = ref("");
const statusFilter = ref("all");

const currentPage = ref(1);
const itemsPerPage = 5;

onMounted(async () => {
  await Promise.all([
    productStore.fetchProducts(),
    historyStore.fetchHistory(),
  ]);
});

const filteredProducts = computed(() => {
  let products = productStore.products;

  if (search.value.trim()) {
    products = products.filter((product) =>
      product.name.toLowerCase().includes(search.value.toLowerCase())
    );
  }

  switch (statusFilter.value) {
    case "active":
      products = products.filter((product) => product.status);
      break;

    case "inactive":
      products = products.filter((product) => !product.status);
      break;

    default:
      break;
  }

  return products;
});

const totalPages = computed(() =>
  Math.ceil(filteredProducts.value.length / itemsPerPage),
);

const paginatedProducts = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;

  return filteredProducts.value.slice(start, start + itemsPerPage);
});

const stats = computed(() => {
  const total = productStore.products.length;

  const active = productStore.products.filter(
    (product) => product.status,
  ).length;

  const inactive = total - active;

  const totalStock = productStore.products.reduce(
    (sum, product) => sum + Number(product.stock),
    0,
  );

  return {
    total,
    active,
    inactive,
    totalStock,
  };
});

const selectedHistory = computed(() => {
  if (!selectedProduct.value) return [];

  return historyStore.history.filter(
    (item) => item.product_name === selectedProduct.value.name,
  );
});

function openProductModal() {
  selectedProduct.value = null;
  isEditing.value = false;
  showModal.value = true;
}

async function saveProduct(product) {
  try {
    if (isEditing.value) {
      await productStore.updateProduct(product.id, product);
    } else {
      await productStore.createProduct(product);
    }

    await historyStore.fetchHistory();

    Swal.fire({
      icon: "success",
      title: isEditing.value ? "Producto actualizado" : "Producto creado",
      text: isEditing.value
        ? "El producto fue actualizado correctamente."
        : "El producto fue creado correctamente.",
      timer: 1800,
      showConfirmButton: false,
    });

    showModal.value = false;
    selectedProduct.value = null;
    isEditing.value = false;
  } catch (error) {
    Swal.fire({
      icon: "error",
      title: "Error",
      text: "Ocurrió un error al guardar el producto.",
    });
  }
}

function editProduct(product) {
  selectedProduct.value = { ...product };
  isEditing.value = true;
  showModal.value = true;
}

function deleteProduct(product) {
  selectedProduct.value = product;
  showDeleteModal.value = true;
}

async function confirmDelete(product) {
  try {
    await productStore.deleteProduct(product.id);

    await historyStore.fetchHistory();

    Swal.fire({
      icon: "success",
      title: "Producto eliminado",
      text: "El producto fue eliminado correctamente.",
      timer: 1800,
      showConfirmButton: false,
    });

    showDeleteModal.value = false;
    selectedProduct.value = null;
  } catch (error) {
    Swal.fire({
      icon: "error",
      title: "Error",
      text: "No fue posible eliminar el producto.",
    });
  }
}

function openHistory(product) {
  selectedProduct.value = product;
  showHistoryModal.value = true;
}

function handleSearch(value) {
  search.value = value;
  currentPage.value = 1;
}

function filterByStatus(filter) {
  statusFilter.value = filter;
  currentPage.value = 1;
}
async function toggleStatus(product) {
  try {
    await productStore.changeStatus(
      product.id,
      !product.status
    );

    await historyStore.fetchHistory();
  } catch (error) {
    console.error(error);
  }
}
</script>

<style scoped src="./products-view.css"></style>
