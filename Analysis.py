"""
QGEM 2018
Dry Lab
Analysis
Authors: Abigael, Eric
Start Date: May 2, 2018

This program was made to compute the calculation of concentration of cortisol
"""



import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sci

global cortisolBindingRate
global luciferaseUnitLight
global samplingPeriod
global discardPeriod
global targetFunction


def plotGraph(x,y):

    X = np.array(x)
    Y = np.array(y)
    plt.scatter(X,Y)
    plt.show()
    return

def determineFunction(x,y):

    function = np.polyfit(x,y,1,rcond=None, full=False)
    a = function[0]
    b = function[1]
    return a,b

def lambdaFunction(a,b):

    global targetFunction    
    targetFunction = lambda x : a*x + b
    return 
    

def cutData(x,y):
    lengthX = len(x)
    lengthY = len(y)
    xCut = x[1:lengthX]
    yCut = y[1:lengthY]
    return xCut, yCut



def takeDerivative(targetFunction, x0):
    derivative = sci.derivative(targetFunction, x0)
    return
def main():
    global targetFunction
    x = [1,2,3]
    y = [2,3,4]
    plotGraph(x,y)
    a,b = determineFunction(x,y)
    lambdaFunction(a,b)
    xCut,yCut = cutData(x,y)
    x0 = 1
    derivative = takeDerivative(targetFunction, x0)

    print(targetFunction)
    print (a,b)
    print (xCut, yCut)
    print (derivative)
        
main()

