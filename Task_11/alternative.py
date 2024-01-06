# Part 1: alternating the case of each character
input_string = "I am learning to code"
print(input_string)

# An existing string cannot be altered. A new string must be created instead.
# Needs a counter to connect numeric indexes to letters of the string.
counter = 0
new_string = ""
for letter in input_string:
    if counter % 2 == 0:
        letter = letter.upper()
    else :
        letter = letter.lower()
    counter += 1
    new_string += letter
print(new_string)

# Part 2: alternating the case of each word
# Must separate string into a list to change the case of each item
# Declare new empty list
string_list = input_string.split()
new_list = []
print(string_list)

for index in range(len(string_list)):
    if index % 2 == 0:
        new_list.append(string_list[index].lower())
    else:
        new_list.append(string_list[index].upper())
final_string = " ".join(new_list)
print(final_string)