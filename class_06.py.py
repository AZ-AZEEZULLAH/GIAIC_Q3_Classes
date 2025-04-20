import requests
import json

# ✅ List: Mutable (changeable)
months: list[str] = ['January','February','March','April','May','June','July','August','September','October','November','December']

print(months[3:6])  # Prints April to June (index 3 to 5)
print(months[-3:-1])  # Prints last 3rd to 2nd months → ['June', 'July']
print(months[-1])  # Prints last month → 'August'
print(months[0:]) # Print January to December

# ✅ List is changeable
months[0] = "Septembere"
print(months)

# ✅ Tuple: Immutable (not changeable)
numbers: tuple[int] = (12,93,-21,45,87,89)
print(numbers[0:4])  # Slicing tuple → (12, 93, -21, 45)
print(numbers[-1:-4])  # Invalid backward slice → ()
print(numbers.count(12))  # Count occurrences of 12 in tuple → 1
# ✅ Tuple to List conversion (to allow change)
teacher_name: tuple[str] = ("Ali Jawad","Ahmed Ali", "Haseeb Ali")
print(type(teacher_name))  # <class 'tuple'>

tuple_to_list = list(teacher_name)
tuple_to_list.append("Ameen")  # Add new name
print(tuple_to_list)

teacher_name = tuple(tuple_to_list)  # Convert back to tuple
print(type(teacher_name))  # <class 'tuple'>

# ✅ Dictionary: Key-Value store
students_info = {
    "roll_number": 23455,
    "name": "Ali Jawad",
    "courses": ['Docker','FastAPI','OpenAI'],
    "assignments": {
        "assignOne": "assignTwo"
    }
}

# Looping through dictionary items
for hello, world in students_info.items():
    print(hello, world)

# ✅ For Loop: Print 1 to 9
for i in range(1, 10):
    print(i)

# ✅ While Loop: Print 0 to 8
i = 0
while i <= 8:
    print(i)
    i += 1

# ✅ Try-Except-Finally block: API call and error handling
try:
    url = requests.get("https://jsonplaceholder.typicode.com/posts")
    res = url.json()
    print(res)
except Exception as e:
    print("Error message:", e)
finally:
    print("This is finally block")

# ✅ Set: Unordered, no duplicates
my_favourite: set[str] = {"Coding", "Reading", "Teaching"}
my_favourite.add("Playing")  # Use .add(), not .append()
print(my_favourite)
