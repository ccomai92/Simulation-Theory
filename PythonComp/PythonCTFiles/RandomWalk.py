# RandomWalk.py
#
# 10.2  Random Walk
#
# Introduction to Computational Science:  Modeling and Simulation for the Sciences
# Angela B. Shiflet and George W. Shiflet
# Wofford College
# Copyright 2006 by Princeton University Press
#

from graphics import *
from random import randrange

WIN_WIDTH  = 500
WIN_HEIGHT = 500

def main():
    
# Show the path and distance of last position from first

    # determine points of path
    x = x0 = 0
    y = y0 = 0
    n = 25  # number of steps
    xLst = [0] 
    yLst = [0] 
    lst = [[0, 0]]
    for i in range(n):
        if randrange(2) == 0:
            x = x + 1
        else:
            x = x - 1
            
        if randrange(2) == 0:
            y = y + 1
        else:
            y = y - 1

        xLst.append(x)
        yLst.append(y)
        lst.append([x, y])

    xmin = min(xLst)
    xmax = max(xLst)
    ymin = min(yLst)
    ymax = max(yLst)

    # display points in blue
    listPlot(xmin, ymin, xmax, ymax, lst)
       
    
# display points in blue with first and last point in red and
# lines segments connecting points

def listPlot(xmin, ymin, xmax, ymax, pts):
    win = GraphWin("Random Walk", WIN_WIDTH, WIN_HEIGHT)
    win.setBackground("white")
    win.setCoords(xmin - 1, ymin - 1, xmax + 1, ymax + 1)

    cir = Circle(Point(pts[0][0], pts[0][1]), 0.15)
    cir.setFill("red")
    cir.draw(win)
    ptPrev = pts[0]
    
    for pt in pts[1:]:
        line = Line(Point(ptPrev[0], ptPrev[1]), (Point(pt[0], pt[1])))
        line.draw(win)
        cir = Circle(Point(pt[0], pt[1]), 0.1)
        cir.setFill("blue")
        cir.draw(win)
        ptPrev = pt

    cir = Circle(Point(pt[0], pt[1]), 0.15)
    cir.setFill("red")
    cir.draw(win)


main()
    
