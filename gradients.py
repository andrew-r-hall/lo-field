# A Biot-Savart simulation for iterative design of transverse gradient coils

import numpy as np
import matplotlib.pyplot

class current_element:

    def __init__(self , x_coord , y_coord , z_coord , current=1 , theta=0):
        self.current = current # amperes
        self.munaught = 4 * np.pi * 10**-7
        self.theta = theta # radians from pointing "up" in grid frame of reference
        self.l = .01 / np.cosine(theta)



class grid:

    def __init__(self, x_resolution=.01 , y_resolution=.01 , z_resolution=.01 , x_fov=.5 , y_fov=.5 , z_fov=.5):
        self.x_resolution = x_resolution # meters
        self.y_resolution = y_resolution
        self.z_resolution = z_resolution

        self.x_fov = x_fov # meters
        self.y_fov = y_fov
        self.z_fov = z_fov

        self.x_dimension = int(x_fov / x_resolution) # array dimensions: unitless
        self.y_dimension = int(y_fov / y_resolution)
        self.z_dimension = int(z_fov / z_resolution)

        self.array = np.zeros(shape=[self.x_dimension,self.y_dimension,self.z_dimension])

def fieldmap(Grid , current_element , coordinates):
    for x in range(grid.x_dimension):
        for y in range(grid.y_dimension):
            for z in range(grid.z_dimension):
                theta = 
                r = np.sqrt( (x - current_element.x_coord)**2 + (y - current_element.y_coord)**2 + (z - current_element.z_coord)**2 )
                B = ( current_element.munaught * current_element.l * np.sin(theta)) / ( 4 * np.pi * np.abs(r)**2)
