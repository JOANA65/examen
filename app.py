from flask import Flask
from flasgger import Swagger
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    # 🔥 Crear BD y datos automáticamente
    with app.app_context():
        from models.models import Category, Course, Student

        db.create_all()

        if not Category.query.first():

            # 📁 Categorías
            cat1 = Category(name="Programación")
            cat2 = Category(name="Diseño")

            db.session.add_all([cat1, cat2])
            db.session.commit()

            # 📚 Cursos
            courses = [
                Course(name="Python Básico", category_id=cat1.id),
                Course(name="Flask API", category_id=cat1.id),
                Course(name="JavaScript", category_id=cat1.id),
                Course(name="HTML", category_id=cat1.id),
                Course(name="CSS", category_id=cat1.id),
                Course(name="UI Design", category_id=cat2.id),
                Course(name="UX Research", category_id=cat2.id),
                Course(name="Photoshop", category_id=cat2.id),
                Course(name="Illustrator", category_id=cat2.id),
                Course(name="Figma", category_id=cat2.id),
            ]

            db.session.add_all(courses)
            db.session.commit()

            # 👨‍🎓 Alumnos
            students = [
                Student(name="Juan Perez"),
                Student(name="Maria Lopez"),
                Student(name="Carlos Ruiz"),
                Student(name="Ana Torres"),
                Student(name="Luis Gomez"),
            ]

            db.session.add_all(students)
            db.session.commit()

            # 🔗 Inscripciones
            students[0].courses.append(courses[0])
            students[0].courses.append(courses[1])

            students[1].courses.append(courses[2])
            students[1].courses.append(courses[3])

            students[2].courses.append(courses[4])
            students[2].courses.append(courses[5])

            students[3].courses.append(courses[6])
            students[3].courses.append(courses[7])

            students[4].courses.append(courses[8])
            students[4].courses.append(courses[9])

            db.session.commit()

    # 🔥 CONFIGURACIÓN CORRECTA DE SWAGGER
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API Examen Flask",
            "description": "Documentación de la API académica",
            "version": "1.0"
        }
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }

    Swagger(app, template=swagger_template, config=swagger_config)

    # 🔌 Blueprints
    from routes.categories import categories_bp
    from routes.courses import courses_bp
    from routes.students import students_bp
    from routes.enrollments import enrollments_bp

    app.register_blueprint(categories_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(enrollments_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)