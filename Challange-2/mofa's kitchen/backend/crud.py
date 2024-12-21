from backend.database import db_manager
from backend.models import Ingredient, Recipe
from typing import List, Optional
from bson import ObjectId

class IngredientCRUD:
    @staticmethod
    def create_ingredient(ingredient: Ingredient):
        collection = db_manager.get_ingredients_collection()
        ingredient_dict = ingredient.dict(by_alias=True)
        result = collection.insert_one(ingredient_dict)
        return str(result.inserted_id)

    @staticmethod
    def get_all_ingredients() -> List[Ingredient]:
        collection = db_manager.get_ingredients_collection()
        ingredients = list(collection.find())
        return [Ingredient(**ingredient) for ingredient in ingredients]

    @staticmethod
    def update_ingredient(ingredient_id: str, update_data: dict):
        collection = db_manager.get_ingredients_collection()
        result = collection.update_one(
            {'_id': ObjectId(ingredient_id)}, 
            {'$set': update_data}
        )
        return result.modified_count > 0

class RecipeCRUD:
    @staticmethod
    def create_recipe(recipe: Recipe):
        collection = db_manager.get_recipes_collection()
        recipe_dict = recipe.dict(by_alias=True)
        result = collection.insert_one(recipe_dict)
        return str(result.inserted_id)

    @staticmethod
    def find_recipes_by_ingredients(ingredients: List[str]):
        collection = db_manager.get_recipes_collection()
        recipes = list(collection.find({
            'ingredients': {'$all': ingredients}
        }))
        return [Recipe(**recipe) for recipe in recipes]