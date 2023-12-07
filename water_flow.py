#Moroni Bamvakiades Ramos
#11/08/2023
#This code snippet defines a function that calculates the pressure loss from a pipe.
#Python documentation, ChatGPT, Codeium


#This code snippet defines a function that calculates the height of a water column in a tower. 
# It takes two parameters: tower_height and tank_height. 
# The height of the water column is calculated by adding the tower_height to three-quarters of the tank_height. 
# The calculated height is then returned as the result.
def mbr_water_column_height(tower_height, tank_height):
    height_of_water_column = tower_height + (3 * tank_height / 4)
    
    return height_of_water_column


#This code calculates the pressure exerted by a column of water given its height. 
# It uses the formula: pressure = density_of_water * acceleration_due_to_gravity * height. 
# The density of water is assumed to be 998.2 kg/m^3 and the acceleration due to gravity is assumed to be 9.80665 m/s^2. 
# The function takes the height of the water column as input and returns the calculated pressure.
def mbr_pressure_gain_from_water_height(height):
    
    density_of_water = 998.2  # Density of water in kg/m^3
    acceleration_due_to_gravity = 9.80665  # Acceleration due to gravity in m/s^2

    pressure = density_of_water * acceleration_due_to_gravity * height
    return pressure
    
    
#This code snippet defines a function called mbr_pressure_loss_from_pipe that calculates the pressure loss in a pipe using the given parameters. 
#It uses the Darcy-Weisbach equation to calculate the pressure loss based on the pipe diameter, length, friction factor, and fluid velocity. 
#The calculated pressure loss is then returned by the function.    
def mbr_pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
    P = - friction_factor * pipe_length * 998.2 * fluid_velocity ** 2 / 2000 * pipe_diameter
    
    return P