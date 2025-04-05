from tkinter import *

print('Hello Everyone, This is a test area')

#defining a window    
root = Tk()

#Label widget
firstLabel = Label(root, text="Welcome To Main")
#puts widdget in first avaliable space (places on screen)
firstLabel.pack()

#title
root.title("Pack Testing")


#constantly loops this progam file
#root.mainloop()

#grid testing
root2 = Tk()

#title 
root2.title('grid window')

#label
label1 = Label(root2, text="This is label1")
label2 = Label(root2,text="this is label 2")
#grid packing, doesnt autofill anything (places on screen)
label1.grid(row = 0, column= 0)
label2.grid(row = 0, column= 4)

#can also do this one liner
label3 = Label(root2,text="this is a 3rd label").grid(row=1,column=0)

#activates root2
#root2.mainloop()

#button testing
root3 = Tk()
root3.title("Button Testing Window")

#simple button
button1 = Button(root3,text="Click me", padx= 50, pady= 25)
button1.pack()

#function for button
def bClick():
    labeltest = Label(root3,text="You clicked a button")
    labeltest.pack()

#action button, dont add () to functions
button2 = Button(root3, text="I have an action", command=bClick, fg="Blue", bg="Grey")
button2.pack()

#this still runs all above windows 
#root3.mainloop()

#input boxes
root4 = Tk()
root4.title("Input boxes")


#input widget
e = Entry(root4,width=50, fg="Black", bg="grey")
e.grid(row=0,column=0)
#adding default txt
e.insert(0,"Enter your name")


#gets user input from Entry widget
def click2():
    elabel= Label(root4,text="hello " + e.get())
    elabel.grid(row=2,column=0)


ebutton = Button(root4,text="Enter your name",command=click2)
ebutton.grid(row=0,column=1)

#root4.mainloop()



# creating a calculator here:

rootc = Tk()
rootc.title("Basic Calculator")

#function #1 will need to be able to pass numbers too it

#function #2



# creating numbers 
number1 = Button(rootc,text= "1",padx=10,pady=10).grid(row=3,column=0)
number2 = Button(rootc,text= "2",padx=10,pady=10).grid(row=3,column=1)
number3 = Button(rootc,text= "3",padx=10,pady=10).grid(row=3,column=2)
number4 = Button(rootc,text= "4",padx=10,pady=10).grid(row=2,column=0)
number5 = Button(rootc,text= "5",padx=10,pady=10).grid(row=2,column=1)
number6 = Button(rootc,text= "6",padx=10,pady=10).grid(row=2,column=2)
number7 = Button(rootc,text= "7",padx=10,pady=10).grid(row=1,column=0)
number8 = Button(rootc,text= "8",padx=10,pady=10).grid(row=1,column=1)
number9 = Button(rootc,text= "9",padx=10,pady=10).grid(row=1,column=2)
number0 = Button(rootc,text= "0",padx=10,pady=10).grid(row=4,column=0)

#clear
bClear = Button(rootc, text= "Clear",padx=20,pady=10).grid(row=4, column=1)

#equal and plus button
eqb = Button(rootc, text="=",padx=20,pady=10).grid(row=5,column=1)
pls = Button(rootc, text="+",padx=10,pady=10).grid(row=5,column=0)

rootc.mainloop()
