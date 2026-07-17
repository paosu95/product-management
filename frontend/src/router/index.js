import { createRouter, createWebHistory } from 'vue-router'

import DashboardView from '../views/DashboardView.vue'
import ProductsView from '../views/ProductsView.vue'

const routes = [

    {
        path:'/',
        name:'dashboard',
        component:DashboardView
    },

    {
        path:'/products',
        name:'products',
        component:ProductsView
    }

]

export default createRouter({

    history:createWebHistory(),

    routes

})