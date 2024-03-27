import random

# Define lists of dishes for each mealtime
breakfast_options = ['Oatmeal', 'Eggs and Toast', 'Smoothie Bowl', 'Pancakes', 'Avocado Toast']
lunch_options = ['Grilled Chicken Salad', 'Vegetable Stir-Fry', 'Quinoa Bowl', 'Turkey Sandwich', 'Sushi']
dinner_options = ['Spaghetti Bolognese', 'Grilled Salmon with Vegetables', 'Taco Night', 'Vegetarian Curry', 'Steak with Mashed Potatoes']

# Define days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Generate meal plan for the week
for day in days_of_week:
    breakfast_choice = random.choice(breakfast_options)
    lunch_choice = random.choice(lunch_options)
    dinner_choice = random.choice(dinner_options)
    
    print(f"On {day}:")
    print(f"Breakfast: {breakfast_choice}")
    print(f"Lunch: {lunch_choice}")
    print(f"Dinner: {dinner_choice}")
    print()



















