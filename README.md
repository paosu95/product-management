# Product Management System

Prueba técnica Full Stack desarrollada con Vue 3, FastAPI y PostgreSQL para la gestión de productos.

---

# Tecnologías

## Frontend

- Vue 3
- Vite
- Pinia
- Vue Router
- Axios
- Bootstrap Icons
- SweetAlert2

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

---

# Requisitos

Antes de ejecutar el proyecto debe tener instalado:

- Node.js 20 o superior
- Python 3.11 o superior
- PostgreSQL 15 o superior
- Git

---

# Clonar el proyecto

```bash
git clone https://github.com/paosu95/product-management.git

cd NOMBRE_REPOSITORIO
```

---

# Base de datos

Crear una base de datos en PostgreSQL.

Ejemplo:

```sql
CREATE DATABASE product_management;
```

Ejecutar posteriormente el script:

```
database/database.sql
```

---

# Variables de entorno

## Backend

Crear un archivo `.env` tomando como base:

```
.env.example
```

Ejemplo:

```
DATABASE_URL=postgresql://postgres:postgres123@localhost:5432/product_management
```

---

# Instalación Backend

```bash
cd backend

python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# Instalación Frontend

```bash
cd frontend

npm install
```

Ejecutar

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# Funcionalidades

- Crear productos
- Editar productos
- Eliminar productos
- Activar / desactivar productos
- Búsqueda por nombre
- Ordenamiento de columnas
- Paginación
- Dashboard con estadísticas
- Historial completo de cambios
- Historial por producto
- Confirmaciones con SweetAlert2
- Diseño responsive

---

# API

## Endpoints

GET

```
/products
```

GET

```
/products/{id}
```

POST

```
/products
```

PUT

```
/products/{id}
```

PATCH

```
/products/{id}/status
```

DELETE

```
/products/{id}
```

GET

```
/history
```

---

# Autor

Gina Paola Suarez
