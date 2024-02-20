import json

name = input("Name: ")
age = input("Age: ")
favoriteFood = input("Favorite Food: ")

user = {
    "Name": name,
    "Age": age,
    "Favorite_food": favoriteFood
}

data = json.dumps(user, indent=2)

with open("output.json", "w") as file:
    file.write(data)
