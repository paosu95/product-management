<template>

    <ProductStats />

    <SearchToolbar
        @create="openProductModal"
    />

    <ProductTable
        :products="products"
        @edit="editProduct"
        @delete="deleteProduct"
    />

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

</template>

<script setup>

import { ref } from 'vue'

import ProductStats from '@/components/products/product-stats/ProductStats.vue'
import SearchToolbar from '@/components/products/search-toolbar/SearchToolbar.vue'
import ProductTable from '@/components/products/product-table/ProductTable.vue'
import ProductModal from '@/components/products/product-modal/ProductModal.vue'
import DeleteModal from '@/components/products/delete-modal/DeleteModal.vue'

const showModal = ref(false)
const showDeleteModal = ref(false)

const isEditing = ref(false)

const selectedProduct = ref(null)

const products = ref([
    {
        id: 1,
        name: 'Laptop',
        category: 'Tecnología',
        price: 1200,
        stock: 10,
        active: true
    },
    {
        id: 2,
        name: 'Mouse',
        category: 'Accesorios',
        price: 30,
        stock: 50,
        active: true
    },
    {
        id: 3,
        name: 'Monitor',
        category: 'Tecnología',
        price: 350,
        stock: 8,
        active: false
    }
])

function openProductModal() {

    selectedProduct.value = null

    isEditing.value = false

    showModal.value = true

}

function saveProduct(product) {

    if (isEditing.value) {

        const index = products.value.findIndex(

            p => p.id === product.id

        )

        if (index !== -1) {

            products.value[index] = {
                ...product
            }

        }

    } else {

        products.value.push(product)

    }

    showModal.value = false

    selectedProduct.value = null

    isEditing.value = false

}

function editProduct(product) {

    selectedProduct.value = {
        ...product
    }

    isEditing.value = true

    showModal.value = true

}

function deleteProduct(product) {

    selectedProduct.value = product

    showDeleteModal.value = true

}

function confirmDelete(product) {

    products.value = products.value.filter(

        p => p.id !== product.id

    )

    selectedProduct.value = null

    showDeleteModal.value = false

}

</script>

<style scoped src="./products-view.css"></style>