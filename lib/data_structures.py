spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names
    pass

def get_spiciest_foods(spicy_foods):
    foods = [food for food in spicy_foods if food["heat_level"]>5]
    return foods
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level="🌶" * food["heat_level"]
        spicy_food = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}"
        print(spicy_food)
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
        
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_emojis = "🌶" * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
    pass

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level
    pass

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
    pass
