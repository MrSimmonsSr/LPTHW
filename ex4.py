# Assigns value of 100 to variable named cars
cars = 100

# Assigns floating point number 4.0 to variable space_in_a_car
space_in_a_car = 4.0

# Assigns integrer value of 30 to vairable drivers
drivers = 30

# Assigns integrer value of 90 to vairable passengers
passengers = 90

# Subtracts 30 from 100 and assigns result to variable called cars_not_driven
cars_not_driven = cars - drivers

# Takes value of drivers variable and assigns it to variable names cars_driven
cars_driven = drivers

# multiples the number of cars being driven (30) times number of spaces in a car (4.0)
# and assigns that value to a variable called carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# Divides the total number of passengers (90) by the number of cars being driven (30)
# to calculate we need 3 people per car. That number is assigned to variable called
# average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# These lines all just print strings of text with variables inserted inside of them
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")