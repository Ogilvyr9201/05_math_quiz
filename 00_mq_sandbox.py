# time.clock() function
import time

# prints time every second
for i in range(1, 100):
    print("%f" % time.clock())
    time.sleep(1)
