import google.generativeai as genai
import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class RecipeRecommendationEngine:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_GENERATIVE_AI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_recommendations(self, available_ingredients: List[str], preference: str):
        try:
            prompt = f"""
            Available Ingredients: {', '.join(available_ingredients)}
            User Preference: {preference}

            Generate 3 creative recipe recommendations that:
            1. Use most of the available ingredients
            2. Match the user's preference
            3. Are easy to prepare
            4. Provide nutritional insights
            """

            response = self.model.generate_content(prompt)
            return response.text.split('\n\n')
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return [f"An error occurred: {str(e)}"]

    def nutritional_analysis(self, recipe: str) -> str:
        try:
            prompt = f"""
            Perform a detailed nutritional analysis of the following recipe:
            {recipe}

            Provide:
            - Estimated Calories
            - Macronutrient Breakdown (Proteins, Carbs, Fats)
            - Key Vitamins and Minerals
            - Dietary Considerations
            """

            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Nutritional analysis error: {str(e)}"

class DietaryAssistant:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_GENERATIVE_AI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro')

    def meal_plan_generator(self, dietary_restrictions: List[str], calorie_goal: int, cuisine_preference: str = None) -> dict:
        try:
            prompt = f"""
            Create a comprehensive 3-day meal plan with the following specifications:
            Dietary Restrictions: {', '.join(dietary_restrictions)}
            Daily Calorie Goal: {calorie_goal} calories
            Cuisine Preference: {cuisine_preference or 'Mixed'}

            For each day, provide:
            1. Breakfast
            2. Morning Snack
            3. Lunch
            4. Afternoon Snack
            5. Dinner
            6. Evening Snack

            Include:
            - Recipe names
            - Brief preparation instructions
            - Nutritional breakdown
            - Ingredient list
            """

            response = self.model.generate_content(prompt)
            meal_plan = {
                "dietary_restrictions": dietary_restrictions,
                "calorie_goal": calorie_goal,
                "plan": response.text
            }
            return meal_plan
        except Exception as e:
            return {
                "error": f"Meal plan generation failed: {str(e)}",
                "details": str(e)
            }

def ingredient_substitution_finder(original_ingredient: str) -> List[str]:
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""
        Provide a list of potential substitutes for {original_ingredient}

        For each substitute, include:
        - Substitute name
        - Flavor profile
        - Nutritional comparison
        - Cooking adjustment tips
        """

        response = model.generate_content(prompt)
        return response.text.split('\n')
    except Exception as e:
        return [f"Substitution search failed: {str(e)}"]
