# variable
cars = 100
# why it is 4.0 not 4 
space_in_a_car = 4.0
# difined variable
drivers = 30
# people amount
passengers = 90
# new variable by operation other variable 
cars_not_driven = cars - drivers
# give variable
cars_driven = drivers
# average_passengers_per_car = car_pool_capacity / passenger NameError: name 'car_pool_capacity' is not defined 
# ps:car_pool_capacity is not variable
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# put variable in ""
print "There are", cars, "cars available."
print "There are only", drivers,"drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "people in each car."
