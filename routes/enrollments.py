from flask import Blueprint, jsonify
from models.models import Student

enrollments_bp = Blueprint('enrollments', __name__, url_prefix='/enrollments')


@enrollments_bp.route('/', methods=['GET'])
def get_enrollments():
    """
    Obtener inscripciones (alumnos y sus cursos)
    ---
    tags:
      - Inscripciones
    responses:
      200:
        description: Lista de alumnos con sus cursos
        schema:
          type: array
          items:
            type: object
            properties:
              student:
                type: string
                example: Juan Perez
              courses:
                type: array
                items:
                  type: string
                  example: Python Básico
    """
    students = Student.query.all()

    result = []
    for s in students:
        result.append({
            "student": s.name,
            "courses": [c.name for c in s.courses]
        })

    return jsonify(result)