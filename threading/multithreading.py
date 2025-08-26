"""
Multi threading 
When to use Multi threading
I/O-Bound tasks: Task that spend more time waiting for I/O operations(e.g, file operations)"""


import threading
import time

def print_numbers(n):
    for i in range (n):
        time.sleep(2)
        print(f'Number:{i}')
        
def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter:{letter}')
        
t= time.asctime()
print(f'start_time:{t}')
t1= threading.Thread(target=print_numbers,args=(10,))
t2=threading.Thread(target=print_letter)

t1.start()
t2.start()
t1.join()
t2.join()
# print_numbers(10)
# print_letter()
finished_time= time.asctime()
print(f'finished_time:{finished_time}')