'''
Running tests with changing parameters.
'''

from main import main


# frame_duration = 800
# frame_duration = 2000

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


def test_boids(frame_duration, debug_state):

    test_id = 0
    
    total_test = len(flock_sizes) * len(perceptions) + len(weights)
    progress_bar(0, total_test)
    
    for flock_size in flock_sizes:
        for perception in perceptions:
            test_id += 1
            main('boid', test_id, frame_duration, flock_size, perception, aC=10, cC=10, sC=10, debug = debug_state)   # Run simulation
            progress_bar(test_id, total_test)

        
    for aC, cC, sC in weights:
        test_id += 1
        main('boid', test_id, frame_duration, flock_sizes[0], perceptions[0], aC=aC, cC=cC, sC=sC, debug = debug_state)   # Run simulation
        progress_bar(test_id, total_test)


def test_sync(frame_duration, debug_state):

    test_id = 0
    
    total_test = len(flock_sizes) * len(perceptions * len(weights_sync))
    progress_bar(0, total_test)

    for flock_size in flock_sizes:
        for perception in perceptions:
            for aC, cC, sC in weights_sync:
                test_id += 1
                
                main('sync', test_id, frame_duration, flock_size, perception, aC=aC, cC=cC, sC=sC, debug = debug_state)   # Run simulation
                progress_bar(test_id, total_test)



def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '■' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


if __name__ == '__main__':
    
    debug_state = False
    
    # print('Boids test...')
    # test_boids(800, debug_state)
    
    print('\nSync test...')
    test_sync(2000, debug_state)
    
