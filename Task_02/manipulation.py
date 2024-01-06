# get input from user
str_manip = input("Type a sentence: ")

#print length of sentence
print("The length of this sentence is " + str(len(str_manip)) + " letters.")

# get last letter from the input string
last_letter = str_manip[-1]     # do not assign a value to a variable through print!
print("The last letter of this sentence is " + last_letter + ".")

# replace every occurrence of an unknown last letter in the sentence
print(str_manip.replace(last_letter, "@"))

# print the last three letters of the sentence
print(str_manip[-3:])

# print the first three and last two letters of the sentence to form a new word
print(str_manip[:3] + str_manip[-2:]) # :3 means the first three letters