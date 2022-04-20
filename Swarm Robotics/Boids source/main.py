"""
Simple simulation of drone flock behaviour.

Author: Nicoline Louise Thomsen
Last update: 31-05-21
"""

import numpy as np
import time
import tkinter as tk

import constants
from gui_setup import BoidFrame, OptionFrame, takeScreenshot
from vector import Vector2D
from behaviour import Behaviour
from boid import Boid
from logger import Logger


def main(test_id, frame_duration, flock_size, perception, aC = 0, cC = 0, sC = 0, debug = False):

    root = tk.Tk()
    root.resizable(width = False, height = False)

    boidFrame = BoidFrame()
    optFrame = OptionFrame()  # Option frame disabled

    frame = 0

    # # Logging information
    log = Logger(test_id)
    log.log_to_file('Flock size, perception, aC, cC, sC', *[flock_size, perception, aC, cC, sC])   # Print to log
    avg_align_log = 0


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
        for boid in flock:

            steer.update(boid, aC, cC, sC)  # Steering vector

            if steer.force.__abs__() > constants.MAX_FORCE:
                steer.force = (steer.force / steer.force.__abs__()) * constants.MAX_FORCE

            boid.update(steer.force)

            avg_align_log += boid.log_heading_angle
        avg_align_log /= flock_size

        frame += 1


        # Main loop breakers
        if frame > frame_duration and frame_duration != -1: break
        if steer.break_flag == True: break


        # Logging
        # if (frame % 50 + 20) == 20:    # Take screenshots every 50 frames, starting from frame 20 (to load gui)
        #     takeScreenshot(boidFrame.board)

        log.log_to_file(frame, avg_align_log)   # Print to log


        # Update GUI
        if debug == True:
            root.update_idletasks()
            root.update()
            time.sleep(0.01)


    root.destroy()



if __name__ == '__main__':
    test_id = -1
    main(test_id, -1, constants.FLOCK_SIZE, constants.PERCEPTION, aC=10, cC=1, sC=1, debug = True)

