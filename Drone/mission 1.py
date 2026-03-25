from pysimverse import Drone
import time

drone = Drone()
drone.connect()

drone.take_off(100)
drone.move_forward(250)
drone.move_right(250)
drone.set_speed(800)
drone.land() 