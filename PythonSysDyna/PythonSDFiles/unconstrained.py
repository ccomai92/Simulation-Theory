# unconstrained.py# Program to run simulation of unconstrained growth# and to display graph of population versus time# and to display a table of the resultsfrom graphics import *WIN_WIDTH  = 500WIN_HEIGHT = 300def main():    maxt, maxy, pts = unconstrained()    plotGraph(maxt, maxy, pts)# Function to run a simulation of unconstrained growth,# to display a table of time and population, and to# return maximum time, maximum population, and list# of points with time and populationdef unconstrained(growthRate = 0.10, P = 100, DT = 0.25, simLength = 40):    numIterations = int(simLength/DT) + 1    print "         t\tpopulation\tgrowth"    t = 0    growth = growthRate * P    print '%10.2f\t%12.2f\t%12.2f' % (t, P, growth)    pts = [[t, P]]    tLst = [t]    yLst = [P]    print '%10.2f\t%12.2f\t%12.2f' % (t, P, growth)    for i in range(1, numIterations):        t = i * DT        P = P + growth * DT        growth = growthRate * P        print '%10.2f\t%12.2f\t%12.2f' % (t, P, growth)        pts.append([t, P])        tLst.append(t)        yLst.append(P)    return int(max(tLst) + 0.5), int(max(yLst) + 0.5), pts    # Function to plot points pts with horizontal axis going from# 0 to maxt and vertical axis going from 0 to maxydef plotGraph(maxt, maxy, pts):    win = GraphWin("Unconstrained Growth", WIN_WIDTH, WIN_HEIGHT)    win.setBackground("white")    win.setCoords(-0.15 * maxt, -0.1 * maxy, 1.1 * maxt, 1.15 * maxy)    plotArea = Rectangle(Point(0, 0), Point(maxt, maxy))    plotArea.draw(win)    for i in range(0, maxt + 1, 10):        Text(Point(i, -200), i).draw(win)    Text(Point(-0.05 * maxt, maxy/2), maxy/2).draw(win)    Text(Point(-0.05 * maxt, maxy), maxy).draw(win)    Text(Point(0, 1.08 * maxy), "population").draw(win)        for pt in pts:        win.plot(pt[0], pt[1])main()