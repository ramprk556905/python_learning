from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f'Number:{number}'

numbers=[1,2,3,4,5,5,6,767,7,5,4,44,3,33]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)
    
for result in results:
    print(result)