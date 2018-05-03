from sympy import *

def createFunction(m,b):
    x = Symbol('x')
    equation = Lambda(x, m*x + b)
    return equation

def printLambda(func):
    stringFunc = (str(func)).rstrip(")")
    splitFunc = stringFunc.split(",")
    prettyFunc = splitFunc[1].lstrip(" ")
    print(prettyFunc)

def main():
    equation = createFunction(5,10)
    printLambda(equation)
    print(equation(3))
    
main()
