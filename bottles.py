'''# create a variable and set to 99 
# bottles = 99
# while loop > 1
# print the lines using the variable
# if statement not plural (1 bottle of beer)
# if statement 0 - (no bottles)'''

bottles = 99
while bottles > 0:
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall,")
        print(f"{bottles} bottle of beer")
    else:
        print(f"{bottles} bottles of beer on the wall,")
        print(f"{bottles} bottles of beer")

    bottles -= 1
    if bottles == 0:
        print("No more bottles of beer on the wall!")
    else:
        print("Take one down, pass it around,")
