"""Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps."""

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = []
steps_taken = int(input(f"Enter the number of steps you took on {day}:"))
steps.append(steps_taken)
print("\nSteps recorded for each day:")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")
total_steps = sum(steps)
print(f"\nTotal steps taken during the week: {total_steps} steps")

average_steps = total_steps / len(days)
print(f"Average steps per day: {average_steps:.2f} steps")