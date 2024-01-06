# Create a program to calculate the value of a cafe's stock
# Create a list for the menu items
# Create a dictionary for the number of each item
# Create another dictionary that contains the prices for each item on 

print("This is a program that calculates the value of a cafe's total stock.\n")
menu = ["coffee", "tea", "cake", "sandwich"]
stock = {
    "coffee": 50,
    "tea": 43,
    "cake": 26,
    "sandwich": 21
}
print(f"A cafe has the following items: {stock}\n")
price = {
    "coffee": 3.00,
    "tea": 2.50,
    "cake": 4.99,
    "sandwich": 5.99
}
print(f"These items are priced as follows: {price}\n")
# Create a counter for the total sum. Each iteration will add to this sum.
# Loop through the menu list and call the corresponding values from dictionaries.
total_stock = 0
for item in menu:
    item_value = (stock[item] * price[item])
    total_stock = total_stock + item_value

print(f"The total value of the cafe's stock is £{total_stock}\n")