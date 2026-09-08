import multiprocessing
import time


def task1():
    for i in range(1, 6):
        print("Process 1:", i)
        time.sleep(1)


def task2():
    for i in range(1, 6):
        print("Process 2:", i)
        time.sleep(1)


if __name__ == "__main__":
    process1 = multiprocessing.Process(target=task1)
    process2 = multiprocessing.Process(target=task2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processes completed.")