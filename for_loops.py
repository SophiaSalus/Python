"""Write a Python program to find and print all numbers divisible by 7 between 1 and 300.
Use a for loop and the modulus operator (%)."""

# Loop through numbers from 1 to 300
for number in range(1, 301):
    # Check if the number is divisible by 7
    if number % 7 == 0:
        print(number)
