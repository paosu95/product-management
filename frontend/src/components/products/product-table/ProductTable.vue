<template>
  <div class="product-table">
    <table>
      <thead>
        <tr>
          <th @click="sortBy('name')" class="sortable">
            Nombre {{ getArrow("name") }}
          </th>

          <th @click="sortBy('description')" class="sortable">
            Descripción {{ getArrow("description") }}
          </th>

          <th @click="sortBy('price')" class="sortable">
            Precio {{ getArrow("price") }}
          </th>

          <th @click="sortBy('stock')" class="sortable">
            Stock {{ getArrow("stock") }}
          </th>

          <th @click="sortBy('status')" class="sortable">
            Estado {{ getArrow("status") }}
          </th>

          <th>Acciones</th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="product in sortedProducts"
          :key="product.id"
        >
          <td>{{ product.name }}</td>

          <td>{{ product.description }}</td>

          <td>${{ product.price }}</td>

          <td>{{ product.stock }}</td>

          <td>
            <StatusBadge :status="product.status" />
          </td>

          <td>
            <TableActions
              @edit="editProduct(product)"
              @delete="deleteProduct(product)"
              @history="historyProduct(product)"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

import StatusBadge from "../status-badge/StatusBadge.vue";
import TableActions from "../table-actions/TableActions.vue";

const props = defineProps({
  products: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits([
  "edit",
  "delete",
  "history",
]);

const currentSort = ref("name");
const currentDirection = ref("asc");

const sortedProducts = computed(() => {
  const products = [...props.products];

  return products.sort((a, b) => {
    let valueA = a[currentSort.value];
    let valueB = b[currentSort.value];

    if (typeof valueA === "string") {
      valueA = valueA.toLowerCase();
      valueB = valueB.toLowerCase();
    }

    if (valueA < valueB) return currentDirection.value === "asc" ? -1 : 1;
    if (valueA > valueB) return currentDirection.value === "asc" ? 1 : -1;

    return 0;
  });
});

function sortBy(column) {
  if (currentSort.value === column) {
    currentDirection.value =
      currentDirection.value === "asc" ? "desc" : "asc";
  } else {
    currentSort.value = column;
    currentDirection.value = "asc";
  }
}

function getArrow(column) {
  if (currentSort.value !== column) {
    return "⇅";
  }

  return currentDirection.value === "asc" ? "▲" : "▼";
}

function editProduct(product) {
  emit("edit", product);
}

function deleteProduct(product) {
  emit("delete", product);
}

function historyProduct(product) {
  emit("history", product);
}
</script>

<style scoped src="./product-table.css"></style>