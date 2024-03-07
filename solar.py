import turtle           # Imports library that allows user to alter a turtle. A turtle is something that has a position and a direction, and can draw lines
from turtle import *    # Imports functions from the turtle library that allow user to alter the turtle
from tkinter import *
from math import *

# The gravitational constant G
G = 6.6741e-11

# The Astronomical Unit = distance from earth to the sun [meters]
AU = 149600000000
SCALE = 75.0 / AU       # Scale 1 AU to 30 pixels

# Class definitions: planet
class planet(Turtle):   # This function defines the parameters for each planets

    # Initialize planet name, location, velocity
    vx = vy = 0.0
    xloc = yloc = 0.0

    # Compute the attraction between planet and other body
    def attraction(self, other, date):

        # Compute x, y, and total distances between planet and other body
        rx = other.xloc - self.xloc
        ry = other.yloc - self.yloc
        r =  sqrt(rx**2 + ry**2)

        if r != 0:

        # Compute the overall force
            f = (G*(self.mass * other.mass))/(r**2)


            # Compute the angle between the hypotenuse and the adjacent side
            theta = atan2(ry,rx)
            # Compute the x component of the force
            fx = f * cos(theta)
            # Compute the y component of the force
            fy = f * sin(theta)
            # Return the x and y components of the force to the main loop
            return fx, fy

        else:
            return 0,0

class rocket(Turtle):
    # Initialize planet name, location, velocity
    yloc = (1 * AU) *   0.96756
    xloc = (1 * AU) *  -0.17522
    vy = AU * -0.0031302  / 86400
    vx = AU * -0.017201 / 86400

    # Compute the attraction between planet and other body
    def attraction(self, other, date):

        # Compute x, y, and total distances between planet and other body
        rx = other.xloc - self.xloc
        ry = other.yloc - self.yloc
        r =  sqrt(rx**2 + ry**2)
        if r != 0:

        # Compute the overall force
            f = (G*(self.mass * other.mass))/(r**2)


            # Compute the angle between the hypotenuse and the adjacent side
            theta = atan2(ry,rx)
            # Compute the x component of the force
            fx = f * cos(theta)
            # Compute the y component of the force
            fy = f * sin(theta)
            # Return the x and y components of the force to the main loop
            return fx, fy

        else:
            return 0,0


    # def thrust():
    #     rocket = rocket()
    #
    #
    #
    # thrust()




# def stop(system):
#     if rocket.xloc==mars.xloc and rocket.yloc==mars.yloc:
#         delete rocket

def loop(system):                       # This function calculates the orbit of each planet and displays it in a window
    timestep = 1*24*3600                # One earth day
    date = 0                            # Starting date for the simulation - date increases for every iteration of the loop

    earthrocket=system[5]
    marsrocket=system[6]
    earth=system[5]

    for body in system:                                 # Runs a loop for each planet
        body.goto(body.xloc*SCALE, body.yloc*SCALE)     # Puts the planet in its proper location on the display
        body.pendown()                                  # Puts down the pen - this means that a line will be draw to show the path of the orbit

    while True:                         # Loop will run until user interrupts program (ctrl+c)
        force = {}                      # Create a dictionary that holds the total forces on each planet

        if date==0:
            marsrocket.hideturtle()
            marsrocket.penup()
        if date==20:
            earthrocket.hideturtle()
            earthrocket.penup()
        if date==40:
            marsrocket.showturtle()
            marsrocket.pendown()

        if date==40:
            rocket = planet()
            rocket.name = 'Intermediate Rocket'
            rocket.mass = 5.97 * 10**24
            rocket.penup()
            rocket.color('black')
            rocket.shape('classic')
            rocket.shapesize(0.5,0.5,1)
            rocket.diameter = 12742
            rocket.yloc = earth.yloc
            rocket.xloc = earth.xloc
            rocket.vy = 0
            rocket.vx = 0
            rocket.showturtle()
            rocket.pendown()
            rocket.forward(20)

        for body in system:

            total_fx = total_fy = 0.0   # Initialize the x and y components on the planet as 0

            # Update all forces exerted on the planets through gravity
            for other in system:
                if body is other: # makes sure the model isn't computing g force with itself
                    continue
                fx, fy = body.attraction(other, date)   # Goes to the function called attraction (line 20)
                total_fx += fx     # Sums up the x components of the gravitational forces on the planet
                total_fy += fy    # Sums up the y components of the gravitational forces on the planet

            force[body] = (total_fx, total_fy)        # Assign the total force exerted on the planet to the dictionary, force

        # Update velocities
        for body in system:
            fx, fy = force[body]                       # Assign the components of the total force to the variables fx and fy
            # Compute velocities from gravity
            body.vx +=  (fx* timestep) / body.mass
            body.vy +=  (fy* timestep) /body.mass

        # Update locations of planets
        for body in system:
            body.xloc += body.vx * timestep
            body.yloc += body.vy * timestep
            body.goto(body.xloc*SCALE, body.yloc*SCALE)         # Move everything!



        date += 1

