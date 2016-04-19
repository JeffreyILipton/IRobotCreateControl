﻿import csv
import numpy as np
from numpy import genfromtxt
import matplotlib
import matplotlib.pyplot as plt
import sys
from CreateModel import minAngleDif


def plotCSVRun(file = 'run.csv'):
    data = genfromtxt(file,delimiter = ',')
    print data.shape
    headings = data[0,:]
    data = np.delete(data,0,0)
    print data.shape
    
    # convert T from ms since epoch to seconds since start
    T = data[:,0]
    T = T-T[0]
    T = T/(1e4)

    X_target = data[:,1]
    Y_target = data[:,2]
    Theta_target = data[:,3] 
    X_actual = data[:,4]
    Y_actual = data[:,5]
    Theta_actual = data[:,6]
    Uo0 = data[:,8]
    Uo1 = data[:,9]
    Uc0 = data[:,10]
    Uc1 = data[:,11]
    


    # plot of XY target and actual
    # sub plot of XYs over time
    # sub plot of thetas over time
    # sub plot of XY
    plt.figure(1)
    plt.subplot(211)
    plt.plot(T,X_target,'-',label ="X target", linewidth=3)
    plt.plot(T,Y_target,'-',label ="Y target",linewidth=3)
    plt.plot(T,X_actual,'--',label ="X Actual",linewidth=2)
    plt.plot(T,Y_actual,'--',label ="Y Actual",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('XY vs T')



    
    plt.subplot(212)
    plt.plot(T,Theta_target,'-',label =r"$\theta$ target",linewidth=3)
    plt.plot(T,Theta_actual,'--',label =r"$\theta$ actual",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('Theta v T')


    plt.figure(2)
    plt.plot(X_target,Y_target,'-', label = 'Target',linewidth=3)
    plt.plot(X_actual,Y_actual,'--', label = 'Actual',linewidth=2)
    plt.axes().set_aspect('equal')
    plt.legend(bbox_to_anchor = (1.15,0.5), loc=7, borderaxespad=0.)
    plt.title('XY')




    # plot of Error
    #    sub plot of error in XY over time
    #    sub plot of error in Theta over time
    Ex = X_target-X_actual
    Ey = Y_target-Y_actual
    vAngDif = np.vectorize(minAngleDif,otypes=[np.float])
    Etheta =  vAngDif(Theta_actual,Theta_target)
    plt.figure(3)
    plt.subplot(311)    
    plt.plot(T,Ex,'-',label ="X Error", linewidth=2)
    plt.plot(T,Ey,'--',label ="Y Error",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('XY Error over time')

    plt.subplot(312)    
    plt.plot(T,Etheta,'-',label =r"$\theta$ Error", linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('Angle Error over time')


    R_error = np.sqrt(np.square(Ex)+np.square(Ey));
 
    plt.subplot(313)    
    plt.plot(T,R_error,'-',label =r"Radial Error", linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('Radial Error over time')


    # plot of U
    #    sub plot of Uo 
    #    sub plot of Uc     
    plt.figure(4)
    plt.subplot(211)    
    plt.plot(T,Uo0,'-',label ="Uo 0", linewidth=2)
    plt.plot(T,Uo1,'--',label ="Uo 1",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('Baseline speeds time')

    plt.subplot(212)    
    plt.plot(T,Uc0,'-',label ="Uc 0", linewidth=2)
    plt.plot(T,Uc1,'--',label ="Uc 1",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('Baseline speeds time')
    plt.title('Controller speeds')
    #

    plt.show()

def plotCharicterizationRun(file = 'run.csv'):
    data = genfromtxt(file,delimiter = ',')
    print data.shape
    headings = data[0,:]
    data = np.delete(data,0,0)
    print data.shape
    
    # convert T from ms since epoch to seconds since start
    T = data[:,0]
    T = T-T[0]
    T = T/(1e4)


    X_actual = data[:,2]
    Y_actual = data[:,3]
    Theta_actual = data[:,4]
    Uset = data[:,1]

    


    # plot of XY target and actual
    # sub plot of XYs over time
    # sub plot of thetas over time
    # sub plot of XY
    plt.figure(1)
    plt.subplot(411)
    plt.plot(T,X_actual,'--',label ="X Actual",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('X vs T')

    plt.subplot(412)
    plt.plot(T,Y_actual,'--',label ="Y Actual",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title('Y v T')

    plt.subplot(413)
    plt.plot(T,Theta_actual,'--',label =r"\theta Actual",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title(r'\theta v T')

    plt.subplot(414)
    plt.plot(T,Uset,'--',label =r"U ",linewidth=2)
    plt.legend(bbox_to_anchor = (1.1,0.5), loc=7, borderaxespad=0.)
    plt.title(r'\U v T')


    plt.show()

def main():
    plotCSVRun()

if __name__ == "__main__":
    sys.exit(int(main() or 0))