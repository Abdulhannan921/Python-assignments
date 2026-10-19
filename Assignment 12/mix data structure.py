# Q41. Student Performance System
# students = [
#     {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
#     {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
#     {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
# ]
# Calculate each average, top student, tuple of names, and set of unique marks.

students = [
    {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
    {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
    {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
]

averages = {s["name"]: sum(s["marks"]) / len(s["marks"]) for s in students}
top_student = max(averages, key=averages.get)
names = tuple(s["name"] for s in students)
unique_marks = {m for s in students for m in s["marks"]}

print({n: round(a, 2) for n, a in averages.items()})
# {'Ali': 87.67, 'Sara': 92.67, 'Ahmed': 80.67}
print(top_student)    # Sara
print(names)          # ('Ali', 'Sara', 'Ahmed')
print(unique_marks)   # {78, 80, 84, 85, 88, 90, 91, 92, 95}

# Q42. Employee Skills
# employees = {
#     "Ali": {"Python", "SQL", "AWS"},
#     "Sara": {"Python", "Databricks", "SQL"},
#     "Ahmed": {"AWS", "Snowflake", "SQL"}
# }
# Find common skills, Ali-only skills, all team skills,
# and employees meeting Python + SQL requirements.

employees = {
    "Ali": {"Python", "SQL", "AWS"},
    "Sara": {"Python", "Databricks", "SQL"},
    "Ahmed": {"AWS", "Snowflake", "SQL"}
}

common_skills = set.intersection(*employees.values())
ali_only = employees["Ali"] - employees["Sara"] - employees["Ahmed"]
all_skills = set.union(*employees.values())
required = {"Python", "SQL"}
meeting_requirements = [name for name, skills in employees.items() if required.issubset(skills)]

print(common_skills)           # {'SQL'}
print(ali_only)                # set() (Ali ki koi unique skill nahi)
print(all_skills)              # {'Python', 'SQL', 'AWS', 'Databricks', 'Snowflake'}
print(meeting_requirements)    # ['Ali', 'Sara']

# Q43. Sales Data
# sales = [
#     ("Laptop", 120000, 2),
#     ("Mouse", 1500, 5),
#     ("Keyboard", 3500, 3)
# ]
# Calculate revenue, top-revenue product, name-to-revenue dictionary,
# and set of prices.

sales = [
    ("Laptop", 120000, 2),
    ("Mouse", 1500, 5),
    ("Keyboard", 3500, 3)
]

revenue = sum(price * qty for name, price, qty in sales)
name_to_revenue = {name: price * qty for name, price, qty in sales}
top_product = max(name_to_revenue, key=name_to_revenue.get)
prices = {price for name, price, qty in sales}

print(revenue)           # 258000
print(top_product)       # Laptop
print(name_to_revenue)   # {'Laptop': 240000, 'Mouse': 7500, 'Keyboard': 10500}
print(prices)            # {120000, 1500, 3500}

# Q44. Customer Orders
# customers = {
#     "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
#     "C102": {"name": "Sara", "orders": [3000, 4500]},
#     "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
# }
# Calculate spending per customer, top customer,
# and tuple of totals in customer ID order.

customers = {
    "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    "C102": {"name": "Sara", "orders": [3000, 4500]},
    "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}

spending = {c["name"]: sum(c["orders"]) for c in customers.values()}
top_customer = max(spending, key=spending.get)
totals_tuple = tuple(sum(customers[cid]["orders"]) for cid in sorted(customers))

print(spending)        # {'Ali': 5500, 'Sara': 7500, 'Ahmed': 4500}
print(top_customer)    # Sara
print(totals_tuple)    # (5500, 7500, 4500)

# Q45. Course Enrollment
# courses = {
#     "Python": {"Ali", "Sara", "Ahmed"},
#     "SQL": {"Sara", "Ahmed", "Zain"},
#     "AWS": {"Ali", "Ahmed", "Zain"}
# }
# Find students in exactly two, all three, and exactly one course;
# count unique students.

from collections import Counter

courses = {
    "Python": {"Ali", "Sara", "Ahmed"},
    "SQL": {"Sara", "Ahmed", "Zain"},
    "AWS": {"Ali", "Ahmed", "Zain"}
}

# Count in how many courses each student appears
counts = Counter(student for students in courses.values() for student in students)

exactly_two = {s for s, c in counts.items() if c == 2}
all_three = {s for s, c in counts.items() if c == 3}
exactly_one = {s for s, c in counts.items() if c == 1}
unique_count = len(counts)

print(exactly_two)    # {'Ali', 'Sara', 'Zain'}
print(all_three)      # {'Ahmed'}
print(exactly_one)    # set()
print(unique_count)   # 4

# Q46. E-Commerce Transactions
# transactions = [
#     {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
#     {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
#     {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
# ]
# Calculate total revenue, Ali spending, largest transaction,
# and unique product names.

transactions = [
    {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
    {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
    {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
]

# Total of each transaction
txn_totals = {t["id"]: sum(p * q for n, p, q in t["items"]) for t in transactions}

total_revenue = sum(txn_totals.values())
ali_spending = sum(
    txn_totals[t["id"]] for t in transactions if t["customer"] == "Ali"
)
largest_txn = max(txn_totals, key=txn_totals.get)
unique_products = {n for t in transactions for n, p, q in t["items"]}

print(txn_totals)         # {101: 123000, 102: 8500, 103: 45000}
print(total_revenue)      # 176500
print(ali_spending)       # 168000
print(largest_txn, txn_totals[largest_txn])   # 101 123000
print(unique_products)    # {'Laptop', 'Mouse', 'Keyboard', 'Monitor'}

# Q47. Pipeline Monitoring
# pipelines = {
#     "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
#     "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
#     "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
# }
# Find total processed records, failed pipelines, largest pipeline total,
# and average records per run for each.

pipelines = {
    "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}

pipeline_totals = {name: sum(p["records"]) for name, p in pipelines.items()}
total_records = sum(pipeline_totals.values())
failed = [name for name, p in pipelines.items() if p["status"] == "failed"]
largest_pipeline = max(pipeline_totals, key=pipeline_totals.get)
avg_per_run = {name: sum(p["records"]) / len(p["records"]) for name, p in pipelines.items()}

print(total_records)       # 8900
print(failed)              # ['pipeline_2']
print(largest_pipeline, pipeline_totals[largest_pipeline])   # pipeline_3 4800
print({n: round(a, 2) for n, a in avg_per_run.items()})
# {'pipeline_1': 1100.0, 'pipeline_2': 266.67, 'pipeline_3': 1600.0}

# Q48. Banking Transactions
# accounts = {
#     "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
#     "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
#     "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
# }
# Assuming zero starting balances, calculate final balances, highest balance,
# total withdrawals, and largest single deposit.

accounts = {
    "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}

balances = {acc: sum(d["transactions"]) for acc, d in accounts.items()}
highest_account = max(balances, key=balances.get)
total_withdrawals = abs(sum(t for d in accounts.values() for t in d["transactions"] if t < 0))
largest_deposit = max(t for d in accounts.values() for t in d["transactions"] if t > 0)

print(balances)             # {'A101': 5000, 'A102': 5000, 'A103': 8000}
print(highest_account, balances[highest_account])   # A103 8000
print(total_withdrawals)    # 9500
print(largest_deposit)      # 10000

# Q49. Product Recommendations
# users = {
#     "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
#     "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
#     "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
# }
# Find products bought by at least two users, Ali wishlist minus purchases,
# shared wishlist products, and all products.

from collections import Counter

users = {
    "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
    "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
    "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
}

purchase_counts = Counter(p for u in users.values() for p in u["purchased"])
bought_by_two_plus = {p for p, c in purchase_counts.items() if c >= 2}

ali_wishlist_not_bought = users["Ali"]["wishlist"] - users["Ali"]["purchased"]

wishlist_counts = Counter(p for u in users.values() for p in u["wishlist"])
shared_wishlist = {p for p, c in wishlist_counts.items() if c >= 2}

all_products = set.union(*(u["purchased"] | u["wishlist"] for u in users.values()))

print(bought_by_two_plus)         # {'Laptop', 'Keyboard'}
print(ali_wishlist_not_bought)    # {'Keyboard', 'Monitor'}
print(shared_wishlist)            # {'Mouse', 'Monitor'}
print(all_products)               # {'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'}

# Q50. Final Company Analysis
# company = {
#     "departments": {
#         "Engineering": {
#             "employees": [
#                 ("Ali", 120000, {"Python", "AWS", "SQL"}),
#                 ("Sara", 150000, {"Python", "Databricks", "SQL"})
#             ],
#             "budget": 500000
#         },
#         "Analytics": {
#             "employees": [
#                 ("Ahmed", 100000, {"SQL", "Power BI"}),
#                 ("Zain", 130000, {"Python", "SQL", "Tableau"})
#             ],
#             "budget": 400000
#         }
#     }
# }
# 1. Payroll per department.
# 2. Company payroll.
# 3. Highest-paid employee.
# 4. Skills shared by all.
# 5. Engineering-only skills.
# 6. Remaining budget per department.
# 7. Department with higher average salary.
# 8. Name-to-salary dictionary.
# 9. All unique skills.
# 10. Is combined budget sufficient?

company = {
    "departments": {
        "Engineering": {
            "employees": [
                ("Ali", 120000, {"Python", "AWS", "SQL"}),
                ("Sara", 150000, {"Python", "Databricks", "SQL"})
            ],
            "budget": 500000
        },
        "Analytics": {
            "employees": [
                ("Ahmed", 100000, {"SQL", "Power BI"}),
                ("Zain", 130000, {"Python", "SQL", "Tableau"})
            ],
            "budget": 400000
        }
    }
}

depts = company["departments"]
all_employees = [e for d in depts.values() for e in d["employees"]]

# 1. Payroll per department
payroll = {name: sum(e[1] for e in d["employees"]) for name, d in depts.items()}
print(payroll)   # {'Engineering': 270000, 'Analytics': 230000}

# 2. Company payroll
company_payroll = sum(payroll.values())
print(company_payroll)   # 500000

# 3. Highest-paid employee
highest_paid = max(all_employees, key=lambda e: e[1])[0]
print(highest_paid)   # Sara

# 4. Skills shared by all employees
shared_skills = set.intersection(*(e[2] for e in all_employees))
print(shared_skills)   # {'SQL'}

# 5. Engineering-only skills
eng_skills = set.union(*(e[2] for e in depts["Engineering"]["employees"]))
ana_skills = set.union(*(e[2] for e in depts["Analytics"]["employees"]))
engineering_only = eng_skills - ana_skills
print(engineering_only)   # {'AWS', 'Databricks'}

# 6. Remaining budget per department
remaining_budget = {name: d["budget"] - payroll[name] for name, d in depts.items()}
print(remaining_budget)   # {'Engineering': 230000, 'Analytics': 170000}

# 7. Department with higher average salary
avg_salary = {name: payroll[name] / len(d["employees"]) for name, d in depts.items()}
higher_avg_dept = max(avg_salary, key=avg_salary.get)
print(avg_salary)         # {'Engineering': 135000.0, 'Analytics': 115000.0}
print(higher_avg_dept)    # Engineering

# 8. Name-to-salary dictionary
name_to_salary = {e[0]: e[1] for e in all_employees}
print(name_to_salary)   # {'Ali': 120000, 'Sara': 150000, 'Ahmed': 100000, 'Zain': 130000}

# 9. All unique skills
all_skills = set.union(*(e[2] for e in all_employees))
print(all_skills)   # {'Python', 'AWS', 'SQL', 'Databricks', 'Power BI', 'Tableau'}

# 10. Is combined budget sufficient?
combined_budget = sum(d["budget"] for d in depts.values())
is_sufficient = combined_budget >= company_payroll
print(combined_budget)   # 900000
print(is_sufficient)     # True