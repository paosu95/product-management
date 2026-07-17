import Swal from "sweetalert2";

export const successAlert = (title) => {
  Swal.fire({
    icon: "success",
    title,
    showConfirmButton: false,
    timer: 1800,
  });
};

export const errorAlert = (message) => {
  Swal.fire({
    icon: "error",
    title: "Error",
    text: message,
  });
};

export const confirmDelete = async () => {
  return await Swal.fire({
    title: "¿Eliminar producto?",
    text: "Esta acción no se puede deshacer.",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  });
};