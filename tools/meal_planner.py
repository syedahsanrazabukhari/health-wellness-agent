from agents import function_tool, RunContextWrapper
from pydantic import BaseModel
from typing import List

class MealPlan(BaseModel):
    weekly_plan: List[str]

@function_tool
async def plan_meals(ctx: RunContextWrapper) -> MealPlan:
    preferences = (ctx.context.diet_preferences or "balanced").lower()
    goal = (ctx.context.goal or {}).get("type", "").lower()

    def calorie_tag(base):
        if goal == "weight gain":
            return f"🍽️ High-Calorie: {base}"
        elif goal == "weight loss":
            return f"🥗 Low-Calorie: {base}"
        else:
            return base

    if "vegetarian" in preferences:
        meals = [
            calorie_tag("Tofu stir-fry with vegetables"),
            calorie_tag("Lentil soup with whole grain bread"),
            calorie_tag("Paneer and quinoa bowl"),
            calorie_tag("Chickpea curry with brown rice"),
            calorie_tag("Stuffed peppers with oats"),
            calorie_tag("Vegetable pasta mix"),
            calorie_tag("Spinach mushroom wrap")
        ]
    elif "vegan" in preferences:
        meals = [
            calorie_tag("Quinoa salad with roasted veggies"),
            calorie_tag("Vegan chili with beans"),
            calorie_tag("Tofu scramble with avocado toast"),
            calorie_tag("Lentil dal with rice"),
            calorie_tag("Tempeh stir-fry"),
            calorie_tag("Grilled veggie burger"),
            calorie_tag("Hummus and salad wrap")
        ]
    elif "keto" in preferences:
        meals = [
            calorie_tag("Grilled salmon with avocado salad"),
            calorie_tag("Chicken casserole with cheese"),
            calorie_tag("Spinach mushroom omelette"),
            calorie_tag("Zucchini noodles with pesto"),
            calorie_tag("Beef steak with asparagus"),
            calorie_tag("Tuna salad with olive oil"),
            calorie_tag("Bacon and egg muffins")
        ]
    elif "high-protein" in preferences:
        meals = [
            calorie_tag("Grilled chicken with quinoa"),
            calorie_tag("Steak with mashed sweet potatoes"),
            calorie_tag("Protein pancakes with nut butter"),
            calorie_tag("Tuna egg salad"),
            calorie_tag("Greek yogurt with nuts"),
            calorie_tag("Turkey meatballs and rice"),
            calorie_tag("Whey chia smoothie")
        ]
    elif "low-carb" in preferences:
        meals = [
            calorie_tag("Chicken broccoli stir-fry"),
            calorie_tag("Cauliflower crust pizza"),
            calorie_tag("Turkey lettuce wraps"),
            calorie_tag("Grilled shrimp with veggies"),
            calorie_tag("Zucchini noodles with meatballs"),
            calorie_tag("Stuffed cabbage rolls"),
            calorie_tag("Spinach and boiled eggs salad")
        ]
    elif "diabetic" in preferences:
        meals = [
            calorie_tag("Grilled chicken with steamed veggies"),
            calorie_tag("Lentil soup with whole grain toast"),
            calorie_tag("Quinoa and bean salad"),
            calorie_tag("Baked fish with sweet potato"),
            calorie_tag("Tofu vegetable stir-fry"),
            calorie_tag("Turkey veggie wraps"),
            calorie_tag("Low-sugar oatmeal with seeds")
        ]
    else:
        meals = [
            calorie_tag("Grilled chicken with veggies"),
            calorie_tag("Mixed vegetable salad"),
            calorie_tag("Oats porridge with fruits"),
            calorie_tag("Brown rice with lentils"),
            calorie_tag("Egg and spinach scramble"),
            calorie_tag("Fruit smoothie bowl"),
            calorie_tag("Yogurt with nuts")
        ]

    ctx.context.meal_plan = meals
    return MealPlan(weekly_plan=meals)
