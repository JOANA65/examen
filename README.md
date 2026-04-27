🧪 Examen: Desarrollo de API con Flask + Swagger
📌 Descripción general
El objetivo de este examen es que el alumno desarrolle una API REST profesional utilizando Flask, aplicando buenas prácticas de estructuración, modelado de datos y documentación.

El sistema deberá representar una estructura académica con:

Categorías
Cursos
Alumnos
Donde:

Un curso pertenece a una categoría
Un alumno puede estar inscrito en uno o varios cursos
🎯 Requerimientos funcionales
📚 Modelo de datos
Se debe implementar la siguiente relación:

Categoría

id
nombre
Curso

id
nombre
categoria_id (FK)
Alumno

id
nombre
📊 Reglas mínimas de datos
La base de datos debe incluir como mínimo:

✅ 2 categorías
✅ 10 cursos distribuidos en las categorías
✅ Alumnos (cantidad libre, mínimo sugerido: 10)
✅ Relaciones entre alumnos y cursos
🔌 Endpoints requeridos
📁 Categorías
GET /categories

Lista todas las categorías
GET /categories/{id}/courses

Devuelve los cursos de una categoría
GET /categories/{id}/courses/count

Devuelve cuántos cursos tiene una categoría
📁 Cursos
GET /courses

Lista todos los cursos
GET /courses/{id}/students

Lista los alumnos inscritos en un curso
📁 Alumnos
GET /students

Lista todos los alumnos
GET /students/{id}/courses

Lista los cursos en los que está inscrito un alumno
📁 Endpoint clave del examen
GET /enrollments

Debe devolver una estructura donde se indique:

Alumno
Cursos en los que está inscrito
Ejemplo esperado:

[
  {
    "student": "Juan Pérez",
    "courses": ["Python Básico", "Flask API"]
  }
]
📄 Documentación con Swagger
Se debe integrar documentación usando Swagger.

Requisito obligatorio:
Acceso a documentación vía navegador Ejemplo:

http://localhost:5000/docs
🗄️ Base de datos
Puede utilizar:

SQLite (recomendado)
MySQL
PostgreSQL
📌 Requisitos:
Incluir script de creación de tablas (schema.sql) o migraciones
Incluir script de inserción de datos (seed.sql)
📦 Entregables
El alumno debe entregar:

Código fuente completo
Archivo README.md (con instrucciones claras)
Script de base de datos (schema.sql)
Script de datos (seed.sql)
Archivo requirements.txt
Documentación Swagger funcionando
⚠️ Criterios de evaluación
✔️ Buen diseño de endpoints REST
✔️ Uso adecuado de Flask
✔️ Documentación Swagger funcional
✔️ Organización del proyecto
✔️ Claridad en README
✔️ Datos de prueba funcionales
⏰ Fecha límite de entrega
📅 Lunes a las 6:00 PM La entrega compartirar el link de su proyecto al siguiente correo ricardo.lugo@utvtol.edu.mx

📝 Notas adicionales
No se permite copiar proyectos existentes
Se evaluará la comprensión del desarrollo, no solo que funcione
Se recomienda aplicar buenas prácticas (modularización, naming, etc.)
🌿 Requerimientos de control de versiones (Git)
El proyecto debe entregarse en un repositorio Git (GitHub, GitLab o similar) cumpliendo con lo siguiente:

🔀 Uso de ramas
No trabajar directamente en main o master
Uso de al menos una rama para desarrollo
🔁 Pull Request (PR)
Crear un Pull Request hacia la rama principal
El PR debe incluir una descripción clara de los cambios realizados
📝 Commits
Los commits deben ser claros y descriptivos
Se debe evidenciar el avance del desarrollo del proyecto
Éxito en el desarrollo 🚀

📊 Rúbrica de Evaluación (Total: 10 puntos)
Criterio	Descripción	Puntos
🧱 Modelado de Base de Datos	Esquemas y script correctos	1.0
📊 Datos mínimos (seed.sql)	Cumple con: 2 categorías, 10 cursos, alumnos y relaciones	0.5
🔌 Endpoints REST	Implementación completa y correcta de todos los endpoints requeridos	2.5
🔑 Endpoint /enrollments	Respuesta correcta, estructura clara y lógica bien implementada	1.5
📄 Swagger (documentación)	Documentación funcional accesible en /docs	1.5
🧠 Uso de Flask	Separación de responsabilidades, buenas prácticas	1.0
🧱 Estructura del proyecto	Organización clara (models, routes, controllers, etc.)	0.5
📘 README	Instrucciones claras para ejecutar el proyecto	0.5
⚙️ Ejecución funcional	El proyecto corre sin errores y responde correctamente	0.5
🌿 Uso de Git (branch y PR)	Uso adecuado de ramas y Pull Request	0.3
📝 Commits	Commits claros y descriptivos	0.2
TOTAL	10
About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Contributors
1
@richie20502
richie20502 El Richie
