'''
Creation and management of boids on the board.

Author: Nicoline Louise Thomsen

Inspiration from tutorial for boids behaviour: 
https://medium.com/better-programming/boids-simulating-birds-flock-behavior-in-python-9fff99375118
'''
import numpy as np
from vector import Vector2D

import constants

DOT_SIZE = constants.DRONE_RADIUS

class Boid():

    def __init__(self, perception, canvas, x, y):
        self.canvas = canvas
        self.colour = constants.COLOUR_BOID

        self.perception = perception
        self.position = Vector2D(x, y)
        
        self.velocity = Vector2D(*(np.random.rand(2) - 0.5) * constants.MAX_SPEED)
        self.acceleration = Vector2D(*np.zeros(2))
        
        self.blink = False
        self.sync = np.random.rand()
        self.blink_duration = 0

        
        self.dot = self.makeDot(init = True)

        # Logging values
        self.log_heading_angle = 0


    def update(self, force):

        self.acceleration += force
        self.velocity += self.acceleration
        self.position += self.velocity
        

        vel = [self.velocity.x, self.velocity.y]
        if np.linalg.norm(vel) > constants.MAX_SPEED:
            self.velocity = self.velocity / np.linalg.norm(vel) * constants.MAX_SPEED

        self.checkOutOfBounds()
        self.canvas.move(self.dot, self.velocity.x, self.velocity.y)

        self.acceleration = Vector2D(*np.zeros(2))
        
        # Blink
        self.blink_visual()
        
        # Save value for logging
        self.log_heading_angle = self.velocity.angle()
        
    
    def blink_visual(self):
        if (self.blink == True):
            self.canvas.itemconfig(self.dot, fill=constants.COLOUR_GREEN)
            self.blink_duration = 10
        
        if (self.blink_duration != 0):
            self.blink_duration -= 1
        else:  
            self.canvas.itemconfig(self.dot, fill=self.colour)
        
            

    def makeDot(self, init):
        if not init:
            self.canvas.delete(self.dot)

        x0 = self.position.x - DOT_SIZE
        y0 = self.position.y - DOT_SIZE
        x1 = self.position.x + DOT_SIZE
        y1 = self.position.y + DOT_SIZE
        return self.canvas.create_oval(x0, y0, x1, y1, fill = self.colour, outline = "")


    def checkOutOfBounds(self):
        if self.position.x > constants.BOARD_SIZE:
            self.position.x = 0
            self.dot = self.makeDot(init = False)

        elif self.position.x < 0:
            self.position.x = constants.BOARD_SIZE
            self.dot = self.makeDot(init = False)

        if self.position.y > constants.BOARD_SIZE:
            self.position.y = 0
            self.dot = self.makeDot(init = False)

        elif self.position.y < 0:
            self.position.y = constants.BOARD_SIZE
            self.dot = self.makeDot(init = False)

