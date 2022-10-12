import sys, time

sys.path.insert(0, "../")

import AdroitComs

robot = AdroitComs.AdroitComs(1, channel="can0", bustype="socketcan")
assert robot.reset()

while True:
    print(
        "position: {:<6f} velocity: {:<6f} effort: {:<6f} motor current: {:<6f}".format(
            robot.position[0], robot.velocity[0], robot.effort[0], robot.motor_current[0]
        )
    )
    time.sleep(1 / 50)
