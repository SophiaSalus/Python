"""Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists."""

# Function to perform bubble sort
def bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] > names[j+1]:
                # Swap if the element found is greater than the next element
                names[j], names[j+1] = names[j+1], names[j]

# Prompt the user to enter five names
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# Apply bubble sort to the names list
bubble_sort(names)

# Reverse the sorted list using the reverse() method
names.reverse()

# Print the sorted and reversed list
print("Sorted list:", names)