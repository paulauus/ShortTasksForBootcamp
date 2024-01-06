# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")   # Syntax error: needs parentheses to output
print("\n")     # Syntax error: also missing parentheses, and fixed incorrect indentation in lines 6-15

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"   # Syntax error: assign a value to variable with '='
age = int("24")  # Syntax error: words in a string cannot be cast into integers
print(f"I'm {age} years old.")  # Syntax error: cannot concatenate int into str, can use f-string instead

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now)  # Syntax error: cannot add str and int, both must be int for numeric output

print(f"The total number of years after 3 years: {total_years}") # Syntax error: missing parentheses, and can use f-string to cast int to str

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12   # Syntax error: misspelt variable, 'total' should be 'total_years'
total_months_add = total_months + 6 # Logical error in next line: must add 6 months to get the correct answer
print(f"In 3 years and 6 months, I'll be {total_months_add} months old.")    # Syntax error: add parentheses, use f-string and correct variable

#HINT, 330 months is the correct answer
