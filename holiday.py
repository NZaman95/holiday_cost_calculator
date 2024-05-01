# define function for plane_cost with variable city_flight for each city
# use if-elif statement to return prices

def plane_cost(city_flight):
    
    if city_flight == 1:
        return 50
            
    elif city_flight == 2:
        return 75
    
    elif city_flight == 3:
        return 35
    
    elif city_flight == 4:
        return 100


# define function for hotel_cost with variable num_nights for number of nights
def hotel_cost(num_nights):
    price_per_night = 100  # set price per night as variable
    return num_nights*price_per_night # return number of nights multiplied by price


#define function for car_rental with variable for number of rental_days
def car_rental(rental_days):
    cost_per_day = 50  # set cost per day as variable
    return cost_per_day*rental_days # return number of days multiplied by cost 

#define function for holiday cost with previously defined arguments
def holiday_cost (num_nights, city_flight, rental_days):

    hotel = hotel_cost(num_nights) 
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    total_cost = hotel + plane + car

    return total_cost

# print numberered list of destinations ofr user selection
print("Destination List:\n1 - London\n2 - Paris\n3 - Berlin\n4 - Madrid\n")

# Set list for valid choices with while loop
valid_choices = [1,2,3,4]
while True:

    # get user input for city_flight
    city_flight = int(input("Please select one of the available cities by entering the corresponding number: "))

    # if user input is valid, get user input for num_nights and rental_days
    if city_flight in valid_choices:
        num_nights = int(input("Please enter the desired number of nights for your hotel stay: "))
        rental_days = int(input("Please enter how many days you will need a hire car: "))

        #print the statement for cost of holiday, with holiday_cost given
        print("The cost of a holiday for", num_nights, "nights in city", city_flight, "when the car is hired for", rental_days, end = "")
        print(" days is £", holiday_cost (num_nights, city_flight, rental_days))
        break