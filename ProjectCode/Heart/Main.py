import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import DTALG as DT
import LogisticRegression as LR
import CNN as cnn
import RandomForest as RF
import Predict as pred
bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"

  
# Show image using label


def Home():
	global window
	def clear():
	    print("Clear1")
	      
	    txt1.delete(0, 'end')
	    txt2.delete(0, 'end')
	    txt3.delete(0, 'end')
	    txt4.delete(0, 'end')    
	    txt5.delete(0, 'end')
	    txt6.delete(0, 'end')
	    txt7.delete(0, 'end')
	    txt8.delete(0, 'end')    
	    txt9.delete(0, 'end')
	    txt10.delete(0, 'end')
	    txt11.delete(0, 'end')
	    txt12.delete(0, 'end')    
	    txt13.delete(0, 'end')
	    txt14.delete(0, 'end')
	    

	window = tk.Tk()
	
	window.title("Heart Disease Prediction")
	 
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

	message1 = tk.Label(window, text="Automated Cardio Vascular Disease Diagonsis Using HBO With CNN " ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=1)

	

	lbl1 = tk.Label(window, text="Enter Gender",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=50, y=100)
	
	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=250, y=115)

	lbl2 = tk.Label(window, text="Enter Age",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=50, y=170)
	
	txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=250, y=175)
	lbl3 = tk.Label(window, text="Current Smoker",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=50, y=230)
	
	txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=250, y=235)
	
	lbl4 = tk.Label(window, text="Cigarets/day",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl4.place(x=50, y=285)
	
	txt4 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt4.place(x=250, y=290)

	lbl5 = tk.Label(window, text="Do You have BP",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl5.place(x=50, y=350)
	
	txt5 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt5.place(x=250, y=365)
	lbl6 = tk.Label(window, text="Do You have Stroke",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl6.place(x=50, y=420)
	
	txt6 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt6.place(x=250, y=435)
	lbl7 = tk.Label(window, text="Do You have HyperTension",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl7.place(x=700, y=100)
	
	txt7 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt7.place(x=950, y=115)

	lbl8 = tk.Label(window, text="Do You have Diabetics",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl8.place(x=700, y=170)
	
	txt8 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt8.place(x=950, y=175)
	lbl9 = tk.Label(window, text="Your Cholstral",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl9.place(x=700, y=230)
	
	txt9 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt9.place(x=950, y=235)
	lbl10 = tk.Label(window, text="SysBp",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl10.place(x=700, y=285)
	
	txt10 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt10.place(x=950, y=290)
	lbl11 = tk.Label(window, text="DiaBp",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl11.place(x=700, y=350)
	
	txt11 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt11.place(x=950, y=365)

	lbl12 = tk.Label(window, text="BMI",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl12.place(x=700, y=420)
	
	txt12 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt12.place(x=950, y=435)
	lbl13 = tk.Label(window, text="Heart Rate",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl13.place(x=700, y=480)
	
	txt13 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt13.place(x=950, y=495)
	lbl14 = tk.Label(window, text=" Your Gulucose Level",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl14.place(x=700, y=540)
	
	txt14 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt14.place(x=950, y=555)



		

	def LRprocess():
		sym="dataset.csv"
		if sym != "":
			LR.process(sym)
			tm.showinfo("Input", "Logistic Regression Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def RFprocess():
		sym="dataset.csv"
		if sym != "":
			RF.process(sym)
			tm.showinfo("Input", "Random Forest Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def DTProcess():
		sym="dataset.csv"
		if sym != "":
			DT.process(sym)
			tm.showinfo("Input", "Decision Tree  Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def CNNprocess():
		sym="dataset.csv"
		if sym != "":
			cnn.process(sym)
			tm.showinfo("Input", "CNN Finished Success")
		else:
			tm.showinfo("Input error", "Select Dataset File")

	def Predictprocess():
                sym="dataset.csv"
                a1=txt1.get()
                if a1=="male":
                        a1=1
                else:
                        a1=0
                a2=txt2.get()
                a3=txt3.get()
                if a3=="yes":
                        a3=1
                else:
                        a3=0
                a4=txt4.get()
                a5=txt5.get()
                if a5=="yes":
                        a5=1
                else:
                        a5=0
                a6=txt6.get()
                if a6=="yes":
                        a6=1
                else:
                        a6=0
                a7=txt7.get()
                if a7=="yes":
                        a7=1
                else:
                        a7=0
                a8=txt8.get()
                if a8=="yes":
                        a8=1
                else:
                        a8=0
                a9=txt9.get()
                a10=txt10.get()
                a11=txt11.get()
                a12=txt12.get()
                a13=txt13.get()
                a14=txt14.get()
                if a1 == "":
                        tm.showinfo("Insert error", "Enter Gender")
                elif a2 == "":
                        tm.showinfo("Insert error", "Enter Age")
                elif a3 == "":
                        tm.showinfo("Insert error", "Enter Current Smoking")
                elif a4 == "":
                        tm.showinfo("Insert error", "Enter Cigarte per day")
                elif a5 == "":
                        tm.showinfo("Insert error", "Enter Do You have BP?")
                elif a6 == "":
                        tm.showinfo("Insert error", "Enter Do You have Stroke?")
                elif a7 == "":
                        tm.showinfo("Insert error", "Enter Do You have Hyper Tension?")
                elif a8 == "":
                        tm.showinfo("Insert error", "Enter Do You have Diabetics?")
                elif a9 == "":
                        tm.showinfo("Insert error", "Enter Cholatral")
                elif a10=="":
                        tm.showinfo("Insert error", "Enter Sys BP")
                elif a11 == "":
                        tm.showinfo("Insert error", "Enter Dia BP")
                elif a12 == "":
                        tm.showinfo("Insert error", "Enter BMI")
                elif a13 == "":
                        tm.showinfo("Insert error", "Enter Heart Rate")
                elif a14 == "":
                        tm.showinfo("Insert error", "Enter Gulcose Level")
                else:
                        print("a1==",a1)
                        print("a2==",a2)
                        print("a3==",a3)
                        print("a4==",a4)
                        print("a5==",a5)
                        print("a6==",a6)
                        print("a7==",a7)
                        print("a8==",a8)
                        print("a9==",a9)
                        print("a10==",a10)
                        print("a11==",a11)
                        print("a12==",a12)
                        print("a13==",a13)
                        print("a14==",a14)
                        res = pred.process(sym,float(a1),float(a2),float(a3),float(a4),float(a5),float(a6),float(a7),float(a8),float(a9),float(a10),float(a11),float(a12),float(a13),float(a14))
                        print(res)
                        if res!="":
                                tm.showinfo("Result", str(res))
                        else:
                                tm.showinfo("Input error", "Select Dataset File")
                        
                                

	

	clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=500, y=300)
	 
	proc = tk.Button(window, text="Random Forest", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	proc.place(x=100, y=600)
	

	LRbutton = tk.Button(window, text="LogisticRegression", command=LRprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	LRbutton.place(x=300, y=600)


	RFbutton = tk.Button(window, text="Decision Tree", command=DTProcess  ,fg=fgcolor   ,bg=bgcolor1 ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	RFbutton.place(x=500, y=600)

	SVMbutton = tk.Button(window, text="QMBC", command=CNNprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	SVMbutton.place(x=700, y=600)

	PRbutton = tk.Button(window, text="Predict", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=14  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	PRbutton.place(x=900, y=600)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=1100, y=600)

	window.mainloop()
Home()

