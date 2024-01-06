# ask for input of the user's age
age = int(input("How old are you? "))
# order of the if-elif-else statements matters if you don't know how to use logical operators
if (age > 100): # higher than 100
    print("Sorry, you're dead!")
elif (age >= 65): # equal to or higher than 65
    print("Enjoy your retirement!")
elif (age >= 40): # equal to or higher than 40
    print("You're over the hill!")
elif (age == 21): # equal to 21
    print("Congrats on your 21st!")
elif (age < 13): # lower than 12
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")