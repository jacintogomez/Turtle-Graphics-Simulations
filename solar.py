import turtle
from turtle import *
from math import *

G=6.6741e-11
AU=149600000000
SCALE=75.0/AU

class planet(Turtle):
    def __init__(self,params):
        super().__init__()
        self.name=params[0]
        self.mass=params[1]
        self.diameter=params[2]
        self.color(params[3])
        self.shape(params[4])
        self.shapesize(params[5][0],params[5][1],params[5][2])
        self.xloc=params[6]
        self.yloc=params[7]
        self.vx=params[8]
        self.vy=params[9]
    def attraction(self,other,date):
        # x, y and total distance
        rx=other.xloc-self.xloc
        ry=other.yloc-self.yloc
        r=sqrt(rx**2+ry**2)
        if r!=0:
            f=(G*(self.mass*other.mass))/(r**2)
            theta=atan2(ry,rx)
            fx=f*cos(theta) # x force component
            fy=f*sin(theta) # y force component
            return fx,fy
        else:
            return 0,0

class rocket(Turtle):
    yloc=(1*AU)*0.96756
    xloc=(1*AU)*-0.17522
    vy=AU*-0.0031302/86400
    vx=AU*-0.017201/86400

    def attraction(self, other, date):
        rx=other.xloc-self.xloc
        ry=other.yloc-self.yloc
        r=sqrt(rx**2+ry**2)
        if r!=0:
            f=(G*(self.mass*other.mass))/(r**2)
            theta=atan2(ry,rx)
            fx=f*cos(theta)
            fy=f*sin(theta)
            return fx,fy
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

def loop(system):
    timestep=1*24*3600 # One day
    date=0
    # earthrocket=system[5]
    # marsrocket=system[6]
    # earth=system[5]
    for body in system:
        body.goto(body.xloc*SCALE,body.yloc*SCALE)
        body.pendown() # start drawing
    while True:
        force={}
        # if date==0:
        #     marsrocket.hideturtle()
        #     marsrocket.penup()
        # if date==20:
        #     earthrocket.hideturtle()
        #     earthrocket.penup()
        # if date==40:
        #     marsrocket.showturtle()
        #     marsrocket.pendown()
        # if date==40:
        #     rocket=planet()
        #     rocket.name='Intermediate Rocket'
        #     rocket.mass=5.97*10**24
        #     rocket.penup()
        #     rocket.color('black')
        #     rocket.shape('classic')
        #     rocket.shapesize(0.5,0.5,1)
        #     rocket.diameter=12742
        #     rocket.yloc=earth.yloc
        #     rocket.xloc=earth.xloc
        #     rocket.vy=0
        #     rocket.vx=0
        #     rocket.showturtle()
        #     rocket.pendown()
        #     rocket.forward(20)
        for body in system:
            total_fx=total_fy=0.0   # Initialize the x and y components on the planet as 0
            # Update all forces exerted on the planets through gravity
            for other in system:
                if body is other: # makes sure the model isn't computing g force with itself
                    continue
                fx,fy=body.attraction(other, date)   # Goes to the function called attraction (line 20)
                total_fx+=fx
                total_fy+=fy
            force[body]=(total_fx,total_fy)

        # Update velocities
        for body in system:
            fx,fy=force[body]                       # Assign the components of the total force to the variables fx and fy
            # Compute velocities from gravity
            body.vx+=(fx* timestep)/body.mass
            body.vy+=(fy* timestep)/body.mass

        # Update locations of planets
        for body in system:
            body.xloc+=body.vx*timestep
            body.yloc+=body.vy*timestep
            body.goto(body.xloc*SCALE,body.yloc*SCALE)
        date+=1

def launch(rocket,plt):
    if rocket.yloc==plt.yloc:
        if rocket.xloc==plt.xloc:
            return True
    return False

def scaledown(v):
    return v*AU

def start_simulation():
    turtle.setup(800,800)
    turtle.bgcolor("white")
    s=86400
    cir='circle'
    ship='classic'

    su=['Sun',1.98892*10**30,1.3914*10**6,'yellow',cir,[2.0,2.0,1],0,0,0,0]
    sun=planet(su)
    sun.color('yellow')
    sun.penup()

    # mer=['Earth Rocket',5.97*10**24,12742,'black',ship,[0.5,0.5,1],scaledown(-6.333487572394930E-02),scaledown(-4.608453269808703E-01),scaledown(-2.399853089908365E-03)/s,scaledown(2.222816779156590E-02)/s]
    # earthrocket=planet()
    # earthrocket.name='Earth Rocket'
    # earthrocket.mass=
    # earthrocket.penup()
    # earthrocket.color('black')
    # earthrocket.shape('classic')
    # earthrocket.shapesize(0.5,0.5,1)
    # earthrocket.diameter=
    # earthrocket.yloc=(1*AU)*0.96756
    # earthrocket.xloc=(1*AU)*-0.17522
    # earthrocket.vy=AU*-0.0031302/86400
    # earthrocket.vx=AU*-0.017201/86400
    #
    # mer=['Mercury',3.302E23,2440*2,'gray',cir,[0.3,0.3,1],scaledown(-6.333487572394930E-02),scaledown(-4.608453269808703E-01),scaledown(-2.399853089908365E-03)/s,scaledown(2.222816779156590E-02)/s]
    # marsrocket=planet()
    # marsrocket.name='Mars Rocket'
    # marsrocket.mass=6.39E23
    # marsrocket.penup()
    # marsrocket.color('black')
    # marsrocket.shape('classic')
    # marsrocket.shapesize(0.4,0.4,1)
    # marsrocket.diameter=3389.92*2
    # marsrocket.xloc=(1*AU)*-1.320107604952232
    # marsrocket.yloc=(1*AU)*-8.857574644771996E-01
    # marsrocket.vy=AU*-1.042277973806052E-2/86400
    # marsrocket.vx=AU*8.320854741090488E-3/86400

    ear=['Earth',5.97*10**24,12742,'blue',cir,[0.6,0.6,1],scaledown(-0.17522),scaledown(0.96756),scaledown(-0.017201)/s,scaledown(-0.0031302)/s]
    earth=planet(ear)
    earth.penup()

    mar=['Mars',6.39E23,3389.92*2,'red',cir,[0.4,0.4,1],scaledown(-1.320107604952232),scaledown(-8.857574644771996E-01),scaledown(8.320854741090488E-3)/s,scaledown(-1.042277973806052E-2)/s]
    mars=planet(mar)
    mars.penup()

    ven=['Venus',4.867E24,6051.84*2,'green',cir,[0.5,0.5,1],scaledown(7.232002999670082E-01),scaledown(5.254837930328842E-02),scaledown(-1.547265569012768E-03)/s,scaledown(2.008132769363285E-02)/s]
    venus=planet(ven)
    venus.penup()

    mer=['Mercury',3.302E23,2440*2,'gray',cir,[0.3,0.3,1],scaledown(-6.333487572394930E-02),scaledown(-4.608453269808703E-01),scaledown(2.222816779156590E-02)/s,scaledown(-2.399853089908365E-03)/s]
    mercury=planet(mer)
    mercury.penup()

    astros=[sun,mercury,venus,earth,mars]
    loop(astros)

start_simulation()