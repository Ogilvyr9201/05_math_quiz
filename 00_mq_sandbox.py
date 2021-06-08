# timer be like 
import time

# how does work
# functions
def timer(t):
    while t != 0:
        print("00 : {}".format(t))
        t -= 1
        time.sleep(t)

timer(3)
