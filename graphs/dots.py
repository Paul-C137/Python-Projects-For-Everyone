from graphics import *
import random

win = GraphWin('Dots',400, 400)

colors = ['black', 'gray', 'white', 'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple']


while True:
    x = random.randint(0,400)
    y = random.randint(0,400)
    color = colors[random.randint(0,len(colors)-1)]
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)


