'''
Name: Jiawen Cai
Class: CS 5001.17350.202410
This is for #3 Programming in HW3:Booleans, Decision Making & Repetition

'''

import turtle
import math

# Initialize the screen
turtle.Screen().bgpic("shape_window.png")
screen = turtle.Screen()
screen.setup(975, 630)

# Create a circle object
circle_pen = turtle.Turtle()
circle_pen.hideturtle()

# Initialize the radius and circle coordinates
radius = 80
circle_x, circle_y = 0, 0

def circle_drawer(x, y):
    '''
    Function -- circle_drawer
    Draws a green circle with a specified center.

    Parameters:
    x (float) -- x-coordinate of the center
    y (float) -- y-coordinate of the center
    '''
    circle_pen.penup()
    # Adjust y coordinate to make the click is the center
    circle_pen.goto(x, y - radius) 
    circle_pen.pencolor("green")
    circle_pen.pendown()
    circle_pen.circle(radius)
    circle_pen.penup()

circle_drawer(0,0)

def distance(point1, point2):
    return math.sqrt(\
        (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def click_shaper(x, y):
    '''
    Handle interactions with a turtle graphics window under different clicks.

    Parameters:
    x (float): The x-coordinate of the mouse click.
    y (float): The y-coordinate of the mouse click.

    This function checks if the mouse click is within a certain distance of a previously drawn circle
    on the turtle graphics window. If it is, the existing circle is cleared, and a new one is drawn
    centered at the new mouse click coordinates (x, y).
    '''


    global circle_x, circle_y  # Declare circle_x and circle_y as global variables

    dist = distance((x, y), (circle_x, circle_y))

    if turtle.isvisible() and dist <= radius:
        circle_pen.clear()
        if not circle_pen.isvisible():
            circle_x, circle_y = x, y
            circle_drawer(x, y)


# Register the function to handle mouse clicks
screen.onscreenclick(click_shaper)

# Keep the turtle graphics window open
turtle.mainloop()
 
