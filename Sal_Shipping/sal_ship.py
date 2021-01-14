# Function to calculate the cost of ground shipping
def ground_shipping(weight):
    if (weight <= 2) :
        return (weight * 1.5) + 20
    elif (weight <= 6):
        return weight * 3.0 + 20
    elif (weight <= 10):
        return weight * 4.0 + 20
    else:
        return weight * 4.75 + 20

# Function for calculating the cost of drone shipping
def drone_shipping(weight):
    if (weight <= 2):
        return weight * 4.5
    elif (weight <= 6):
        return weight * 9.0
    elif (weight <= 10):
        return weight * 12.0
    else:
        return weight * 14.25

# Cost of premium ground
preem_ground = 125.0

def cheapest_shipping(weight):
    ground = ground_shipping(weight)
    drone = drone_shipping(weight)

    if (ground < drone and ground < preem_ground):
        return ground
    elif (drone < ground and drone < preem_ground):
        return drone
    else:
        return preem_ground

print("Cost of ground shipping for 8.4 pound package: " + str(ground_shipping(8.4)))
print("Cost of drone shipping for a 1.5 pount package: " + str(drone_shipping(1.5)))

print(str(cheapest_shipping(4.8)))
print(str(cheapest_shipping(41.5)))
