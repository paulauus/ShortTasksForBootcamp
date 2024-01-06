'''
*
**
***
****
*****
****
***
**
*
'''
# Use a for loop with if-else statements to create the star pattern above
# Create an empty string variable before the loop starts
# The loop needs to iterate 9 times, adding '*' each time
# After the middle line this needs to reverse - take '*' away each iteration

pattern = ""

for index in range(0, 9):
    if index < 5:
        pattern += "*"
        print(pattern)
    elif index > 4:
        print((9 - index) * "*")