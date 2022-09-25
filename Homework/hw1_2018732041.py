import turtle as t
t.shape("turtle")
t.speed(15)

def face(): # 얼굴
    t.penup()
    t.setposition(0,-280)
    t.pendown()
    t.pensize(5)
    t.color("black","orange")
    t.begin_fill()
    t.circle(300) 
    t.end_fill()

def mouth():
    t.pensize(5)
    t.penup()
    t.setposition(-130,-170)
    t.color("red","red")
    t.begin_fill()
    t.pendown()
    t.right(40)
    t.circle(210,80)
    t.left(167)
    t.circle(-300,53)
    t.end_fill()

def nose():
    t.penup()
    t.home()
    t.pendown()
    t.color("yellow","yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
   
def eyes():
    t.penup()
    t.pensize(5)
    t.setposition(-200,130)
    t.pendown()
    t.color("black","blue")
    t.begin_fill()
    t.right(30)
    t.circle(150,60)
    t.penup()
    t.setposition(-200,130)
    t.pendown()
    t.circle(-150,60)
    t.end_fill()
    
    t.penup()
    t.setposition(80,130)
    t.pensize(10)
    t.pendown()
    t.color("black","pink")
    t.begin_fill()
    t.right(30)
    t.circle(60,130)
    t.penup()
    t.setposition(80,130)
    t.pendown()
    t.circle(-60,130)
    t.end_fill()

def main():
    face()
    eyes()
    nose()
    mouth()
    t.hideturtle()
    t.done()
    
    
main()




