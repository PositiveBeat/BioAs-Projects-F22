'''
Simple simulation of drone flock behaviour.
'''

import numpy as np
import time
import tkinter as tk

import constants
from gui_setup import BoidFrame, OptionFrame, takeScreenshot
from behaviour import Behaviour
from boid import Boid
from logger import Logger
from plotCSV import plotCSV


def main(test_id, test_nr, frame_duration, flock_size, perception, aC = 0, cC = 0, sC = 0, debug = False):

    root = tk.Tk()
    root.resizable(width = False, height = False)

    boidFrame = BoidFrame()
    optFrame = OptionFrame()  # Option frame disabled

    frame = 0

    # Logging information
    log = Logger(test_id + str(test_nr))
    log.log_to_file('Flock size, perception, aC, cC, sC', *[flock_size, perception, aC, cC, sC])   # Print to log
    avg_align_log = 0
    sync_diff_log = np.zeros(flock_size)
    T = 25


    # SPAWN AND INITIALIZE BOIDS #####################################
    flock = [Boid(perception, boidFrame.board, *np.random.rand(2) * constants.BOARD_SIZE) for _ in range(flock_size)]
    steer = Behaviour(flock)  # Steering vector


    # MAIN LOOP #####################################
    while True:

        if frame_duration == -1:
            # Get slider values for weights if endless mode
            aC = optFrame.board.chk_alignment_value.get() *  optFrame.board.sldr_alignment.get()    # Alignment
            cC = optFrame.board.chk_cohesion_value.get() *  optFrame.board.sldr_cohesion.get()      # Cohesion
            sC = optFrame.board.chk_seperation_value.get() *  optFrame.board.sldr_seperation.get()  # Separation

        # Boid control
        for i, boid in enumerate(flock):

            steer.update(boid, aC, cC, sC)  # Steering vector

            if steer.force.__abs__() > constants.MAX_FORCE:
                steer.force = (steer.force / steer.force.__abs__()) * constants.MAX_FORCE

            boid.update(steer.force)


            # Log sample
            avg_align_log += boid.log_heading_angle
            
            if (frame % T) == 0:
                sync_diff_log[i] = boid.sync
        
        avg_align_log /= flock_size


        frame += 1

        # Main loop breakers
        if frame > frame_duration and frame_duration != -1: break
        if steer.break_flag == True: break


        # Logging
        # if (frame % 50 + 20) == 20:    # Take screenshots every 50 frames, starting from frame 20 (to load gui)
        #     takeScreenshot(boidFrame.board)


        if(test_id == 'boid'):
            log.log_to_file(frame, avg_align_log)   # Print to log
            
        elif (test_id == 'sync'):
            if (frame % T) == 0:
                log.log_to_file(frame, *sync_diff_log)   # Print to log


        # Update GUI
        if debug == True:
            root.update_idletasks()
            root.update()
            time.sleep(0.01)


    root.destroy()



if __name__ == '__main__':
    
    flock_size = 50
    
    test_id = ''
    test_nr = ''
    main(test_id, test_nr, -1, flock_size, constants.PERCEPTION+1000, aC=10, cC=1, sC=1, debug = True)

