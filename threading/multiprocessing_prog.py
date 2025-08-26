"""
Process that run in parallel
CPU bound task-task that are heavy on CPU usage
||el execution"""
import multiprocessing
import time

def square_numers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Square {i}:{i*i} ')
        
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube {i}:{i*i*i} ')
        
if __name__ == "__main__":


    t= time.asctime()
    print(f'start_time:{t}')     
    p1=multiprocessing.Process(target=square_numers)
    p2=multiprocessing.Process(target=cube_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    finished_time= time.asctime()
    print(f'finished_time:{finished_time}')