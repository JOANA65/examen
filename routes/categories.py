from flask import Blueprint, jsonify
from models.models import Category

# Usamos prefix (mejor práctica 🔥)
categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['GET'])
def get_categories():
    """
    Obtener todas las categorías
    ---
    tags:
      - Categorías
    responses:
      200:
        description: Lista de categorías
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
                example: Programación
    """
    data = Category.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in data])


@categories_bp.route('/<int:id>/courses', methods=['GET'])
def get_courses_by_category(id):
    """
    Obtener cursos por categoría
    ---
    tags:
      - Categorías
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la categoría
    responses:
      200:
        description: Lista de cursos
        schema:
          type: array
          items:
            type: string
            example: Python Básico
      404:
        description: Categoría no encontrada
    """
    category = Category.query.get_or_404(id)
    return jsonify([c.name for c in category.courses])


@categories_bp.route('/<int:id>/courses/count', methods=['GET'])
def count_courses(id):
    """
    Contar cursos de una categoría
    ---
    tags:
      - Categorías
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la categoría
    responses:
      200:
        description: Número de cursos
        schema:
          type: object
          properties:
            count:
              type: integer
              example: 5
      404:
        description: Categoría no encontrada
    """
    category = Category.query.get_or_404(id)
    return jsonify({"count": len(category.courses)})