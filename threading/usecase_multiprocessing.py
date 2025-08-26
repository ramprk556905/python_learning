'''
Real world Example: Multiprocesing for CPU-bound tasks
Scenario: Factorial Calculation
Factorial Calculations, especialy for large numbers,
involve significant computational work. Multiprocess 
can be used to distribute the workload across multiple
CPU cores, improving performance
'''
import multiprocessing
import math,sys,time
#Increase the maximum number of digits for integration conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial of given number

def computational_factorial(number):
    print(f'Computational factorial of{number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == "__main__":
    numbers=[5000,6000,700,8000]
    
    start_time = time.time()
    ##create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(computational_factorial,numbers)
        
    end_time = time.time()
    print(f'Results:{results}')
    print(f'Time taken: {end_time-start_time} seconds')