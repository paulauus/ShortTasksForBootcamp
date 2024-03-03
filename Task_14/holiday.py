# This is a program to request user input on their holiday destination from a selection
# and calculate the total cost, taking into account hotel, plane and car costs.

# Print the selection of holiday destinations, ask the user to choose one and print out the selection.
print("The holiday destinations for 2024 are:\n A: London\n B: Paris\n C: Rome\n")
destination_dict = {
    "a": "London",
    "b": "Paris",
    "c": "Rome"
}
city_flight = input("Please enter the letter of your destination (A, B or C): ")
city_flight = city_flight.lower()
while city_flight not in destination_dict:
    city_flight = input("Try again. Please enter A, B or C: ")
    city_flight = city_flight.lower()
print(f"You are going to {destination_dict[city_flight]}.\n")

# Ask user input for nights spent at a hotel.
while True:
    try:
        num_nights = input("How many nights are you staying at a hotel? ")
        num_nights = int(num_nights)
        if num_nights < 1:
            print ("Please input a positive number greater than 0.")
            continue
        else:
            break
    except ValueError as e:
        print("That is not a valid input. Try again")
print(f"You are staying {num_nights} nights at the hotel.\n")

# Ask user input for number of car rental days.
while True:
    try:
        rental_days = input("How many days are you renting a car? ")
        rental_days = int(rental_days)
        if rental_days < 1:
            print ("Please input a positive number greater than 0.")
            continue
        else:
            break
    except ValueError as e:
        print("That is not a valid input. Try again")
print(f"You have a car for {rental_days} days.\n")

# Create a funtion for calculating 1) hotel cost, 2) flight cost, 3) car rental cost, 4) total holiday cost.
def hotel_cost(num_nights, city_flight):
    hotel_cost_dict = {
        "a": 250,
        "b": 180,
        "c": 99
    }
    hotel_cost = hotel_cost_dict[city_flight] * num_nights
    return hotel_cost

def plane_cost(city_flight):
    if city_flight == "a":
        plane_cost = 180
    elif city_flight == "b":
        plane_cost = 135
    else:
        plane_cost = 79
    return plane_cost

def car_rental(rental_days, city_flight):
    car_rental_dict = {
        "a": 94,
        "b": 78,
        "c": 55
    }
    car_rental = rental_days * car_rental_dict[city_flight]
    return car_rental

def holiday_cost(hotel_cost, plane_cost, car_rental):
    holiday_cost = (hotel_cost(num_nights, city_flight)) + (plane_cost(city_flight)) + (car_rental(rental_days, city_flight))
    return holiday_cost

# Print out the cost of the holiday in a user friendly way (separately, then the total cost).
print(f"The price of a hotel is £{hotel_cost(num_nights, city_flight)} for {num_nights} night(s),")
print(f"the flight to {destination_dict[city_flight]} is £{plane_cost(city_flight)},")
print(f"and the car rental for {rental_days} day(s) is £{car_rental(rental_days, city_flight)}.")
print(f"The total cost of this holiday is £{holiday_cost(hotel_cost, plane_cost, car_rental)}.")