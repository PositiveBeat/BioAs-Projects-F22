'''
Simple simulation of drone flock behaviour.
'''

import numpy as np
import time
import tkinter as tk

from behaviour import Behaviour
from boid import Boid
import constants
from gui_setup import BoidFrame, OptionFrame, takeScreenshot
from logger import Logger
from vector import Vector2D



def main(test_id, test_nr, frame_duration, flock_size, perception, aC = 0, cC = 0, sC = 0, debug = False):

    # GUI Setup
    root = tk.Tk()
    root.resizable(width = False, height = False)

    boidFrame = BoidFrame()
    optFrame = OptionFrame()

    frame = 0

    # Logging information
    log = Logger(test_id + str(test_nr))
    log.log_to_file('Flock size, perception, aC, cC, sC', *[flock_size, perception, aC, cC, sC])   # Print to log
    avg_align_log = 0
    norm_vel_sum = Vector2D(*np.zeros(2))   
    sync_diff_log = np.zeros(flock_size)
    T = 25


    # Spawn and initialise boids
    flock = [Boid(perception, boidFrame.board, *np.random.rand(2) * constants.BOARD_SIZE) for _ in range(flock_size)]
    steer = Behaviour(flock)  # Steering vector


    # MAIN LOOP #####################################
    while True:
        
        frame += 1
        # Main loop breakers
        if frame > frame_duration and frame_duration != -1: break
        

        # if frame_duration == -1:
        #     # Get slider values for weights if endless mode
        #     aC = optFrame.board.chk_alignment_value.get() *  optFrame.board.sldr_alignment.get()    # Alignment
        #     cC = optFrame.board.chk_cohesion_value.get() *  optFrame.board.sldr_cohesion.get()      # Cohesion
        #     sC = optFrame.board.chk_seperation_value.get() *  optFrame.board.sldr_seperation.get()  # Separation

        # Reset running sums
        avg_align_log = 0
        norm_vel_sum = Vector2D(*np.zeros(2))

        # Boid control
        for i, boid in enumerate(flock):

            steer.update(boid, aC, cC, sC)  # Steering vector

            if steer.force.__abs__() > constants.MAX_FORCE:
                steer.force = (steer.force / steer.force.__abs__()) * constants.MAX_FORCE

            boid.update(steer.force)


            # Log sample
            avg_align_log += boid.log_heading_angle
            norm_vel_sum += boid.velocity.norm()
            
            if (frame % T) == 0:
                sync_diff_log[i] = boid.sync
        
        avg_align_log /= flock_size
        flocking_state_log = norm_vel_sum.__abs__() / flock_size
        

        # Logging
        if(test_id == 'boid'):
            # log.log_to_file(frame, avg_align_log)   # Print to log (boids test)
            log.log_to_file(frame, flocking_state_log)   # Print to log (boids test)
            
        elif (test_id == 'sync'):
            if (frame % T) == 0:
                log.log_to_file(frame, *sync_diff_log)   # Print to log (sync test)
        
        if (frame % 25 + 25) == 25:    # Take screenshots every 50 frames, starting from frame 20 (to load gui)
            takeScreenshot(boidFrame.board, test_id + str(test_nr), str(frame))


        # Update GUI
        if debug == True:
            root.update_idletasks()
            root.update()
            time.sleep(0.01)


    root.destroy()



if __name__ == '__main__':    
    flock_size = 50
    
    test_id = 'boid'
    test_nr = -1
    main(test_id, test_nr, -1, flock_size, constants.PERCEPTION, aC=6, cC=4, sC=10, debug = True)

