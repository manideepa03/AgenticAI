import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"))

MAX_RETRIES = 5

# Example user constraints
RECIPE_REQUEST = """
Create a dinner recipe with the following requirements:
- Must be high in protein (at least 30g per serving)
- Must be low in carbohydrates (under 15g per serving)
- Cannot contain gluten, dairy, or nuts (severe allergies)
- Must be suitable for someone with diabetes (low glycemic index)
- Should have no more than 8 ingredients
- Must be flavorful and appealing to someone who normally eats a standard American diet
- Total preparation and cooking time should be under 30 minutes
- Should contain at least 3 different vegetables
- Must include a source of omega-3 fatty acids
"""
recipe_request_dict = {}

class RecipeCreatorAgent:
    def create_recipe(self, recipe_request, feedback=None):
        system_prompt = """You are an innovative and highly skilled chef, renowned for creating delicious
        recipes that also meet specific dietary and nutritional targets. 
        You are good at interpreting user requests and also at refining your creations 
        based on precise feedback.        
        """
        base_dish = recipe_request
    
        user_prompt_text = f"Please create a '{base_dish}' recipe that meets all of the following constraints in it"
        if feedback:
            user_prompt_text += f"\n\nIMPORTANT: Your previous attempt had issues. Please revise the recipe based on this specific feedback: {feedback}\nEnsure all original constraints AND this feedback are addressed."
        else:
            user_prompt_text += "\nThis is the first attempt."
            user_prompt_text += "\n\nPlease provide: a creative name for the dish, a list of ingredients (with quantities), step-by-step instructions, an estimated calorie count per serving, an estimated protein content (grams) per serving, and a short description of its taste profile."
        
        response = client.chat.completions.create(
            model= "gpt-4",
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt_text}
            ],
            temperature = 0.7
        )
        print(f" the recipe is {response.choices[0].message.content}")

        return response.choices[0].message.content

class NutritionEvaluatorAgent:
    def evaluate(self, recipe_request, proposed_recipe):
        """Check if the proposed recipe meets all specified constraints and requirements."""

        system_prompt = """You are a strict dietitian. Your job is to find ANY and ALL violations of dietary constraints.
        Do not accept approximations. Be meticulous and provide corrective feedback."""

        user_prompt = f"""Recipe Request: {recipe_request}
        
        Proposed Recipe:
        {proposed_recipe}
        
        Please evaluate this recipe against ALL the specified requirements.
        Check EACH constraint individually and confirm whether it is satisfied:
        
        1. Is the protein content at least 30g per serving?
        2. Is the carbohydrate content under 15g per serving?
        3. Does it contain ANY gluten, dairy, or nuts (even trace amounts)?
        4. Is it suitable for someone with diabetes (low glycemic index foods)?
        5. Does it have no more than 8 ingredients?
        6. Would it be flavorful and appealing to someone used to standard American diet?
        7. Is total preparation and cooking time under 30 minutes?
        8. Does it contain at least 3 different vegetables?
        9. Does it include a source of omega-3 fatty acids?
        
        If ALL constraints are fully satisfied, begin your response with "APPROVED: This recipe meets all requirements."
        
        Otherwise, list specifically which requirements are NOT met and provide detailed suggestions for how to modify 
        the recipe to meet those requirements while maintaining the integrity of the dish."""

        response = client.chat.completions.create(
            model= "gpt-4",
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature = 0.1
        )
        print(f" the recipe is {response.choices[0].message.content}")

        return response.choices[0].message.content

def optimize_recipe(recipe_request):
        recipe_creator = RecipeCreatorAgent()
        evaluator = NutritionEvaluatorAgent()
        current_feedback = None

        for attempt in range(MAX_RETRIES):
            print(f"\n--- Attempt {attempt + 1} of {MAX_RETRIES} ---")
            current_recipe_str = recipe_creator.create_recipe(RECIPE_REQUEST, current_feedback)
            print(f"💡 Chef Proposed:\n{current_recipe_str}")
            evaluation_str = evaluator.evaluate(RECIPE_REQUEST, current_recipe_str)
            print(f"🧐 Critic's Evaluation:\n{evaluation_str}")

            if "overall status: passed" in evaluation_str.lower():
                print("\n✅ Recipe Approved by Evaluator!")
                return current_recipe_str, evaluation_str, attempt + 1 # Return success
            else:
                current_feedback = evaluation_str

        print(f"\n❌ Failed to meet all constraints after {MAX_RETRIES} attempts.")
        
        return current_recipe_str, evaluation_str, MAX_RETRIES

if __name__ == "__main__":
    print("Recipe Optimizer for Dietary Restrictions")
    print("\nRecipe Request:")
    print(RECIPE_REQUEST)
    print("\nCreating optimized recipe...")

    recipe, evaluation, attempts = optimize_recipe(RECIPE_REQUEST)

    if "APPROVED" in evaluation:
        print("\n✅ All dietary constraints satisfied!")
    else:
        print("\n⚠️ Could not satisfy all constraints after maximum retries.")

    print("\nFinal Recipe:")
    print(recipe)

    print("\nEvaluation:")
    print(evaluation)




