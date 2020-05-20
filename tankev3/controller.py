from time import sleep
from random import choice, randint

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, LargeMotor
from ev3dev2.button import Button
from ev3dev2.sensor.lego import InfraredSensor

motors = [LargeMotor(adress) for adress in (OUTPUT_B,OUTPUT_C)]
ir = InfraredSensor()
print('Robot Starting')
btn = Button()

def start()
for m in motors:
    m.run_direct()

def turn()
power = choice([(1,-1),(-1,1)])
t = randint(250, 750)
for m, p in zip(motors, power):
    m.run_timed(speed_sp = p*750, time_sp = t)
    while any(m.state for m in motors):
        sleep(0.1)

def make_move(self, motor, speed):
        def move(state):
            if state:
                motor.on(speed)
            else:
                motor.stop()
        return move