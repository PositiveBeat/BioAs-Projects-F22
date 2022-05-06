'''
Running tests with changing parameters.
'''

from main import main


frame_duration = 800

# Parameters to test
flock_sizes = [25, 100]

perceptions = [200, 1000]

weights = [ [0, 0, 0],
            [10, 10, 10],
            [20, 5, 5],
            [5, 20, 5],
            [5, 5, 20] ]

weights_sync = [ [0, 0, 0],
                 [10, 10, 10] ]


def test_boids():

    test_id = 0
    debug_state = True
    
    for flock_size in flock_sizes:
        for perception in perceptions:
            test_id += 1
            print("Test: ", test_id)
            main('boid', test_id, frame_duration, flock_size, perception, aC=10, cC=10, sC=10, debug = debug_state)   # Run simulation
    
    print('Changing weights...')
    
    for aC, cC, sC in weights:
        test_id += 1
        print("Test: ", test_id)
        main('boid', test_id, frame_duration, flock_sizes[0], perceptions[0], aC=aC, cC=cC, sC=sC, debug = debug_state)   # Run simulation


def test_sync():

    test_id = 0

    for flock_size in flock_sizes:
        for perception in perceptions:
            for aC, cC, sC in weights_sync:
                test_id += 1
                print("Test: ", test_id)

                main('sync', test_id, frame_duration, flock_size, perception, aC=aC, cC=cC, sC=sC)   # Run simulation



if __name__ == '__main__':
    
    print('Boids test...')
    test_boids()
    
    print('\nSync test...')
    test_sync()
    
    print("All done!")
