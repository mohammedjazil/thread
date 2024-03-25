import time

start = time.perf_counter()

def do_something():
    print("sleeping 1 second")
    time.sleep(10)
    print("done sleeping")
    
do_something()

finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")