def launch(rocket, plt):
    if rocket.yloc==plt.yloc:
        if rocket.xloc==plt.xloc:
            return True
    return False

def main():  # Sets up the positions, velocities, colours, and shapes of the planets on the display

    turtle.setup(800, 800)          # Set the window size to 800 by 800 pixels
    turtle.bgcolor("white")         # Set up the window with a white background

    """
    For each planet, the setup follows the same procedure:
    planet = planet()               Sets up the variables for the planet, goes to the function called planet (line 11)
    planet.name = 'planet name'     Names the planet
    planet.mass = number            Gives the planet a mass
    planet.penup()                  Picks up the turtle so it does not draw a line when you move it
    planet.color('colour')          Gives the planet a colour (ex. yellow)
    planet.shape('shape')           Gives the planet a shape (ex. circle)
    planet.xloc = number            Gives the planet an x component position
    planet.yloc = number            Gives the planet a y component position
    planet.vx = number              Gives the planet an x component velocity
    planet.vy = number              Gives the planet a y component velocity
    """

    sun = planet()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30
    sun.penup()
    sun.color('yellow')
    sun.shape('circle')
    sun.diameter = 1.3914 * 10**6
    sun.shapesize(2.0,2.0,1)
    """sun.vx = 1000
    sun.vy = 0"""

    earthrocket = planet()
    earthrocket.name = 'Earth Rocket'
    earthrocket.mass = 5.97 * 10**24
    earthrocket.penup()
    earthrocket.color('black')
    earthrocket.shape('classic')
    earthrocket.shapesize(0.5,0.5,1)
    earthrocket.diameter = 12742
    earthrocket.yloc = (1 * AU) *   0.96756
    earthrocket.xloc = (1 * AU) *  -0.17522
    earthrocket.vy = AU * -0.0031302  / 86400
    earthrocket.vx = AU * -0.017201 / 86400

    marsrocket = planet()
    marsrocket.name = 'Mars Rocket'
    marsrocket.mass = 6.39E23
    marsrocket.penup()
    marsrocket.color('black')
    marsrocket.shape('classic')
    marsrocket.shapesize(0.4,0.4,1)
    marsrocket.diameter = 3389.92 * 2
    marsrocket.xloc = (1 * AU) *  -1.320107604952232
    marsrocket.yloc = (1 * AU) *  -8.857574644771996E-01
    marsrocket.vy = AU * -1.042277973806052E-2  / 86400
    marsrocket.vx = AU * 8.320854741090488E-3 / 86400

    earth = planet()
    earth.name = 'Earth'
    earth.mass = 5.97 * 10**24
    earth.penup()
    earth.color('blue')
    earth.shape('circle')
    earth.shapesize(0.6,0.6,1)
    earth.diameter = 12742
    earth.yloc = (1 * AU) *   0.96756
    earth.xloc = (1 * AU) *  -0.17522
    earth.vy = AU * -0.0031302  / 86400
    earth.vx = AU * -0.017201 / 86400

    mars = planet()
    mars.name = 'Mars'
    mars.mass = 6.39E23
    mars.penup()
    mars.color('red')
    mars.shape('circle')
    mars.shapesize(0.4,0.4,1)
    mars.diameter = 3389.92 * 2
    mars.xloc = (1 * AU) *  -1.320107604952232
    mars.yloc = (1 * AU) *  -8.857574644771996E-01
    mars.vy = AU * -1.042277973806052E-2  / 86400
    mars.vx = AU * 8.320854741090488E-3 / 86400

    venus = planet()
    venus.name = 'Venus'
    venus.mass = 4.867E24
    venus.penup()
    venus.color('green')
    venus.shape('circle')
    venus.shapesize(0.5,0.5,1)
    venus.diameter = 6051.84 * 2
    venus.xloc = (1 * AU) *  7.232002999670082E-01
    venus.yloc = (1 * AU) *  5.254837930328842E-02
    venus.vy = AU * 2.008132769363285E-02 / 86400
    venus.vx = AU * -1.547265569012768E-03/ 86400


    mercury = planet()
    mercury.name = 'Mercury'
    mercury.mass = 3.302E23
    mercury.penup()
    mercury.color('gray')
    mercury.shape('circle')
    mercury.shapesize(0.3,0.3,1)
    mercury.diameter = 2440 * 2
    mercury.xloc = (1 * AU) *  -6.333487572394930E-02
    mercury.yloc = (1 * AU) *  -4.608453269808703E-01
    mercury.vy = AU * -2.399853089908365E-03 / 86400
    mercury.vx = AU * 2.222816779156590E-02/ 86400

    loop([sun, mars, earth, venus, mercury, earthrocket, marsrocket])       # Goes to the function called loop (line 37). Takes these planets and creates a solar system.


if __name__ == '__main__':          # The code starts here
    main()                          # Goes to the function called main (line 82)