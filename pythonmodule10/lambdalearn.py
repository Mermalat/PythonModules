# Help me learn how to use lambda functions in Python.
# Lambda functions are anonymous functions in Python that are defined using the `lambda` keyword. They can take any number of arguments but can only have one expression.
# The expression is evaluated and returned when the lambda function is called.

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )

# The `artifact_sorter` function takes a list of artifacts (dictionaries) and sorts them in descending order based on their "power" attribute using a lambda function as the key for sorting.
# Why there is key=lambda artifact: artifact["power"]?
# The `key=lambda artifact: artifact["power"]` part of the `sorted` function is used to specify the sorting criteria. The `key` parameter allows you to provide a function that extracts
# The value to be used for sorting from each element in the list.

liste12 = [{"name": "Crystal Orb", "power": 85, "type": "focus"},
           {"name": "Fire Staff", "power": 92, "type": "weapon"},
           {"name": "Moon Amulet", "power": 67, "type": "charm"}]

liste21 = sorted(liste12, key=lambda artifact: artifact["power"], reverse=True)

print(liste12)
print("Testing artifact sorter...")
print(liste21)

# So the lambda part is where we decide what attribute of the artifact we want to sort by.
# In this case, we want to sort by the "power" attribute, so we use `lambda artifact: artifact["power"]`.

def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    powers = list(map(lambda mage: mage["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }

# Bu kismi anlayamadim, aciklar misin?
# The `mage_stats` function calculates statistics about a list of mages, specifically their maximum power, minimum power, and average power. Let's break it down step by step:
# How does it work?
# 1. The function takes a list of mages, where each mage is represented as a dictionary containing attributes like "name", "power", and "element".
# 2. It first checks if the list of mages is empty. If it is, it returns a dictionary with default values for max_power, min_power, and avg_power.
# 3. If the list is not empty, it uses the `map` function along with a lambda function to extract the "power" attribute from each mage in the list. The `map` function applies the lambda function to each element in the `mages` list, creating a new list of powers.
# 4. It then calculates the maximum power using the `max` function, the minimum power using the `min` function, and the average power by summing the powers and dividing by the number of mages. The average is rounded to two decimal places.
# 5. Finally, it returns a dictionary containing the calculated statistics.

# Can you write me some lambda exercises to practice with?
# Sure! Here are some lambda function exercises to help you practice:
# Exercise 1: Create a lambda function that takes two numbers and returns their sum.
sum_lambda = lambda x, y: x + y
print(sum_lambda(5, 3))  # Output: 8

# Exercise 2: Create a list of numbers and use a lambda function with the `filter` function to return only the even numbers from the list.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Exercise 3: Create a list of strings and use a lambda function with the `map` function to convert all strings to uppercase.
strings = ["hello", "world", "python"]
uppercase_strings = list(map(lambda s: s.upper(), strings))
print(uppercase_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Exercise 4: Create a list of dictionaries representing students with their names and grades. Use a lambda function to sort the list of students by their grades in descending order.
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
]
sorted_students = sorted(students, key=lambda student: student["grade"], reverse=True)
print(sorted_students)  # Output: [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 78}]

sorted_students_names = sorted(students, key=lambda student: student["name"])
print(sorted_students_names)  # Output: [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}, {'name': 'Charlie', 'grade': 78}]