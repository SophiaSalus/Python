"""Create a Python script to track heart rate readings and calculate the average heart rate.
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it."""

# Define the time slots for heart rate tracking
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

# Collect heart rate readings from the user
for slot in time_slots:
    while True:
        try:
            heart_rate = int(input(f"Enter your heart rate (BPM) for {slot}: "))
            if heart_rate <= 0:
                raise ValueError("Heart rate must be a positive integer.")
            heart_rates.append([slot, heart_rate])
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

# Calculate the average heart rate
average_heart_rate = sum(hr[1] for hr in heart_rates) / len(heart_rates)

# Display the results
print("\nHeart Rate Readings:")
for slot, rate in heart_rates:
    print(f"{slot}: {rate} BPM")

print(f"\nAverage Heart Rate: {average_heart_rate:.2f} BPM")