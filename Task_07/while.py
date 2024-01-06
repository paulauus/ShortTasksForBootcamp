# Must import statistics at the start to use statistics.mean()
# Create a list !before! the loop starts, and add the inputs to the list
# Use a while loop to enable continuous input of numbers
# Include an if statement to break the loop when user enters -1
# Error handling: use try-except to continue the loop if the user doesn't enter numbers
# Remove -1 from the list
# Calculate and display appropriately the average of the entered numbers

import statistics
numbers_list = []

while True:
    try:
        num = int(input("Please enter a number: "))
        numbers_list.append(num)
        if num == -1:
            break

    except ValueError:
        print("Invalid input. Try again.")

del numbers_list[-1]
print(f"You have entered the numbers {numbers_list}.")
average_list = statistics.mean(numbers_list)
print(f"The average of the numbers entered (excluding -1) is {average_list}.")