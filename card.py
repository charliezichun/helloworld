import turtle as t 
import random,time 
t.bgcolor("gold")
def heart() :
    t.seth(0)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(50,360-142.5418864678)
    t.fd(147.709957542 ) 
    t.penup()
    t.home()
    t.pendown()
    t.left(-90)
    t.circle(50,-(360-142.5418864678))
    t.fd(-147.709957542 ) 
    t.end_fill()
    t.penup()
    t.home()
    t.left(180)
    t.fd(50)
    t.left(90)
    t.forward(10)
    t.pendown()
    t.write("Happy teacher's day")

class Windmill():
    def __init__(self,x,l,color):
        self.length = random.randint(150,200)
        self.x = x 
        self.l = l
        self.color = color
    def draw_branch(self):
        t.up()
        t.goto(self.x,-290)
        t.pendown()
        t.goto(self.x,-290+self.length)
        
    def draw_blade(self,r):
        t.seth(0+r)
        t.fillcolor(self.color)
        t.begin_fill()
        for i in range(4):
            t.fd(self.l)
            t.lt(120)
            t.fd(self.l)
            t.goto(self.x,-290+self.length)
            t.seth((i+1)*90+r)
        t.end_fill()



List = []
color = ["red","orange","yellow","grey","cyan","blue","green",'magenta',"black","darkgoldenrod"]
for i in range(10):
    l = random.randint(20,70)
    w = Windmill(-310+i*70,l,color[i])
    List.append(w)
t.tracer(False)
#t.speed(1)
while True :

    for r in range(0,360,2):
        t.clear()
        
        for i in range(len(List)):
            
            List[i].draw_branch()
      
            List[i].draw_blade(r)
            heart()
            
            
        t.update()
        time.sleep(0.01)
        
    
t.done()
