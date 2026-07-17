import { createRouter, createWebHistory } from 'vue-router'

import MainLayout from '@/layouts/main-layout/MainLayout.vue'

import ProductsView from '@/views/products/ProductsView.vue'
import HistoryView from '@/views/HistoryView/HistoryView.vue'

const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: '',
        redirect: '/products'
      },
      {
        path: 'products',
        name: 'products',
        component: ProductsView
      },
      {
        path: 'history',
        name: 'history',
        component: HistoryView
      }
    ]
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})