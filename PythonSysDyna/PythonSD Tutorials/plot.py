from graphics import *
def f(x):  # define a function to plot
    return x**2

def getPoints(f1,a,b,n):
    """returns a list of n points on the graph of f1.  The interval [a,b] is
       divided into n equal intervals for the x coordinates of the points"""
    points = []
    dt = (b-a)/float(n)
    count = 0
    while count <=n:
        x = a+count*dt
        points.append((x, f1(x)))
        count = count+1
    
    return points


def myPlot(f1, x1,x2,y1,y2,n):
    """Displays f1 by plotting n points on the graph of f1 in the viewing window
       with x in the interval [x1,x2] and y in the interval [y1,y2]"""
    w = GraphWin("Function plot", 500, 500)
    w.setCoords(x1, y1, x2, y2)
    xAxis = Line(Point(0,y1), Point(0,y2))
    xAxis.draw(w)
    yAxis = Line(Point(x1,0), Point(x2,0))
    yAxis.draw(w)
    pList = getPoints(f1,x1,x2,n)
    for i in range(len(pList)-1):
        p1 = Point(pList[i][0],pList[i][1])
        p2 = Point(pList[i+1][0],pList[i+1][1])
        seg = Line(p1,p2)
        seg.draw(w)
    
    p = w.getMouse()
    w.close()



myPlot(f,-5,5,-5,5,30)
