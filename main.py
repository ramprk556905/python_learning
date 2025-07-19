# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# square_num = [x for x in range(25) if x % 2 == 0]
# print(square_num)

# str_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# int_numbers = list(map(int, str_numbers))
# print(int_numbers)
# sqr_numbers = list(map(lambda x: x**2, int_numbers))
# print(sqr_numbers)

# words = ['hello', 'world', 'python', 'is', 'awesome']
# uppercase_words = list(map(lambda x: x.upper(), words))
# print(uppercase_words)

# def get_name(person):
#     return person['name']

# people = [
#     {'name': 'Alice', 'age': 30},               
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Charlie', 'age': 35}  
# ]
# names = list(map(get_name, people)) 
# print(names)

# def get_name(person):
#     return person['name']

# people = [
#      {'name': 'Alice', 'age': 30},               
#      {'name': 'Bob', 'age': 25} 
#]
# name = list(map(get_name,people))
# print(name)

# people = [
#      {'name': 'Alice', 'age': 30},               
#       {'name': 'Bob', 'age': 25},
#       {'name': 'Ransey', 'age': 26} 
# ]

# def even(num):
#     if num%2 == 0:
#         return True
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# def age_25(person):
#     return person['age']>25
    
# print(list(filter(even,lst)))
# print(list(filter(lambda x:x>5,lst)))
# print(list(filter(lambda x:x>5 and x%2 == 0, lst)))
# print(list(filter(age_25,people)))


# with open('source.txt','r') as source_file:
#     content = source_file.read()
    
# with open('destination.txt', 'w') as destination_file:
#     destination_file.write(content)
    
# def count_text_file(file_path):
#     with open(file_path,'r') as file:
#         lines = file.readline()
#         lince_count = len(lines)
#         word_count = sum(len(line.split()) for line in lines)
#         char_count = sum(len(line) for line in lines)
        
#     return lince_count, word_count, char_count

# file_path = 'source.txt'
# lines, words, characters = count_text_file(file_path)
# print(f'Line: {lines}, Words: {words}, Characters:{characters}')


# try:
#     file = open('source.txt', 'r')
#     content = file.read()
#     print(content)
    
# except FileNotFoundError as err:
#     print(err)
# finally:
#     if 'file' in locals() or not file.closed():
#         file.close()
#         print('file close')

# def read_large_file(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#            yield line
           

# file_path = 'source.txt'
# for line in read_large_file(file_path):
#     print(line.strip()) 
    
    
# even_square_numbers = [x**2 for x in range(1, 25) if x%2 == 0]
# odd_square_numbers = [x**2 for x in range(1, 25) if x%2 == 1]

# print(even_square_numbers)
# print(odd_square_numbers)

# def welcome():
#     return("Welcome to the program!")
    
# wel =  welcome
# wel()
# print(wel())

# def main_function(func):
#     def sub_function():
#         print("This is a sub-function inside the main function.")
#         func("Now, it is not working")
#         print("Sub-function executed successfully.")
#     return sub_function()

# # main_function(print)


# @main_function
# def decorated_function(message):
#     print("This is a decorated function.")
#     print("Message:", message)




def shall(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@shall(5)
def greet(name):
    print(f"Hello, {name}!")
    
greet("Ram")