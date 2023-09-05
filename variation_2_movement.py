# Group Members:
# A K M Muhitul Islam
# Sergio Martelo
# Syed Ali Hasany
# Mingi Lee

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

# I am assuming that, at the start position Cozmo is facing along the positive y-axis.
# The coordinates list in the cozmo_program function is not limited to two sets of coordinates.
# Only two sets are mentioned to satisfy the assignment requirements.


def turnRight(robot):
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    return


def turnLeft(robot):
    robot.turn_in_place(degrees(90)).wait_for_completed()

    return


def move_straight(robot, unit):
    robot.drive_straight(distance_mm(abs(unit)*100),
                         speed_mmps(200)).wait_for_completed()
    return

# This function moves the robot from (current_x, current_y) to (x,y)


def move(robot, current_x, current_y, x, y):
    # say the movement directions
    x_direction = "right" if x > current_x else "left"
    y_direction = "upward" if y > current_y else "downward"
    robot.say_text(
        f"I will cover {abs(x-current_x)*10} cm horizontally {x_direction} and {abs(y-current_y)*10} cm vertically {y_direction}").wait_for_completed()

    if (x >= current_x):
        # turn horizontal
        turnRight(robot)
        # move horizontal
        move_straight(robot, abs(x-current_x))
        if (y >= current_y):
            # turn vertical
            turnLeft(robot)
            # move vertical
            move_straight(robot, abs(y-current_y))
        else:
            # turn vertical
            turnRight(robot)
            # move vertical
            move_straight(robot, abs(y-current_y))
    else:
        # turn horizontal
        turnLeft(robot)
        # move horizontal
        move_straight(robot, abs(x-current_x))
        if (y >= current_y):
            # turn vertical
            turnRight(robot)
            # move vertical
            move_straight(robot, abs(y-current_y))
        else:
            # turn vertical
            turnLeft(robot)
            # move vertical
            move_straight(robot, abs(y-current_y))
    return


def variation_2(robot, coordinates):

    # set current positions to 0, 0
    current_x, current_y = 0, 0

    for (x, y) in coordinates:
        # make the movement
        move(robot, current_x, current_y, x, y)

        # play animation
        robot.play_anim('anim_dizzy_pickup_01').wait_for_completed()

        # set current positions
        current_x, current_y = x, y
    return


def cozmo_program(robot: cozmo.robot.Robot):
    # set the coordinates here
    coordinates = [(3, 4),
                   (4, 6)]  # you can add more sets coordinates if you want

    variation_2(robot, coordinates)
    return


cozmo.run_program(cozmo_program, use_viewer=False, force_viewer_on_top=False)
