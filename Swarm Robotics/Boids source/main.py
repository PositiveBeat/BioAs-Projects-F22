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


def main(frame_duration, flock_size):

    root = tk.Tk()
    root.resizable(width = False, height = False)

    boidFrame = BoidFrame()
    optFrame = OptionFrame()  # Option frame disabled

    frame = 0

    # # Logging information
    # log = Logger(flock_size)
    # dst_target_log = np.zeros(flock_size)


    # SPAWN AND INITIALIZE BOIDS #####################################
    flock = [Boid(boidFrame.board, *np.random.rand(2) * constants.BOARD_SIZE) for _ in range(constants.FLOCK_SIZE)]
    steer = Behaviour(flock)  # Steering vector


    # MAIN LOOP #####################################
    while True:

        # Get slider values for weights
        aC = optFrame.board.chk_alignment_value.get() *  optFrame.board.sldr_alignment.get()    # Alignment
        cC = optFrame.board.chk_cohesion_value.get() *  optFrame.board.sldr_cohesion.get()      # Cohesion
        sC = optFrame.board.chk_seperation_value.get() *  optFrame.board.sldr_seperation.get()  # Separation

        # Boid control
        for boid in flock:

            steer.update(boid, aC, cC, sC)  # Steering vector

            if steer.force.__abs__() > constants.MAX_FORCE:
                steer.force = (steer.force / steer.force.__abs__()) * constants.MAX_FORCE

            boid.update(steer.force)

        frame += 1


        # Main loop breakers
        if frame > frame_duration and frame_duration != -1: break
        if steer.break_flag == True: break


        # Logging
        # if (frame % 50 + 20) == 20:    # Take screenshots every 50 frames, starting from frame 20 (to load gui)
        #     takeScreenshot(boidFrame.board)

        # log.log_to_file(frame, *dst_target_log)   # Print to log


        # Update GUI
        root.update_idletasks()
        root.update()
        time.sleep(0.01)


    root.destroy()



if __name__ == '__main__':
    main(-1, constants.FLOCK_SIZE)
