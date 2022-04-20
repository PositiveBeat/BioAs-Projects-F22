'''
Running tests with changing parameters.

Author: Nicoline Louise Thomsen
'''

from main import main


frame_duration = 800

# Parameters to test
flock_sizes = [5, 10, 25, 50, 100]

perceptions = [1000, 500, 250, 100]

weights = [ [20, 5, 5],
            [5, 20, 5],
            [5, 5, 20] ]




def test():

    test_id = 0

    for flock_size in flock_sizes:
        for perception in perceptions:
            for aC, cC, sC in weights:
                test_id += 1
                print("Test: ", test_id)

                main(test_id, frame_duration, flock_size, perception, aC=aC, cC=cC, sC=sC)   # Run simulation


if __name__ == '__main__':
    test()
