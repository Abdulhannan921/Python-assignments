# Q21. Unique Values
# numbers = [10, 20, 10, 30, 40, 20, 50]
# Convert to a set and count unique elements.

numbers = [10, 20, 10, 30, 40, 20, 50]

unique_numbers = set(numbers)

print(unique_numbers)        # {10, 20, 30, 40, 50}
print(len(unique_numbers))   # 5

# Q22. Set Operations
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# Find union, intersection, a - b, and symmetric difference.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)   # union: {1, 2, 3, 4, 5, 6, 7, 8}
print(a & b)   # intersection: {4, 5}
print(a - b)   # difference: {1, 2, 3}
print(a ^ b)   # symmetric difference: {1, 2, 3, 6, 7, 8}

# Q23. Add and Remove
# skills = {"Python", "SQL", "AWS"}
# Add Snowflake and Databricks; safely remove AWS.

skills = {"Python", "SQL", "AWS"}

skills.add("Snowflake")
skills.add("Databricks")
skills.discard("AWS")   # discard() does not raise an error if the item is missing

print(skills)   # {'Python', 'SQL', 'Snowflake', 'Databricks'} (order may vary)

# Q24. Common Students
# python_students = {"Ali", "Sara", "Ahmed", "Zain"}
# sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}
# Find students taking both and exactly one course.

python_students = {"Ali", "Sara", "Ahmed", "Zain"}
sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}

both = python_students & sql_students
exactly_one = python_students ^ sql_students

print(both)          # {'Sara', 'Ahmed'}
print(exactly_one)   # {'Ali', 'Zain', 'Hamza', 'Usman'}

# Q25. Subset and Superset
# required_skills = {"Python", "SQL"}
# candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}
# Check required skills are a subset and candidate skills a superset.

required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}

print(required_skills.issubset(candidate_skills))     # True
print(candidate_skills.issuperset(required_skills))   # True

# Q26. Missing Numbers
# numbers = {1, 2, 4, 6, 8, 10}
# Find missing integers from 1 through 10 using set operations.

numbers = {1, 2, 4, 6, 8, 10}

missing = set(range(1, 11)) - numbers

print(missing)   # {3, 5, 7, 9}

# Q27. Three-Set Analysis
# python = {"Ali", "Sara", "Ahmed", "Zain"}
# sql = {"Sara", "Ahmed", "Hamza"}
# aws = {"Ahmed", "Zain", "Hamza"}
# Find students in all three, exactly Python and SQL (not AWS), and at least two.

python = {"Ali", "Sara", "Ahmed", "Zain"}
sql = {"Sara", "Ahmed", "Hamza"}
aws = {"Ahmed", "Zain", "Hamza"}

all_three = python & sql & aws
python_sql_not_aws = (python & sql) - aws
at_least_two = (python & sql) | (python & aws) | (sql & aws)

print(all_three)             # {'Ahmed'}
print(python_sql_not_aws)    # {'Sara'}
print(at_least_two)          # {'Sara', 'Ahmed', 'Zain', 'Hamza'}

# Q28. Transaction Analysis
# day1 = {101, 102, 103, 104}
# day2 = {103, 104, 105, 106}
# day3 = {104, 106, 107, 108}
# Find IDs appearing on all days, exactly one day, and at least two days.

day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
day3 = {104, 106, 107, 108}

all_days = day1 & day2 & day3
exactly_one_day = (day1 ^ day2 ^ day3) - all_days
at_least_two_days = (day1 & day2) | (day1 & day3) | (day2 & day3)

print(all_days)             # {104}
print(exactly_one_day)      # {101, 102, 105, 107, 108}
print(at_least_two_days)    # {103, 104, 106}

# Q29. Access Control
# required_permissions = {"read", "write", "execute"}
# user_permissions = {"read", "write", "delete"}
# Find missing and extra permissions and test full authorization.

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write", "delete"}

missing = required_permissions - user_permissions
extra = user_permissions - required_permissions
fully_authorized = required_permissions.issubset(user_permissions)

print(missing)            # {'execute'}
print(extra)              # {'delete'}
print(fully_authorized)   # False
python
# Q30. Customer Segmentation
# website = {"C1", "C2", "C3", "C4", "C5"}
# mobile = {"C3", "C4", "C6", "C7"}
# store = {"C2", "C4", "C7", "C8"}
# Find customers on exactly one, exactly two, and all three platforms.

website = {"C1", "C2", "C3", "C4", "C5"}
mobile = {"C3", "C4", "C6", "C7"}
store = {"C2", "C4", "C7", "C8"}

all_three = website & mobile & store
at_least_two = (website & mobile) | (website & store) | (mobile & store)

exactly_one = (website ^ mobile ^ store) - all_three
exactly_two = at_least_two - all_three

print(exactly_one)   # {'C1', 'C5', 'C6', 'C8'}
print(exactly_two)   # {'C2', 'C3', 'C7'}
print(all_three)     # {'C4'}