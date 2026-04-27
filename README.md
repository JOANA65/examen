# 📘 Examen: Desarrollo de API con Flask + Swagger

## 📌 Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando Flask, que permite gestionar una estructura académica con:

* Categorías
* Cursos
* Alumnos

Relaciones:

* Un curso pertenece a una categoría
* Un alumno puede estar inscrito en varios cursos

---

## 🚀 Tecnologías utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* Flasgger (Swagger)
* SQLite

---


## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/JOANA65/ExamenJ.git
cd ExamenJ
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar el proyecto

```bash
python app.py
```

---

### 5. Acceder a la API

* API: http://127.0.0.1:5000/
* Swagger: http://127.0.0.1:5000/apidocs

---

## 🧱 Base de datos

* Se utiliza SQLite
* La base de datos se crea automáticamente al ejecutar el proyecto
* Se insertan datos de prueba automáticamente
## 🗄️ ¿Por qué se utilizó SQLite?

Se eligió SQLite como sistema de base de datos por las siguientes razones:

* **Simplicidad:** No requiere instalación ni configuración adicional, lo que facilita la ejecución del proyecto.
* **Portabilidad:** La base de datos se guarda en un solo archivo, permitiendo que el proyecto funcione en cualquier equipo sin dependencias externas.
* **Rapidez para desarrollo:** Ideal para proyectos académicos y pruebas, ya que permite trabajar de forma ágil.
* **Cumple con los requisitos del examen:** Es una de las opciones recomendadas.

SQLite es una opción adecuada para este tipo de API, donde no se requiere alta concurrencia ni un servidor de base de datos complejo.

---

## 📊 Datos incluidos

* 2 categorías
* 10 cursos
* 5 alumnos
* Relaciones entre alumnos y cursos

---

## 🔌 Endpoints disponibles

### 📁 Categorías

* GET `/categories/` → Lista todas las categorías
* GET `/categories/{id}/courses` → Cursos de una categoría
* GET `/categories/{id}/courses/count` → Número de cursos

---

### 📁 Cursos

* GET `/courses/` → Lista todos los cursos
* GET `/courses/{id}/students` → Alumnos inscritos

---

### 📁 Alumnos

* GET `/students/` → Lista todos los alumnos
* GET `/students/{id}/courses` → Cursos de un alumno

---

### 🔑 Endpoint clave

* GET `/enrollments/`

Ejemplo de respuesta:

```json
[
  {
    "student": "Juan Perez",
    "courses": ["Python Básico", "Flask API"]
  }
]
```

---

## 📄 Documentación

Se implementa Swagger con Flasgger.

Acceso:
http://127.0.0.1:5000/apidocs

---

## 🌿 Control de versiones (Git)

* Se utilizó rama `develop` para desarrollo
* Rama `main` como principal
* Se realizó Pull Request de `develop` a `main`
* Commits descriptivos evidencian el avance del proyecto

---

## 📦 Archivos incluidos

* `app.py`
* `models/`
* `routes/`
* `extensions.py`
* `config.py`
* `requirements.txt`
* `schema.sql`
* `seed.sql`
* `README.md`

---

## ✅ Estado del proyecto

✔ API funcional
✔ Endpoints completos
✔ Swagger operativo
✔ Base de datos con datos de prueba
✔ Cumple con todos los requerimientos del examen

---

## 👩‍💻 Autor

Joana Benítez

---
