import threading
import time


def task1():
    for i in range(1, 6):
        print("Task 1:", i)
        time.sleep(1)


def task2():
    for i in range(1, 6):
        print("Task 2:", i)
        time.sleep(1)


thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All tasks completed.")