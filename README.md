# 📘 Examen: Desarrollo de API con Flask + Swagger

---

## 🛠️ Desarrollo del Proyecto (Paso a Paso)

### 📌 Paso 1: Creación del proyecto

En la terminal:

```bash
mkdir examen
cd examen
```

Crear archivo README:

```bash
type nul > README.md
```

---

### 🌿 Paso 2: Inicializar repositorio Git

```bash
git init
git add .
git commit -m "Inicialización del proyecto"
git branch -M main
```

Conectar con GitHub:

```bash
git remote add origin https://github.com/JOANA65/ExamenJ.git
```

---

### 🔀 Paso 3: Crear rama de desarrollo

```bash
git checkout -b develop
git push -u origin develop
```

---

### 🐍 Paso 4: Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

Guardar avance:

```bash
git add .
git commit -m "Entorno virtual creado"
git push origin develop
```

---

### 📦 Paso 5: Instalación de dependencias

```bash
pip install flask
pip install flask-sqlalchemy
pip install flasgger
pip install gunicorn
```

Guardar dependencias:

```bash
pip freeze > requirements.txt
```

Guardar en Git:

```bash
git add .
git commit -m "Se agregan dependencias y requirements.txt"
git push origin develop
```

---

### 🧱 Paso 6: Estructura del proyecto

```text
examen/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── README.md
│
├── models/
│   └── models.py
│
├── routes/
│   ├── categories.py
│   ├── courses.py
│   ├── students.py
│   └── enrollments.py
```

---

## 📌 Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando Flask, que permite gestionar una estructura académica con:

* Categorías
* Cursos
* Alumnos

### 🔗 Relaciones:

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

### 5. Acceso

* API → http://127.0.0.1:5000/
* Swagger → http://127.0.0.1:5000/docs

---

## 🧱 Base de datos

* Se utiliza SQLite
* Se crea automáticamente al ejecutar el proyecto
* Se insertan datos de prueba automáticamente

### 📊 Datos incluidos:

* 2 categorías
* 10 cursos
* 5 alumnos
* Relaciones entre alumnos y cursos

---

## 🗄️ ¿Por qué SQLite?

Se eligió SQLite por:

* ✔ No requiere instalación
* ✔ Fácil de usar
* ✔ Portabilidad (archivo único)
* ✔ Ideal para proyectos académicos
* ✔ Cumple con los requisitos del examen

---

## 🔌 Endpoints

### 📁 Categorías

* GET `/categories/`
* GET `/categories/{id}/courses`
* GET `/categories/{id}/courses/count`

### 📁 Cursos

* GET `/courses/`
* GET `/courses/{id}/students`

### 📁 Alumnos

* GET `/students/`
* GET `/students/{id}/courses`

### 🔑 Endpoint clave

* GET `/enrollments/`

Ejemplo:

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

Swagger implementado con Flasgger:

👉 http://127.0.0.1:5000/docs

---

## 🌿 Control de versiones

* Rama principal: `main`
* Desarrollo en: `develop`
* Se realizó Pull Request de `develop` a `main`
* Commits claros y progresivos

---

## 📝 Detalle de commits

### 🔹 Inicialización del proyecto

* Creación del repositorio
* Archivo README.md

### 🔹 Entorno virtual

* Configuración del entorno de desarrollo

### 🔹 Dependencias

* Archivo requirements.txt

### 🔹 Aplicación principal

* Configuración de Flask
* Conexión a base de datos

### 🔹 Configuración base

* config.py
* extensions.py

### 🔹 Modelos

* Definición de entidades
* Scripts SQL

### 🔹 Endpoints

* Implementación de rutas REST

### 🔹 Documentación

* README completo

---

## 📦 Archivos incluidos

* app.py
* models/
* routes/
* config.py
* extensions.py
* requirements.txt
* schema.sql
* seed.sql
* README.md

---

## ✅ Estado del proyecto

✔ API funcional
✔ Endpoints completos
✔ Swagger operativo en `/docs`
✔ Base de datos automática
✔ Cumple todos los requisitos

---

## 👩‍💻 Autor

Joana Benítez
