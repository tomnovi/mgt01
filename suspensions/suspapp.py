import numpy as np
import matplotlib.pyplot as plt
from .quartersusp import rocker, rack, wheel
#from utilities import rodrigues
#
 ################################################################################
 ################################################################################
 # TEST CODE
def run():
    print("Hello")

    # Outboard pickup points
    r_uwbf_out = np.array([0.462, 0.484, 0.323])
    r_uwbr_out = np.array([0.462, 0.484, 0.323])
    r_lwbf_out = np.array([0.447, 0.53, 0.138])
    r_lwbr_out = np.array([0.447, 0.53, 0.138])
    r_prod_out = np.array([0.4579, 0.4497, 0.3349])
    r_trod_out = np.array([0.398, 0.53, 0.156])

    # Inboard pickup points
    r_uwbf_in = np.array([0.295, 0.2515, 0.274])
    r_uwbr_in = np.array([0.55, 0.2755, 0.272])
    r_lwbf_in = np.array([0.415, 0.2245, 0.13])
    r_lwbr_in = np.array([0.57, 0.251, 0.144])
    r_prod_in = np.array([0.4579, 0.3196, 0.5609])
    r_trod_in = np.array([0.334, 0.225, 0.14])

    # Define rocker pivot pickup points
    r_rocker1 = np.array([0.44368, 0.23558, 0.56372])
    r_rocker2 = np.array([0.47568, 0.23558, 0.56372])
    r_rocker = np.array([0.4579, 0.23558, 0.56372])

    r_rocker_axis = r_rocker1 - r_rocker2

    # Define wheel center location
    r_wheel_ctr = np.array([0.445, 0.59, 0.229])

    # Define damper pickup points
    r_damper_rocker = np.array([0.4579, 0.2163, 0.6453])
    r_damper_frame = np.array([0.45968, 0.054, 0.5801])

    Rocker = rocker.Rocker(pivot=r_rocker, pushrod=r_prod_out, damper=r_damper_rocker, axis1=r_rocker1, axis2=r_rocker2)
    Rack = rack.Rack(trackrod=r_trod_in)
    Wheel = wheel.Wheel(upper_wishbone=r_uwbf_out, lower_wishbone=r_lwbf_out, trackrod=r_trod_out, pushrod=r_prod_out, wheel_centre=r_wheel_ctr)

    Wheel.wheel_displacement = {"longitudinal": 0, "lateral": 0, "vertical": 0, "camber": 0, "castor": 0, "toe": 0}
    plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.lower_wishbone_position), c='r')
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.upper_wishbone_position), c='r')
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.pushrod_position), c='r')
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.trackrod_position), c='r')

    #ax.plot3D(*zip(Rocker.pivot_position, Rocker.pushrod_position), c='r')
    #ax.plot3D(*zip(Rocker.pivot_position, Rocker.damper_position), c='r')
    #Rocker.rocker_angle = 10 * np.pi / 180
    #plt.scatter(*zip(Rack.trackrod_position))
    #Rack.rack_displacement =  5*1e-03

    Wheel.wheel_displacement = {"longitudinal": 0, "lateral": 0, "vertical": 0, "camber": 45 * np.pi/180, "castor": 0 * np.pi/180, "toe": 0 * np.pi/180}
    Wheel.apply_displacement()
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.lower_wishbone_position), c='b')
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.upper_wishbone_position), c='b')
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.pushrod_position), c='b')
    ax.plot3D(*zip(Wheel.wheel_centre, Wheel.trackrod_position), c='b')

    #for i in range(0,50):
        #Rocker.apply_rotation()
        #ax.plot3D(*zip(Rocker.pivot_position, Rocker.pushrod_position), c='b')
        #ax.plot3D(*zip(Rocker.pivot_position, Rocker.damper_position), c='g')
        #Rack.apply_displacement()
        #plt.scatter(*zip(Rack.trackrod_position))
    plt.show()
