# Q11. Tuple Indexing
# colors = ("red", "green", "blue", "yellow", "purple")
# Extract second, last, and middle three elements.

colors = ("red", "green", "blue", "yellow", "purple")

second = colors[1]
last = colors[-1]
middle_three = colors[1:4]

print(second)         # green
print(last)           # purple
print(middle_three)   # ('green', 'blue', 'yellow')

# Q12. Tuple Unpacking
# employee = ("Ali", 28, "Data Engineer", 150000)
# Unpack into four variables and display name and salary.

employee = ("Ali", 28, "Data Engineer", 150000)

name, age, job, salary = employee

print("Name:", name)       # Name: Ali
print("Salary:", salary)   # Salary: 150000

# Q13. Tuple Concatenation
# tuple1 = (10, 20, 30)
# tuple2 = (40, 50, 60)
# Combine tuples, then create another tuple in reverse order.

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

combined = tuple1 + tuple2
reversed_tuple = combined[::-1]

print(combined)         # (10, 20, 30, 40, 50, 60)
print(reversed_tuple)   # (60, 50, 40, 30, 20, 10)

# Q14. Count and Locate
# numbers = (10, 20, 30, 20, 40, 20, 50)
# Count occurrences of 20 and find the first index.

numbers = (10, 20, 30, 20, 40, 20, 50)

count_20 = numbers.count(20)
first_index = numbers.index(20)

print(count_20)      # 3
print(first_index)   # 1

# Q15. Extended Tuple Unpacking
# data = (100, 200, 300, 400, 500, 600)
# Unpack first two and last into variables;
# put all remaining elements into a list.

data = (100, 200, 300, 400, 500, 600)

first, second, *remaining, last = data

print(first, second, last)   # 100 200 600
print(remaining)             # [300, 400, 500]

# Q16. Modify an Immutable Tuple
# numbers = (10, 20, 30, 40, 50)
# Create a new tuple replacing 30 with 300.

numbers = (10, 20, 30, 40, 50)

index = numbers.index(30)
new_numbers = numbers[:index] + (300,) + numbers[index + 1:]

print(new_numbers)   # (10, 20, 300, 40, 50)
print(numbers)       # (10, 20, 30, 40, 50) (original unchanged)

# Q17. Nested Tuple Access
# students = (
#     ("Ali", (85, 90, 88)),
#     ("Sara", (92, 87, 95)),
#     ("Ahmed", (78, 84, 80))
# )
# Extract Sara second score, Ali average, and Ahmed highest score.

students = (
    ("Ali", (85, 90, 88)),
    ("Sara", (92, 87, 95)),
    ("Ahmed", (78, 84, 80))
)

sara_second = students[1][1][1]
ali_average = sum(students[0][1]) / len(students[0][1])
ahmed_highest = max(students[2][1])

print(sara_second)               # 87
print(round(ali_average, 2))     # 87.67
print(ahmed_highest)             # 84

# Q18. Tuple Sorting
# employees = (
#     ("Ali", 80000),
#     ("Sara", 120000),
#     ("Ahmed", 95000)
# )
# Sort by salary descending without loops, comprehensions, or lambda.

from operator import itemgetter

employees = (
    ("Ali", 80000),
    ("Sara", 120000),
    ("Ahmed", 95000)
)

sorted_employees = tuple(sorted(employees, key=itemgetter(1), reverse=True))

print(sorted_employees)
# (('Sara', 120000), ('Ahmed', 95000), ('Ali', 80000))

# Q19. Tuple Matrix
# matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))
# Extract diagonal, calculate its product, and build a tuple of row sums.

from math import prod

matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))

diagonal = tuple(matrix[i][i] for i in range(len(matrix)))
diagonal_product = prod(diagonal)
row_sums = tuple(sum(row) for row in matrix)

print(diagonal)           # (2, 10, 18)
print(diagonal_product)   # 360
print(row_sums)           # (12, 30, 48)

# Q20. Inventory Tuple Challenge
# records = (
#     ("Laptop", 120000, 5),
#     ("Mouse", 1500, 20),
#     ("Keyboard", 3500, 10)
# )
# Calculate inventory value, find most expensive product,
# and build reversed tuple of names.

records = (
    ("Laptop", 120000, 5),
    ("Mouse", 1500, 20),
    ("Keyboard", 3500, 10)
)

inventory_value = sum(price * qty for name, price, qty in records)
most_expensive = max(records, key=lambda r: r[1])[0]
names = tuple(name for name, price, qty in records)
reversed_names = names[::-1]

print(inventory_value)   # 665000
print(most_expensive)    # Laptop
print(reversed_names)    # ('Keyboard', 'Mouse', 'Laptop')
