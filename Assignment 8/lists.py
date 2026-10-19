# Q1. Accessing List Elements
# numbers = [10, 20, 30, 40, 50, 60, 70]
# Extract the first, middle, and last elements without modifying the original list.

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

print(first, middle, last)   # 10 40 70
print(numbers)               # original list unchanged

# Q2. List Slicing
# numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# Create three new lists: first five elements, last four elements,
# and every second element in reverse order.

numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

first_five = numbers[:5]
last_four = numbers[-4:]
every_second_reversed = numbers[::-2]

print(first_five)              # [5, 10, 15, 20, 25]
print(last_four)               # [35, 40, 45, 50]
print(every_second_reversed)   # [50, 40, 30, 20, 10]

# Q3. List Modification
# fruits = ["apple", "banana", "cherry", "mango"]
# Replace banana with orange, add grapes at index 2, and remove cherry.

fruits = ["apple", "banana", "cherry", "mango"]

fruits[1] = "orange"        # replace banana with orange
fruits.insert(2, "grapes")  # add grapes at index 2
fruits.remove("cherry")     # remove cherry

print(fruits)  # ['apple', 'orange', 'grapes', 'mango']

# Q4. Reverse Without reverse()
# numbers = [12, 45, 23, 67, 89, 34]
# Reverse using slicing only; preserve the original list.

numbers = [12, 45, 23, 67, 89, 34]

reversed_numbers = numbers[::-1]

print(reversed_numbers)   # [34, 89, 67, 23, 45, 12]
print(numbers)            # [12, 45, 23, 67, 89, 34] (original unchanged)

# Q5. Second Largest Unique Number
# numbers = [45, 12, 89, 34, 89, 67, 45, 23]
# Find the second-largest unique number. Expected: 67.

numbers = [45, 12, 89, 34, 89, 67, 45, 23]

unique_sorted = sorted(set(numbers), reverse=True)   # [89, 67, 45, 34, 23, 12]
second_largest = unique_sorted[1]

print(second_largest)   # 67

# Q6. Rotate a List
# numbers = [10, 20, 30, 40, 50, 60]
# k = 2
# Rotate the list right by k using slicing.
# Expected: [50, 60, 10, 20, 30, 40].

numbers = [10, 20, 30, 40, 50, 60]
k = 2

k = k % len(numbers)   # handles k larger than the list length
rotated = numbers[-k:] + numbers[:-k]

print(rotated)   # [50, 60, 10, 20, 30, 40]

# Q7. Remove Duplicates, Preserve Order
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]
# Remove duplicates while preserving first-occurrence order.

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

result = []
for num in numbers:
    if num not in result:
        result.append(num)

print(result)   # [10, 20, 30, 40, 50]

# Alternative (shorter): dict keeps insertion order
# result = list(dict.fromkeys(numbers))

# Q8. Flatten a Nested List
# data = [[10, 20], [30, 40], [50, 60]]
# Flatten into [10, 20, 30, 40, 50, 60] using list operations.

data = [[10, 20], [30, 40], [50, 60]]

flat = []
for sublist in data:
    flat.extend(sublist)

print(flat)   # [10, 20, 30, 40, 50, 60]

# Alternative (list comprehension):
# flat = [x for sublist in data for x in sublist]

# Q9. Extract Data from a Matrix
# matrix = [
#  [10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]
# ]
# Extract main diagonal, secondary diagonal, and middle column;
# calculate the sum of each.

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

n = len(matrix)

main_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
middle_column = [row[n // 2] for row in matrix]

print(main_diagonal, sum(main_diagonal))               # [10, 50, 90] 150
print(secondary_diagonal, sum(secondary_diagonal))     # [30, 50, 70] 150
print(middle_column, sum(middle_column))               # [20, 50, 80] 150

# Q10. List Transformation Challenge
# data = [15, 5, 25, 10, 35, 20, 30]
# Build a list of the three largest unique values ascending,
# then two smallest unique values descending.
# Expected: [25, 30, 35, 10, 5].

data = [15, 5, 25, 10, 35, 20, 30]

unique_sorted = sorted(set(data))   # [5, 10, 15, 20, 25, 30, 35]

three_largest_asc = unique_sorted[-3:]        # [25, 30, 35]
two_smallest_desc = unique_sorted[:2][::-1]   # [10, 5]

result = three_largest_asc + two_smallest_desc

print(result)   # [25, 30, 35, 10, 5]