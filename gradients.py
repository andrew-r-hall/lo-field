# A Biot-Savart simulation for iterative design of transverse gradient coils

import numpy as np
import matplotlib.pyplot as plt

class current_element:

    def __init__(self , x_coord , y_coord , z_coord , x_len , y_len , z_len , resolution=.01 , current=1 ):
        self.current = current # amperes
        self.munaught = 4 * np.pi * 10**-7
        self.l = np.linalg.norm( [x_len , y_len , z_len] ) # resolution < l < 1.732*resolution
        self.x_len = x_len
        self.y_len = y_len
        self.z_len = z_len
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord



class grid:

    def __init__(self, resolution=.01 , x_fov=.5 , y_fov=.5 , z_fov=.5):
        self.resolution = resolution # meters

        self.x_fov = x_fov # meters
        self.y_fov = y_fov
        self.z_fov = z_fov

        self.x_dimension = int(x_fov / resolution) # array dimensions: unitless
        self.y_dimension = int(y_fov / resolution)
        self.z_dimension = int(z_fov / resolution)

        self.array = np.zeros(shape=[self.x_dimension,self.y_dimension,self.z_dimension])

def fieldmap(Grid , current_element ):
    for x in range(Grid.x_dimension):
        for y in range(Grid.y_dimension):
            for z in range(Grid.z_dimension):
                dx = x - current_element.x_coord
                dy = y - current_element.y_coord
                dz = z - current_element.z_coord
                r = np.linalg.norm([dx,dy,dz])
                theta = np.arccos(np.dot([dx,dy,dz] , [current_element.x_len , current_element.y_len , current_element.z_len]) / ( np.linalg.norm([dx,dy,dz]) * np.linalg.norm([current_element.x_len , current_element.y_len , current_element.z_len])))
                b = ( current_element.munaught * current_element.l * np.sin(theta)) / ( 4 * np.pi * np.abs(r)**2)
                Grid.array[x,y,z] = b
    return(Grid)

def line_example():
    B = []
    for i in range(50):
        print(i)
        e = current_element(i,i,0, .01 , .01 , 0)
        gr = grid()
        gr = fieldmap(gr , e)
        B.append(gr.array)
    B = np.sum(B, axis=0)
    return(B)

def plot_field(B):
    plt.subplot(121)
    plt.imshow(B[:,0,:])
    plt.subplot(122)
    plt.imshow(B[:,:,0])
    plt.show()
    return()
