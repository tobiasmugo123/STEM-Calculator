import math
from Calculus import derivative
import numpy as np
from constants import gravity_accel_constant

def SpringForce(k,Δ): # Simple Spring Force Function
    return -k * Δ

def velocity(distance,time):
    return distance / time

def velocity_from_distance(v_initial, acceleration, distance):
    math.sqrt(v_initial**2 + 2 * acceleration * distance)

def velocity_from_derivative_at_a_point(f,a):
    return derivative(f,a)

def acceleration_from_velocity(v_initial,v_final,time):
    return (v_final - v_initial ) / time

def acceleration_from_derivative_at_a_point(f,a):
    return derivative(f,a)

def acceleration_from_force(Force,mass):
    return Force/ mass

def distance_const_accel(v_initial, acceleration, time):
    return (v_initial * time) + ((acceleration*time**2) / 2)

def force(mass, acceleration):
    return mass * acceleration

def density(mass,volume):
    return mass / volume

def volume_from_density(mass, density):
    return mass / density

def mass_from_density(density,volume):
    return volume*density

def torque(r, force, angle_deg):
    return r * force * math.sin(math.radians(angle_deg))

def center_of_mass_1D(masses, positions):
    return sum(np.array(masses)*np.array(positions)) / sum(np.array(masses))

def weight(mass):
    return mass * gravity_accel_constant

# SpringForce(2,3)
# Next Steps: Add Sum of Forces = 0 -> Equilibrium function
# print(center_of_mass_1D([1,2,3],[2,4,6]))