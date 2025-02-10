''' Requirements: Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
    Housing (rent or mortgage)
    Utilities
    Groceries
    Transportation
    Health Care
    Personal Care
    Clothing
    Debt
    Calculate the percentage of the total budget spent in each category.
    Display the results in a user-friendly format using f-strings.
    Ensure your code is well-commented to explain the functionality of different sections.'''

# Get input from user

budget = float(input("Please enter your net monthly income for the budget: "))
housing = float(input("Please enter your housing costs:  "))
utilities = float(input("Please enter your utilities costs:  "))
groceries = float(input("Please enter your grocery costs:  "))
transportation = float(input("Please enter your transportation costs:  "))
healthcare = float(input("Please enter your healthcare costs:  "))
personal_care = float(input("Please enter your personal care costs:  "))
clothing = float(input("Please enter your clothing costs:  "))
debt = float(input("Please enter your debt costs:  "))

# Perform calculations

housing_percent = housing/budget * 100
utilities_percent = utilities/budget * 100
groceries_percent = groceries/budget * 100
transportation_percent = transportation/budget * 100
healthcare_percent = healthcare/budget * 100
personal_care_percent = personal_care/budget * 100
clothing_percent = clothing/budget * 100
debt_percent = debt/budget * 100

# Output

print(f"Your housing is %{housing_percent:.1f} of your monthly budget.")
print(f"Your utilities is %{utilities_percent:.1f} of your monthly budget.")
print(f"Your groceries is %{groceries_percent:.1f} of your monthly budget.")
print(f"Your transportation is %{transportation_percent:.1f} of your monthly budget.")
print(f"Your healthcare is %{healthcare_percent:.1f} of your monthly budget.")
print(f"Your personal_care is %{personal_care_percent:.1f} of your monthly budget.")
print(f"Your healthcare is %{healthcare_percent:.1f} of your monthly budget.")
print(f"Your debt is %{debt_percent:.1f} of your monthly budget.")
