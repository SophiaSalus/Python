'''Write a Python program that uses if-else statements and:
Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.'''

# Determine if a number is positive
age = int(input("How old are you? "))
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive")

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote!")

if age >= 21:
    print("You are old enough buy alcohol.")
else:
    print("You are not old enough to buy alcohol!")

if age >= 65:
    print("You are old enough for a senior discount.")
else:
    print("You are not old enough for a senior discount!")