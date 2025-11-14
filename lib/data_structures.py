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
    return[food["name"]for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return[food_item for food_item in spicy_foods if food_item["heat_level"]>5]
    pass

def print_spicy_foods(spicy_foods):
    for food_item in spicy_foods:
        name = food_item["name"]
        cuisine = food_item["cuisine"]
        heat_icons = "🌶"* food_item["heat_level"]

        output = f"{name} ({cuisine}) | Heat Level: {heat_icons}"
        print(output)
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food_item in spicy_foods:
        if food_item["cuisine"] == cuisine:
           return food_item
    pass

def print_spiciest_foods(spicy_foods):
    for food_item in spicy_foods:

        if food_item["heat_level"] > 5:
           name = food_item["name"]
           cuisine = food_item.get("cuisine")
           heat_icons = "🌶"* food_item["heat_level"]

           output = f"{name} ({cuisine}) | Heat Level: {heat_icons}"

           print(output)
    pass

def get_average_heat_level(spicy_foods):
    total_heat = 0

    for food_item in spicy_foods:
        total_heat += food_item["heat_level"]

    number_of_items = len(spicy_foods)

    average = total_heat // number_of_items
    return average
    pass

def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods
    pass
