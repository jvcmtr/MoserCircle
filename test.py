import timeit
from circleDivision import solveForPoints, solveForPointsIncremental

def main():
    iterations = 1000
    input = 200
    progressUpdate = 10
    
    print(f"Recursive:")
    time_1 = timeit_with_progress(solveForPoints, [input], iterations, progressUpdate )

    print(f"\nIncremental:")
    time_2 = timeit_with_progress(solveForPointsIncremental, [input], iterations, progressUpdate )



def timeit_with_progress(func, args, total_number, progress_interval, show_total_time = True):
    total_time = 0
    iteration = 0  
    
    while iteration < total_number:
        start_time = timeit.default_timer()
        
        for i in range(min(progress_interval, total_number - iteration)):  
            func(*args)
            iteration += 1
        
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)
        
        print(f"Progress: {progressBar(iteration/total_number, 30)}  ({iteration}/{total_number})         ", end="\r")
    print()
    
    if show_total_time :
        print(f"Total time: {total_time:.6f} seconds")
        
    return total_time


def progressBar(progress, resolution = 20):
    if progress < 0 or progress > 1 :
        return "__ progress-bar-error __"
    
    complete = int(progress * resolution)
    head =  0 if complete == resolution else 1
    incomplete = resolution - complete
    
    bar = f"{'█' * (complete-head)}{ '░║' * head}{' ' * incomplete} {progress * 100:.2f}%"
    
    return bar


if __name__ == '__main__':
    main()
