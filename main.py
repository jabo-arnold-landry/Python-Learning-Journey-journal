#multithreading: is used to perform task concurrently or at the same time(multitasking), best suited for I/O bound tasks like reading file fetching data from an APIs

import threading # we first import threading modules from python builtin modules

# and to use it we call the thread constructor on it and pass in the function which is will is taking too long to complete and then we call it using the start method to start executing
import time
def bathing(fname, lname):# if I had the parameters like this 
    time.sleep(6)
    print(f"me {fname} {lname} I am bathing")
def brushing():
    time.sleep(2)
    print("I am brushing")
def breakfast():
    time.sleep(4)
    print("I am having breakfast")

preparation1 = threading.Thread(target = bathing, args=('landry','arnold')) # if we have argument in the function we are trying to pass in as the thread we add the second parameter which is args and assign a tuple of arguments we would want to give to the function
preparation1.start()
preparation2 = threading.Thread(target = brushing)
preparation2.start()
preparation3 = threading.Thread(target = breakfast)
preparation3.start()
preparation1.join()
preparation2.join()
preparation3.join()
print("I am good to go now!")