#Q1>Write a code to read the contents of a file in Python?
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

#Q2>Write a code to write to a file in Python?
with open('file.txt', 'w') as file:
    file.write("Hello, this is a new content.")

#Q3>Write a code to append to a file in Python?
with open('file.txt', 'a') as file:
    file.write("\nThis is an appended line.")

#Q4>Write a code to read a binary file in Python?
with open('file.bin', 'rb') as file:
    content = file.read()
    print(content)
    
#Q5> What happens if we don't use `with` keyword with `open` in python?
#ANS >If you don't use the with statement to open a file, the file will not be automatically closed after the block of code is executed.

#Q6> Explain the concept of buffering in file handling and how it helps in improving read and write operations?
#ANS >>
# Buffering is the process of reading and writing data to a buffer (a temporary area in memory) instead of performing I/O operations directly on the file. It helps improve performance because reading or writing large chunks of data in memory is faster than doing it one byte at a time




#Q7>Describe the steps involved in implementing buffered file handling in a programming language of your
#choice?
#Ans>
# Open file >> Read or write data using buffer>> close the fiel to ensure all buffered data is written ou and resourse are released

#Q8>Write a Python function to read a text file using buffered reading and return its contents?
def read_file_buffered(file_path):
    with open(file_path, 'r', buffering=1) as file:  
        content = file.read()
    return content

#Q9>What are the advantages of using buffered reading over direct file reading in Python?
#Ans > Performation and efficiency
# Q 10>.Write a Python code snippet to append content to a file using buffered writing?
def append_to_file_buffered(file_path, content):
    with open(file_path, 'a', buffering=1) as file:  
        file.write(content)


#Q11>Write a Python function that demonstrates the use of close() method on a file?
def close_file_example(file_path):
    file = open(file_path, 'w')
    file.write("Some content.")
    file.close()  


#Q12 Create a Python function to showcase the detach() method on a file object?
def detach_example(file_path):
    with open(file_path, 'w') as file:
        writer = file.detach() 



#Q13> Write a Python function to demonstrate the use of the seek() method to change the file position?
def seek_example(file_path):
    with open(file_path, 'r') as file:
        file.seek(5)  
        content = file.read(10)  
    print(content)

#Q14> Create a Python function to return the file descriptor (integer number) of a file using the fileno() method?
def get_file_descriptor(file_path):
    with open(file_path, 'r') as file:
        fd = file.fileno()  
    return fd

#Q15> Write a Python function to return the current position of the file's object using the tell() method?
def get_file_position(file_path):
    with open(file_path, 'r') as file:
        position = file.tell()  # Returns the current file position
    return position

#Q16> Create a Python program that logs a message to a file using the logging module?
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info('This is an info message')

#Q17> Explain the importance of logging levels in Python's logging module?

#Q18>Create a Python program that uses the debugger to find the value of a variable inside a loop?
import pdb

def find_variable_in_loop():
    for i in range(5):
        pdb.set_trace()  
        print(i)

find_variable_in_loop()

#Q19>Create a Python program that demonstrates setting breakpoints and inspecting variables using the
#debugge?
import pdb

def debug_example():
    a = 10
    b = 20
    pdb.set_trace() 
    result = a + b
    print(result)

debug_example()

#Q20> Create a Python program that uses the debugger to trace a recursive function?
import pdb

def factorial(n):
    pdb.set_trace() 
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

#Q21>Write a try-except block to handle a ZeroDivisionError?
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

#Q22>How does the else block work with try-except?
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful, result is:", result)

#Q23>Implement a try-except-else block to open and read a file?
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File content:", content)

#Q24>What is the purpose of the finally block in exception handling?
#Ans>
# The finally block is used for cleanup actions that need to be executed no matter whether an exception is raised or not. It ensures that necessary final actions are performed, such as closing files or releasing resources.

#Q25>Write a try-except-finally block to handle a ValueError?
try:
    value = int("abc")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed.")

#Q26>How multiple except blocks work in Python?
try:
    num = int("abc")
    result = 10 / 0
except ValueError:
    print("A ValueError occurred.")
except ZeroDivisionError:
    print("A ZeroDivisionError occurred.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#Q27> What is a custom exception in Python?
#ANS>
# A custom exception is a user-defined exception class derived from Python's Exception class. It allows you to create meaningful exception types tailored to your application's needs

#Q28> Create a custom exception class with a message?
class NegativeValueError(Exception):
    def __init__(self, message="Value cannot be negative"):
        self.message = message
        super().__init__(self.message)

#Q29> Write a code to raise a custom exception in Python?
def check_positive(value):
    if value < 0:
        raise NegativeValueError("Provided value is negative!")

try:
    check_positive(-5)
except NegativeValueError as e:
    print(e)

#Q30>Write a function that raises a custom exception when a value is negative'
def validate_positive(value):
    if value < 0:
        raise NegativeValueError(f"Invalid input: {value} is negative.")
    return value

try:
    validate_positive(-10)
except NegativeValueError as e:
    print(e)


#Q31>What is the role of try, except, else, and finally in handling exceptions'
#Ans>>
# try: Code that might raise an exception is placed here.
#except: Handles exceptions raised in the try block.
#else: Executes if no exception occurs in the try block.
#finally: Executes regardless of whether an exception occurred or not, often used for cleanup.
 
#Q32> How can custom exceptions improve code readability and maintainability,
#ANS>
#Readability: Custom exceptions convey specific error details, making it clear what went wrong.
#Maintainability: Errors are easier to debug and handle because custom exceptions classify different error conditions.

#Q33>What is multithreading?
#ANS>Multithreading allows multiple threads (lightweight sub-processes) to run concurrently within a single process. It improves performance for I/O-bound tasks.


#Q34> Create a thread in Python?
import threading

def print_numbers():
    for i in range(5):
        print(i)

# Create and start a thread
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()


#Q35>What is the Global Interpreter Lock (GIL) in Python?
#The Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecode at a time, even in a multi-threaded program. This simplifies memory management but can limit performance in CPU-bound tasks

#Q36>Implement a simple multithreading example in Python?
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

#Q37> What is the purpose of the `join()` method in threading?
#Ans>
#The join() method ensures that the main program waits until the thread completes before continuing execution.
#Q38> Describe a scenario where multithreading would be beneficial in Python'
#ANS>
#Reading/writing files simultaneously.
#Performing web scraping with multiple requests.
#Downloading multiple files concurrently

#Q39>What is multiprocessing in Python?
#Ans>Multiprocessing creates separate processes with their own memory space. It's beneficial for CPU-bound tasks where the GIL limits multithreading.

#Q40> How is multiprocessing different from multithreading in Python?

#Q41> Create a process using the multiprocessing module in Python?
import multiprocessing

def worker():
    print("Worker process running")

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()

#Q42>Explain the concept of Pool in the multiprocessing module?
#Ans>
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)  # Output: [1, 4, 9, 16, 25]

#Q43>Explain inter-process communication in multiprocessing.
from multiprocessing import Process, Queue

def producer(queue):
    queue.put("Data from producer")

def consumer(queue):
    data = queue.get()
    print(f"Consumer received: {data}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
