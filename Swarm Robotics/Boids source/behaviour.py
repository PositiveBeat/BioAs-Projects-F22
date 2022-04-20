'''
Rulebase for behaviour of drones

Author: Nicoline Louise Thomsen

Inspiration from tutorial for boids behaviour: 
https://medium.com/better-programming/drones-simulating-birds-flock-behavior-in-python-9fff99375118
The code have been changed to use the datastructure of the Vector2D class, changed the gui package, and other modifications to improve the behaviour for use on drone platforms.
'''

import math
import numpy as np
from vector import Vector2D

import constants

FOV = 1/6
MARGIN = 20
STOP_FORCE = 0.5
MAX_DRONE_PR_TREE = 3
TIME_TO_ANALYZE = 1000

class Behaviour():

    def __init__(self, flock):
        self.drone = []
        self.percieved_flockmates = []
        self.force = 0

        self.break_flag = False
        
        self.flock = flock


    def update(self, drone, aC, cC, sC):
        self.drone = drone
        self.percieved_flockmates.clear()
        
        for flockmate in self.flock:
            if (0 < flockmate.position.distance_to(self.drone.position) < self.drone.perception):
                self.percieved_flockmates.append(flockmate)

        # Apply behaviours
        self.force = aC * self.alignment() + cC * self.cohesion() + sC * self.separation()
        


############################# BEHAVIOURS #############################

    def alignment(self):
        steering = Vector2D(*np.zeros(2))
        avg_vec = Vector2D(*np.zeros(2))
        total = 0

        for flockmate in self.percieved_flockmates:
            avg_vec += flockmate.velocity
            total += 1
        
        if total > 0:
            avg_vec /= total
            steering = avg_vec - self.drone.velocity

        if steering.__abs__() > constants.MAX_FORCE:
            steering = steering.norm() * constants.MAX_FORCE

        return steering


    def cohesion(self):
        steering = Vector2D(*np.zeros(2))
        center_of_mass = Vector2D(*np.zeros(2))
        total = 0

        for flockmate in self.percieved_flockmates:
            center_of_mass += flockmate.position
            total += 1

        if total > 0:
            center_of_mass /= total
            vec_to_com = center_of_mass - self.drone.position
            steering = vec_to_com - self.drone.velocity

        if steering.__abs__() > constants.MAX_FORCE:
            steering = steering.norm() * constants.MAX_FORCE

        return steering


    def separation(self):
        steering = Vector2D(*np.zeros(2))
        avg_vector = Vector2D(*np.zeros(2))
        total = 0
        
        for flockmate in self.percieved_flockmates:
            distance = flockmate.position.distance_to(self.drone.position)
            
            if distance < (self.drone.perception / 4):
                diff = self.drone.position - flockmate.position

                avg_vector += diff
                total += 1

        if total > 0:
            avg_vector /= total
            
            if avg_vector.__abs__() > 0:
                steering = avg_vector - self.drone.velocity

        return steering.norm() * constants.MAX_FORCE
