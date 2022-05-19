# Import Libraries
from tkinter import *
from tkinter import messagebox
from Plotting import *


# Functions

# btnPlot Button Logic

def plotbtn():
    '''
    btnPlot button Function
    Function that recive the input from the entrty userInput
    When the button pressed plotButton
    Then It clears the Entry userInput
    Finally It plots the graph

    return: viod

    '''
    inFun = entryFun.get()
    entryFun.delete(0, END)

    inMax = entryMax.get()
    entryMax.delete(0, END)

    inMin = entryMin.get()
    entryMin.delete(0, END)

    print("Input Function recieved from user: " + inFun)
    print("Max number recieved from user: " + inMax)
    print("Min number recieved from user: " + inMin)

    try:
        inMax = float(inMax)
        inMin = float(inMin)
    except:
        messagebox.showerror(
            "Value Error!", "Max and Min must be number")
        print("Max and Min must be number")

    # check if max and min is correct
    # imported from Plotting
    if not checkMax(inMax, inMin):
        print("Error in max an min values")
        messagebox.showerror(
            "Value Error!", "Max should be bigger than Min")

    # check if fun is correct
    # imported from Plotting
    if not checkFun(inFun):
        print("Error in function values")
        messagebox.showerror(
            "Value Error!", "Enter a Valid Function\n  e.g., 5*x^3 + 2*x.")

    try:

        ploting(inFun, inMax, inMin)

    except:
        print("error accourd while plotting")


# Exit Button Logic


def exitprog():
    '''
    btnExit button function

    return: viod
    '''
    root.quit()
    print("User Exitted the program")


# Root Widget
root = Tk()
root.title("Function Plotter")
root.iconbitmap("going.ico")
# TODO: window size fixed


#  Define GUI Widgets
lblFunction = Label(root, text="Function: ")
entryFun = Entry(root, width=50, borderwidth=3)

lblMax = Label(root, text="Maximum Value: ")
entryMax = Entry(root, width=50, borderwidth=3)

lblMin = Label(root, text="Minimum Values ")
entryMin = Entry(root, width=50, borderwidth=3)

btnPlot = Button(root, text="Plot Function!", command=plotbtn, width=30)
btnExit = Button(root, text="Exit", command=exitprog,
                 width=30, fg="white", bg='darkred')

# Gridding Widgets on screen
lblFunction.grid(row=0, column=0, pady=10, padx=10)
entryFun.grid(row=0, column=1, pady=10, padx=10, columnspan=2)

lblMax.grid(row=1, column=0, pady=10, padx=10)
entryMax.grid(row=1, column=1, pady=10, padx=10, columnspan=2)

lblMin.grid(row=2, column=0, pady=10, padx=10)
entryMin.grid(row=2, column=1, pady=10, padx=10,  columnspan=2)

btnPlot.grid(row=3, column=0, padx=50, pady=20)
btnExit.grid(row=3, column=2, padx=50, pady=20)


# Looping the root Widget

root.mainloop()
#
