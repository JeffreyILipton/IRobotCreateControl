import csv
import numpy as np
from numpy import genfromtxt
import matplotlib
import matplotlib.pyplot as plt
import sys
from CreateModel import minAngleDif
from scipy.stats import linregress

def AnalyseFile(file = 'Run.csv'):
    data = genfromtxt(file,delimiter = ',')
    print data.shape
    headings = data[0,:]
    data = np.delete(data,0,0)
    print data.shape
    
    # convert T from ms since epoch to seconds since start
    #T = data[:,0]
    #T = T-T[0]
    #T = T/(1e6)
    #data[:,0]=T

    speeds = np.unique(data[:,1])
    speeds = np.delete(speeds,0,0)
    analysis = np.zeros((speeds.size,3))
    for i in range(0,speeds.size):
        speed = speeds[i]
        analysis[i,:] = analyzeSpeed(speed,data)

    
    Uslope, Uintercept, U_r_value, U_p_value, U_std_err = linregress(analysis[:,0],analysis[:,2])
    calced = Uslope*analysis[:,0]+Uintercept

    plt.figure(1)
    plt.plot(analysis[:,0],analysis[:,1],'-')
    plt.title("cmd vs delay")

    plt.figure(2)
    plt.plot(analysis[:,0],analysis[:,2],'-')
    plt.plot(analysis[:,0],calced,'--')
    plt.title("cmd vs Actual speed")

    print "Uslope: ", Uslope,"\tr:", U_r_value,"\t stdErr: ",U_std_err

    plt.show()



def analyzeSpeed(speed,data,doplot = False):
    section = data[np.where(data[:,1]==speed)]
    To = section[0,0]
    Xo = section[0,2]
    Yo = section[0,3]
    section[:,0] = (section[:,0]-To)/(1e6)

    section[:,2] = section[:,2]-Xo
    section[:,3] = section[:,3]-Yo
    moving = section[np.where(section[:,2]>2.0)]

    D = np.sqrt(np.square(moving[:,2])+np.square(moving[:,3]));
    if doplot:
        plt.figure(1)
        plt.subplot(211)
        plt.plot(moving[:,0],D,'-')
        plt.title("D vs T")
        plt.subplot(212)
        plt.plot(moving[:,2],moving[:,3],'-')
        plt.show()

    timeToStart = moving[0,0]
    slope, intercept, r_value, p_value, std_err = linregress(moving[:,0],D)
    print "cmd: ",speed, "\tactual:" , slope,"\tr:", r_value
    return [speed,timeToStart,slope]

def main():
    AnalyseFile('unifiedtest.csv')

if __name__ == "__main__":
    sys.exit(int(main() or 0))