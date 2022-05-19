# Import libraries
from ast import pattern
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyval
import re


def checkMax(max, min):
    '''
    Check the correctness of max an min 
    return:
    True: if max and min is valid
    False if  max and min is not valid
    '''
    if max > min:
        return True
    return False


def checkFun(input):
    '''
    check the coorectness of function
    using re a match function 
    return:
    True: if funcition is coorect
    False if Function not coorect
    '''
    # TODO: find or creat a correct RE experssion to match polnomial

    # pattern = re.compile("^([-+]?([0-9]*\.?[0-9]+)?(x(\\^[+-]?[0-9]+)?)?)+")
    # if pattern.match(input, re.IGNORECASE):
    #     return True
    # return False

    return True


def ploting(fun, max, min):
    '''
    fun: valid polynomail fun
    max: valid max number
    min valid min number

    ---
    returns void
    '''
    print("Trying to plot the function")
    fun = fun.replace("^", "**")
    xVal = np.linspace(min, max, 100)
    yVal = [eval(fun) for x in xVal]
    fig = plt.figure(figsize=(10, 5))
    # Create the plot
    plt.plot(xVal, yVal, color='red')
    plt.grid()
    plt.axhline()
    plt.axvline()

    # Show the plot
    plt.show()
    print("Function plotted successfully")

    # TODO: matplotlib embed in tkinter as a widget
