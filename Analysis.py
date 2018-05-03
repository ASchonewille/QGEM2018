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
from sympy import *

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

def createFunction(m,b):
    global targetFunction
    x = Symbol('x')
    targetFunction = Lambda(x, m*x + b)
    return 

def printLambda(func):
    stringFunc = (str(func)).rstrip(")")
    splitFunc = stringFunc.split(",")
    prettyFunc = splitFunc[1].lstrip(" ")
    print(prettyFunc)
    return    

def cutData(x,y):
    lengthX = len(x)
    lengthY = len(y)
    xCut = x[1:lengthX]
    yCut = y[1:lengthY]
    return xCut, yCut



def takeDerivative(x0):
    global targetFunction
    deriv = sci.derivative(targetFunction, x0)
    return deriv

def main():
    global targetFunction
    x = [1,2,3]
    y = [2,3,4]
    plotGraph(x,y)
    a,b = determineFunction(x,y)
    createFunction(a,b)
    xCut,yCut = cutData(x,y)
    x0 = 1
    deriv = takeDerivative(x0)

    printLambda(targetFunction)
    print (a,b)
    print (xCut, yCut)
    print (deriv)
        
main()

