import time

start_time = time.time()
x = 1
counter = 0
while True:
    counter+=1
    if (time.time() - start_time) > x :
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()