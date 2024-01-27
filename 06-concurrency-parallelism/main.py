import threading
import multiprocessing
import asyncio
import time


# Threading Example
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")

def print_letters():
    for char in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {char}")

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Threading Example: Both threads have finished.")
print()


# Multiprocessing Example
def print_numbers_multiprocessing():
    for i in range(5):
        time.sleep(1)
        print(f"Process 1: {i}")

def print_letters_multiprocessing():
    for char in 'ABCDE':
        time.sleep(1)
        print(f"Process 2: {char}")

# Create two processes
process1 = multiprocessing.Process(target=print_numbers_multiprocessing)
process2 = multiprocessing.Process(target=print_letters_multiprocessing)

# Start the processes
process1.start()
process2.start()

# Wait for both processes to finish
process1.join()
process2.join()

print("Multiprocessing Example: Both processes have finished.")
print()


# Asyncio Example
async def print_numbers_asyncio():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"Async Task 1: {i}")

async def print_letters_asyncio():
    for char in 'ABCDE':
        await asyncio.sleep(1)
        print(f"Async Task 2: {char}")

# Create an event loop
async def main_asyncio():
    task1 = asyncio.create_task(print_numbers_asyncio())
    task2 = asyncio.create_task(print_letters_asyncio())

    await asyncio.gather(task1, task2)

# Run the event loop
asyncio.run(main_asyncio())

print("Asyncio Example: Both asyncio tasks have finished.")
