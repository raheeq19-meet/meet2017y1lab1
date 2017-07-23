import turtle

#Everything that comes after the # is a
#comment.
#It is a note to the person reading the code.
#The computer ignores it.
#Write your code below here...
# ...and end it before the next line.



turtle.penup()
#Pick up the pen so it doesn’t
                  #draw
turtle.goto(-200,-100)
#Move the turtle to the
                          #position (-200, -100)
                          #on the screen
turtle.pendown()
#Put the pen down to start
                    #drawing
#Draw the M:
turtle.goto(-200,-100+200)
turtle.goto(-200+50,-100)
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

#Draw the E:
turtle.penup()
turtle.goto(-200+150,-100)
turtle.pendown()
turtle.goto(-200+150,-100+200)
turtle.goto(-200+200,-100+200)
turtle.penup()
turtle.goto(-200+150,-100+100)
turtle.pendown()
turtle.goto(-200+200,-100+100)
turtle.penup()
turtle.goto(-200+150,-100)
turtle.pendown()
turtle.goto(-200+200,-100)

#Draw the E
turtle.penup()
turtle.goto(-200+250,-100)
turtle.pendown()
turtle.goto(-200+250,-100+200)
turtle.goto(-200+300,-100+200)
turtle.penup()
turtle.goto(-200+250,-100+100)
turtle.pendown()
turtle.goto(-200+300,-100+100)
turtle.penup()
turtle.goto(-200+250,-100)
turtle.pendown()
turtle.goto(-200+300,-100)

#draw the T
turtle.penup()
turtle.goto(-200+350,-100+200)
turtle.pendown()
turtle.goto(-200+450,-100+200)
turtle.penup()
turtle.goto(-200+400,-100+200)
turtle.pendown()
turtle.goto(-200+400,-100)


turtle.mainloop()
