# Thid stores the total number of cars available
cars = 100
# This stores how much space one car has (as a floating point number)
space_in_a_car =4.0
# This stores how many drivers are available
drivers = 30
# This stores how many passengers need to carpool 
passengers = 90
# This calculates how many cars are not being driven 
cars_not_driven = cars - drivers
# This stores how many cars are actually being driven 
cars_driven = drivers
# This calculates the total carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# This calculates the average number of passengers per car 
average_passengers_per_car = passengers / cars_driven
print("There are",cars,"cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")