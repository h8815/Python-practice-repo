import threading

def task1(num):
    print(f"Cube of {num} is: {num*num*num}")

def task2(num):
    print(f"Square of {num} is: {num*num}")

if __name__ == "__main__":

    thread1 = threading.Thread(target=task1, args=(10,))
    thread2 = threading.Thread(target=task2, args=(10,))

    # Creating threads
    thread1.start()
    thread2.start()
     
    # wait until the thread is finished
    thread1.join()
    thread2.join()

    print("Done..!")