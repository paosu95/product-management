import api from "./axios";

export const getProducts = (search = "") =>
  api.get(`/products/?search=${search}`);

export const getProduct = (id) =>
  api.get(`/products/${id}`);

export const createProduct = (product) =>
  api.post("/products/", product);

export const updateProduct = (id, product) =>
  api.put(`/products/${id}`, product);

export const deleteProduct = (id) =>
  api.delete(`/products/${id}`);

export const updateStatus = (id, status) =>
  api.patch(`/products/${id}/status`, {
    status,
  });