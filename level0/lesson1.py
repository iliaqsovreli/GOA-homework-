from turtle import *

#we want to paint a house

#step 1: draw a square

speed(20)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("black")
begin_fill()
penup()
goto(15, 100)
pendown()
left(120)
forward(45)
left(90)
forward(40)
left(90)
forward(45)
left(90)
forward(40)
end_fill()

penup()
goto(140, 100)
pendown()
begin_fill()
left(90)
forward(45)
left(90)
forward(40)
left(90)
forward(45)
left(90)
forward(40)
end_fill()

exitonclick()
