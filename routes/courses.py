from flask import Blueprint, jsonify
from models.models import Course

courses_bp = Blueprint('courses', __name__, url_prefix='/courses')


@courses_bp.route('/', methods=['GET'])
def get_courses():
    """
    Obtener todos los cursos
    ---
    tags:
      - Cursos
    responses:
      200:
        description: Lista de cursos
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: Python Básico
    """
    courses = Course.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in courses])


@courses_bp.route('/<int:id>/students', methods=['GET'])
def get_students_by_course(id):
    """
    Obtener alumnos inscritos en un curso
    ---
    tags:
      - Cursos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del curso
    responses:
      200:
        description: Lista de alumnos
        schema:
          type: array
          items:
            type: string
            example: Juan Perez
      404:
        description: Curso no encontrado
    """
    course = Course.query.get_or_404(id)
    return jsonify([s.name for s in course.students])