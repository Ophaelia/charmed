#pretty triangle spiral
from turtle import*

def go():
    fd(x)
    left(120)
    fd(x+10)
    left(120)
    
x=10
y=20

while x<2000 and y<2000:
    go()
    x=x+20
    y=x+40
