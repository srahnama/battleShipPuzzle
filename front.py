from tkinter import *
import battleShip
window = Tk()
window.title("BattleShipPuzzle")
window.geometry('400x200') 
lbl = Label(window, text="BattleShipPuzzle", font=("Arial Bold", 15)).grid(column=1,row=0)
tt=Label(window, text="Size (NXN):",font=("Arial",10)).grid(column=0,row=2)
ttt=Label(window, text="Row[2,5,0,...]:",font=("Arial", 10)).grid(column=0,row=3)
tttt=Label(window, text="Column[2,5,3,...]:",font=("Arial", 10)).grid(column=0,row=4)
ttttt=Label(window, text="Population Size:",font=("Arial", 10)).grid(column=0,row=5)
tttttt=Label(window, text="mutation 0-100:",font=("Arial", 10)).grid(column=0,row=6)
txt = Entry(window,width=30)
txt.grid(column=1, row=2)
    
txt1 = Entry(window,width=30)
txt1.grid(column=1, row=3)


txt2 = Entry(window,width=30)
txt2.grid(column=1, row=4)


txt3 = Entry(window,width=30)
txt3.grid(column=1, row=5)

 

txt4 = Entry(window,width=30)
txt4.grid(column=1, row=6)
  
import ast
def clicked():
       #handle
    n=int(txt.get())
    row=ast.literal_eval(txt1.get())
    col=ast.literal_eval(txt2.get())
    p=int(txt3.get())
    m=int(txt4.get())
    battleShip.main(n,row,col,p,m) 
        
btn = Button(window, text="Start", command=clicked)
     
btn.grid(column=1, row=7)


import sys
import os


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

btn1= Button(window, text="Restart", command=restart_program)
btn1.grid(column=0, row=7)
window.mainloop()