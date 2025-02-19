"""In this exercise, you will practice using logical operators (and, or, not) in Python. Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.
User Input: Start by asking the user to input two distinct integers.
Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
and
or
not
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input."""

a = 10
b = 20
c = 30
e = 40
f = 50
g = 60

# and operator
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")

# or operator
if a > b or a > c:
    print("the or statement is true.")
if b > a or b > c:
    print("the or statement isn't true.")
else:
    print("the or statement is true.")

# not operator
if not a > b:
    print("a is not greater than b")
else:
    print("a is greater than b")

if a > e and e > f:
    print("a is the largest number.")
elif e > a and e > f:
    print("e is the largest number")

if a > f or f > g:
    print("the or statement is true.")
elif not f > g:
    print("the or statement is false.")
