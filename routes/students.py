from flask import Blueprint, jsonify
from models.models import Student

students_bp = Blueprint('students', __name__, url_prefix='/students')


@students_bp.route('/', methods=['GET'])
def get_students():
    """
    Obtener todos los alumnos
    ---
    tags:
      - Alumnos
    responses:
      200:
        description: Lista de alumnos
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
                example: Juan Perez
    """
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name} for s in students])


@students_bp.route('/<int:id>/courses', methods=['GET'])
def get_courses_by_student(id):
    """
    Obtener cursos de un alumno
    ---
    tags:
      - Alumnos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del alumno
    responses:
      200:
        description: Lista de cursos
        schema:
          type: array
          items:
            type: string
            example: Python Básico
      404:
        description: Alumno no encontrado
    """
    student = Student.query.get_or_404(id)
    return jsonify([c.name for c in student.courses])