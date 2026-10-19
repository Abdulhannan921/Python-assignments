# Q31. Dictionary Access
# student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
# Extract name and marks; retrieve missing city with default Karachi.

student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}

name = student["name"]
marks = student["marks"]
city = student.get("city", "Karachi")   # key missing, so default is returned

print(name)    # Ali
print(marks)   # 85
print(city)    # Karachi

# Q32. Update Dictionary
# employee = {"name": "Sara", "salary": 100000, "department": "IT"}
# Raise salary by 20%, add bonus 15000, change department to Data Engineering.

employee = {"name": "Sara", "salary": 100000, "department": "IT"}

employee["salary"] = round(employee["salary"] * 1.20)
employee["bonus"] = 15000
employee["department"] = "Data Engineering"

print(employee)
# {'name': 'Sara', 'salary': 120000, 'department': 'Data Engineering', 'bonus': 15000}

# Q33. Dictionary Methods
# product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
# Extract keys, values, items; remove stock and retain its value.

product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}

print(product.keys())     # dict_keys(['id', 'name', 'price', 'stock'])
print(product.values())   # dict_values([101, 'Laptop', 120000, 5])
print(product.items())    # dict_items([('id', 101), ('name', 'Laptop'), ('price', 120000), ('stock', 5)])

removed_stock = product.pop("stock")   # pop() removes the key and returns its value

print(removed_stock)   # 5
print(product)         # {'id': 101, 'name': 'Laptop', 'price': 120000}

# Q34. Merge Dictionaries
# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"b": 50, "d": 40}
# Merge so dict2 overrides overlapping keys.

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}

merged = {**dict1, **dict2}   # later dictionary (dict2) wins on duplicate keys

print(merged)   # {'a': 10, 'b': 50, 'c': 30, 'd': 40}

# Alternative: merged = dict1 | dict2

# Q35. Student Marks
# marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}
# Find highest, lowest, average, and top-scoring student without loops or lambda.

marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}

highest = max(marks.values())
lowest = min(marks.values())
average = sum(marks.values()) / len(marks)
top_student = max(marks, key=marks.get)   # marks.get used instead of lambda

print(highest)       # 92
print(lowest)        # 78
print(average)       # 85.75
print(top_student)   # Sara

# Q36. Nested Employee Records
# employees = {
#     "E101": {"name": "Ali", "salary": 80000},
#     "E102": {"name": "Sara", "salary": 120000},
#     "E103": {"name": "Ahmed", "salary": 95000}
# }
# Extract Sara salary, increase Ali salary 15%, and calculate total payroll.

employees = {
    "E101": {"name": "Ali", "salary": 80000},
    "E102": {"name": "Sara", "salary": 120000},
    "E103": {"name": "Ahmed", "salary": 95000}
}

sara_salary = employees["E102"]["salary"]
employees["E101"]["salary"] = round(employees["E101"]["salary"] * 1.15)
total_payroll = sum(emp["salary"] for emp in employees.values())

print(sara_salary)                    # 120000
print(employees["E101"]["salary"])    # 92000
print(total_payroll)                  # 307000

# Q37. Dictionary Inversion
# data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
# Create inverse dictionary without loops or comprehensions.

data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}

inverse = dict(zip(data.values(), data.keys()))

print(inverse)   # {'Ali': 'Python', 'Sara': 'SQL', 'Ahmed': 'AWS'}

# Q38. Order Calculation
# order = {
#     "laptop": {"price": 120000, "quantity": 2},
#     "mouse": {"price": 1500, "quantity": 5},
#     "keyboard": {"price": 3500, "quantity": 3}
# }
# Calculate subtotals, grand total, and amount after 10% discount.

order = {
    "laptop": {"price": 120000, "quantity": 2},
    "mouse": {"price": 1500, "quantity": 5},
    "keyboard": {"price": 3500, "quantity": 3}
}

subtotals = {item: d["price"] * d["quantity"] for item, d in order.items()}
grand_total = sum(subtotals.values())
after_discount = grand_total * 0.90

print(subtotals)        # {'laptop': 240000, 'mouse': 7500, 'keyboard': 10500}
print(grand_total)      # 258000
print(after_discount)   # 232200.0

# Q39. Employee Performance
# employees = {
#     "Ali": {"python": 90, "sql": 85, "aws": 88},
#     "Sara": {"python": 95, "sql": 92, "aws": 90},
#     "Ahmed": {"python": 80, "sql": 87, "aws": 84}
# }
# Calculate each average, top performer, and highest SQL score.

employees = {
    "Ali": {"python": 90, "sql": 85, "aws": 88},
    "Sara": {"python": 95, "sql": 92, "aws": 90},
    "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}

averages = {name: sum(s.values()) / len(s) for name, s in employees.items()}
top_performer = max(averages, key=averages.get)
highest_sql = max(s["sql"] for s in employees.values())

print({n: round(a, 2) for n, a in averages.items()})
# {'Ali': 87.67, 'Sara': 92.33, 'Ahmed': 83.67}
print(top_performer)   # Sara
print(highest_sql)     # 92

# Q40. Inventory Management
# inventory = {
#     "P101": {"name": "Laptop", "price": 120000, "stock": 5},
#     "P102": {"name": "Mouse", "price": 1500, "stock": 20},
#     "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
# }
# Calculate total value, most valuable item by price x stock,
# and update stock after selling two laptops and five mice.

inventory = {
    "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}

total_value = sum(i["price"] * i["stock"] for i in inventory.values())

most_valuable_id = max(inventory, key=lambda k: inventory[k]["price"] * inventory[k]["stock"])
most_valuable_item = inventory[most_valuable_id]["name"]

inventory["P101"]["stock"] -= 2   # sold 2 laptops
inventory["P102"]["stock"] -= 5   # sold 5 mice

print(total_value)          # 665000
print(most_valuable_item)   # Laptop
print(inventory["P101"]["stock"])   # 3
print(inventory["P102"]["stock"])   # 15