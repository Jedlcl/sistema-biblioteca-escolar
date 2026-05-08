# 📚 Biblio-IA — Sistema de Gestión Bibliotecaria Escolar

Sistema local para digitalizar y automatizar el control de préstamos de libros en una escuela primaria pública, con soporte para dos turnos (Matutino y Vespertino). Diseñado para funcionar sin conexión a internet, en equipos de bajos recursos, e integrado con Inteligencia Artificial para el registro y clasificación automática de libros.

---

## 🎯 Objetivo

Permitir a maestros y personal directivo:

- Registrar libros automáticamente escaneando su ISBN (con NER/IA).
- Clasificar libros por categoría de forma automática.
- Gestionar ejemplares físicos con código de barras único por copia.
- Registrar y consultar préstamos vinculados a alumno, maestro y ejemplar.
- Ver historial completo de préstamos por alumno, libro o maestro.
- Actualizar el ciclo escolar automáticamente (promoción de grados).
- Operar de forma independiente para dos escuelas (CCTs distintos) bajo una misma base de datos.

---

## 👥 Usuarios del sistema

| Rol | Permisos |
|---|---|
| **Root** | Acceso total al sistema |
| **Director/a** | Gestión de alumnos, ciclo escolar, eliminar libros |
| **Maestro/a** | Registro de préstamos y devoluciones |

---

## 🗄️ Base de datos

- **Motor:** SQLite (local, sin servidor, compatible con hardware antiguo)
- **Tablas:** Escuela, Salón, Maestro, Alumno, Libro, Categoría, Libro_Categoría, Ejemplar, Préstamo, Usuario
- **Borrado lógico:** Ningún registro se elimina físicamente; se usa el campo `activo` para mantener el historial íntegro.

---

## 📋 Estado del proyecto

| Fase | Estado |
|---|---|
| Requerimientos funcionales | ✅ Completado |
| Diseño E-R y Diccionario de datos | ✅ Completado |
