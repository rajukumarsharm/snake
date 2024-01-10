import turtle
import random 
import time

delay = 0.1
sc =0 
hs = 0
bodies=[]
# creating a screen 
s = turtle.Screen()
s.title("Snake Game ")
s.bgcolor("light blue");
s.setup(width=600,height=600) #size of a screen 
 # creting a head 
head= turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction= "stop"

# creting a food for snake 
food= turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()
food.goto(150,200)
food.st()

# creting a score board 
sb = turtle .Turtle()
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score : 0  |  Highest Score : 0")
# certing function for moving in all directions
def moveUP ():
    if head. direction!="down":
        head.direction="up"
def moveDown ():
    if head .direction!="up":
        head.direction="down"
def moveLeft ():
    if head .direction!="right":
        head.direction="left"
def moveRight ():
    if head .direction!="left":
        head.direction="right"
def moveStop():
    head .direction="stop"

def move ():
    if head .direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "left":
        x= head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#event handing
s.listen()
s.onkey(moveUP,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveLeft,"Left")
s.onkey(moveRight,"Right")
s.onkey(moveStop,"space")
 

#mainloop
while True:
    s.update() # to updeta the screen check collision with border
    if head.xcor()>290:
        head.setx(-290)

    if head.xcor()<-290:
        head.setx(290)

    if head.ycor()>290:
        head.sety(-290)

    if head.ycor()<-290:
        head.sety(290)
    
    #check collision with food 
    
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

        # increase the body of sanck
        body= turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body) #append the new body iin list

        sc=sc+100
        delay=delay-0.001 # increase the speed
        if sc>hs :
            hs=sc
        sb.clear()
        sb.write("Score:{}  | Highst Score :{}" . format(sc,hs))
    # move sanck bodies
        
    for i in range (len(bodies)-1,0,-1):
        x=bodies [i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    for body in bodies:
        if body .distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("Score : {} | Highst Score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop





        

