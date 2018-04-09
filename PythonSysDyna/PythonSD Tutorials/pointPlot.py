from graphics import *
import time
import random

def plotPoints(ptList, x1,x2,y1,y2):
    """Display the points in ptList in a graphics window where the x coordinates
       are in [x1,x2] and the y coordinates are in [y1,y2]"""
    w = GraphWin("Point plot", 500, 500)
    w.setCoords(x1, y1, x2, y2)
    xAxis = Line(Point(0,y1), Point(0,y2))
    xAxis.draw(w)
    yAxis = Line(Point(x1,0), Point(x2,0))
    yAxis.draw(w)
    r = (y2-y1)/100.0  #a radius for the point depending on the size of window
    for (x,y) in ptList:
        p = Point(x,y)
        c = Circle(p,r)
        c.setFill("blue")
        c.draw(w)
        time.sleep(.5)
    p1 = w.getMouse()
    w.close()

pts = []
for i in range(10):
    p = (random.random(), random.random())
    pts.append(p)

plotPoints(pts,-.5,1.5,-.5,1.5)

    
