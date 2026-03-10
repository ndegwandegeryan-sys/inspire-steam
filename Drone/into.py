from pysinverse import Drone
import time


drone= Drone()
drone.connect()

drone.take_off()
# distance is in cm

drone.move_forward(360)
time.sleep(1)
drone.move_backward(360)
time.sleep(1)
drone.move_left(80)
time.sleep(1)
drone.move_right(80)
time.sleep(1)

drone.land