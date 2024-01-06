# Design a program that determines the award a person competing in a triathlon will receive.

# Request for input on the total time of completion.
swimming = input("Time of completion for swimming (in minutes): ")
cycling = input("Time of completion for cycling (in minutes): ")
running = input("Time of completion for running (in minutes): ")

# Calculate and display the total time of completion.
total_time = float(swimming) + float(cycling) + float(running)
print(f"You completed the triathlon in {total_time} minutes.")

# Determine and display the type of award the participant will receive based on completion time.
if total_time <= 100:                                            # time range 0-100 minutes
    print("Congratulations! You have been awarded Provincial Colours.")
elif total_time > 100 and total_time <= 105:                     # time range 101-105 minutes
    print ("You have been awarded Provincial Half Colours.")
elif total_time > 105 and total_time <= 110:                     # time range 106-110
    print("You have been awarded Provincial Scroll.")
else:                                                            # more than 111 minutes
    print("Unfortunately you have not achieved an award this time.")