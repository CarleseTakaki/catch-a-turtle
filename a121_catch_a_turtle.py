# a121_catch_a_turtle.py
 
 
#-----import statements-----
import turtle as trtl
import random as rand
 
#-----game configuration----
spot_color = "lightcoral"
spot_size = int(2)
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20,"normal")
timer=30
counter_interval = 1000
timer_up= False
 
colors = ["palegreen", "meduimaquamarine", "forestgreen", "limegreen"]
 
#-----initialize turtle-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-290,190)
counter = trtl.Turtle()
counter.speed(0)
counter.penup()
counter.goto(-290,100)
#-----game functions--------
spot.fillcolor(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)
 
def change_position ():
  new_xpos = rand.randint(-300,300)
  new_ypos = rand.randint(-300,300)
  spot.goto(new_xpos, new_ypos)
 
def spot_clicked(x,y):
  global timer_up
  if timer_up == False:
    spot.hideturtle()
    spot.penup()
    update_score()
    change_position()
    spot.showturtle()
  else:
    spot.hideturtle()
 
 
def update_score():
  score_writer.clear()
  global score
  score += 1
  score_writer.write(score, font=font_setup)
 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up=True
  else:
    counter.write("timer: " + str(timer), font=font_setup)
    timer -=1
    counter.getscreen().ontimer(countdown, counter_interval)
 
def add_color():
  spot.stamp
#-----events----------------
spot.onclick(spot_clicked)
wn=trtl.Screen ()
wn.bgcolor("mediumturquoise")
wn.ontimer(countdown, counter_interval)
wn.mainloop ()

