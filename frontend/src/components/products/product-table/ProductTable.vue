<template>

    <div class="product-table">

        <table>

            <thead>

                <tr>

                    <th>Nombre</th>

                    <th>Categoría</th>

                    <th>Precio</th>

                    <th>Stock</th>

                    <th>Estado</th>

                    <th>Acciones</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="product in products"
                    :key="product.id"
                >

                    <td>{{ product.name }}</td>

                    <td>{{ product.category }}</td>

                    <td>${{ product.price }}</td>

                    <td>{{ product.stock }}</td>

                    <td>

                        <StatusBadge
                            :active="product.active"
                        />

                    </td>

                    <td>

                        <TableActions
                            @edit="editProduct(product)"
                            @delete="deleteProduct(product)"
                        />

                    </td>

                </tr>

            </tbody>

        </table>

    </div>

</template>

<script setup>

import StatusBadge from '../status-badge/StatusBadge.vue'
import TableActions from '../table-actions/TableActions.vue'

const props = defineProps({

    products:{
        type:Array,
        default:() => []
    }

})

const emit = defineEmits([
    'edit',
    'delete'
])

function editProduct(product){

    emit('edit',product)

}

function deleteProduct(product){

    emit('delete',product)

}

</script>

<style scoped src="./product-table.css"></style>