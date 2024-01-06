# Write a program that calculates the area of a rectangle
# Ask user for input on the length and width of the two sides
# Print the answer in a sentence

print("This is a program to calculate the area of a rectangle.")

length = input("What is the length of the rectangle (in centimetres)? ")
width = input("What is the width of the rectangle (in centimetres)? ")

area = (float(length) * float(width)) / 2   # Logical error: the formula for the area of a rectangle is incorrect
area = round(area, 2)

print(f"The area of the rectangle is {area} centimetres.")  # The program is still executed despite the logical error