# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"   # Syntax error: strings must be in quotation marks
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."  # Syntax error: needs f to create f-string
# Logical error in line 9: number_of_teeth and animal_type must be switched for the sentence to make sense
print(full_spec)    # Syntax error: missing parentheses to print