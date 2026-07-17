import { defineStore } from "pinia";
import * as productService from "@/services/api/product.service";

export const useProductStore = defineStore("products", {
  state: () => ({
    products: [],
    loading: false,
    error: null,
  }),

  getters: {
    totalProducts: (state) => state.products.length,

    activeProducts: (state) =>
      state.products.filter((p) => p.status).length,

    inactiveProducts: (state) =>
      state.products.filter((p) => !p.status).length,
  },

  actions: {
    async fetchProducts(search = "") {
      this.loading = true;
      this.error = null;

      try {
        const response = await productService.getProducts(search);
        this.products = response.data;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },

    async createProduct(product) {
      await productService.createProduct(product);
      await this.fetchProducts();
    },

    async updateProduct(id, product) {
      await productService.updateProduct(id, product);
      await this.fetchProducts();
    },

    async deleteProduct(id) {
      await productService.deleteProduct(id);
      await this.fetchProducts();
    },

    async changeStatus(id, status) {
      await productService.updateStatus(id, status);
      await this.fetchProducts();
    },
  },
});