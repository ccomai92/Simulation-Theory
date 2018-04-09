# SIR.py
# Program to run simulation of SIR model for spread of influenza

def SIR(DT = 0.25, simLength = 14):
    numIterations = int(simLength/DT) + 1
    t = 0

    susceptibles = 762
    infecteds = 1
    recovereds = 0

    infection_rate = 0.00218
    recovery_rate = 0.5

    get_sick = infection_rate * susceptibles * infecteds
    recover = recovery_rate * infecteds

#    print '\t%s%s\t%s' % (t, "Susceptibles", "Infecteds", "Recovereds")
    tLst = [t]
    SLst = [susceptibles]
    ILst = [infecteds]
    RLst = [recovereds]
#    print '%10.2f\t%12.2f\t%12.2f\t%12.2f' % (t, susceptibles, infecteds, recovereds)
    for i in range(1, numIterations):
        t = i * DT
        susceptibles = susceptibles + (-get_sick) * DT
        infecteds = infecteds + (get_sick - recover) * DT
        recovereds = recovereds + (recover) * DT

        get_sick = infection_rate * susceptibles * infecteds
        recover = recovery_rate * infecteds

#        print '%10.2f\t%12.2f\t%12.2f\t%12.2f' % (t, susceptibles, infecteds, recovereds)
        tLst.append(t)
        SLst.append(susceptibles)
        ILst.append(infecteds)
        RLst.append(recovereds)

    outfile = open("SIR.dat", 'w')
    for i in range(numIterations):
        outfile.write("%6.3f\t%12.2f\t%12.2f\t%12.2f\n" % (tLst[i], SLst[i], ILst[i], RLst[i]))

    outfile.close()


SIR()
