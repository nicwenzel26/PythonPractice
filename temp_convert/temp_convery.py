
# Function for converting Farenheight to Celcius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp

# Function for converting from C to F
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

# Function to calculate the force of a mass moving at an acceleration
def get_force(mass, acceleration):
    return mass * acceleration

# Function for calculating the energy
def get_energy(mass, c):
    return mass * (c**2)


f100_in_celsius = f_to_c(100)

c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)
print(f100_in_celsius)


train_force = get_force(22680, 10)
print(train_force)


bomb_energy = get_energy(1, 3*10**8)
print(bomb_energy)
