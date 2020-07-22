from tkinter import *
import tkinter as tk

from tkinter.ttk import *
from ttkthemes import ThemedStyle
import numpy as np 
import math
def tan(x):
  
        if radiovar.get():
                values=float(x)
                
        else:
                values=math.radians(x)

        values= math.tan(values)
        if values>=16331239353195370.0:
                return math.inf
        return values
def cos (x):
        if radiovar.get():
                val=float(x)
        else:
                val=math.radians(x)
        return math.cos(val)
def sin(x):
        if radiovar.get():
                val=float(x)
        else:
                val=math.radians(x)
        return math.sin(val)
def cot(x):
        
        if radiovar.get():
                val=float(x)
        else:
                val=math.radians(x)
        values= math.tan(val)
        if values>=16331239353195370.0:
                return math.inf
        return values

def cos_s():
        try:        
           expression=float(text_var.get())
           text_var.set(f'cos({expression})')
        except:
            text_var.set('only numeric allowed')

def sin_s():
        try:        
           expression=float(text_var.get())
           text_var.set(f'sin({expression})')
        except:
            text_var.set('only numeric allowed')

def tan_s():
        try:        
           expression=float(text_var.get())
           text_var.set(f'tan({expression})')
        except:
            text_var.set('only numeric allowed')

def cot_s():
        try:        
           expression=float(text_var.get())
           text_var.set(f'cot({expression})')
        except:
            text_var.set('only numeric allowed')

def clear():
    text_var.set("")
def square(y):
        return y**2
def pow(x,y):
        return x**y
def sqrt(y):
        return y**(0.5)
def percent(y,z):
        return (y/z)*100

def action(item):
    
    expression=text_var.get()+str(item)
    text_var.set(expression)
def equals():
     try:
        
        expression=text_var.get()
        result=float(eval(expression))
        if result>=16331239353195370.0:
                text_var.set(math.inf)
        else: 
                text_var.set(result)
    
     except ZeroDivisionError :
             text_var.set("can't divide by zero")
    
     
     except:
             text_var.set("invalid operation")
def sqr_root():
    
        try:
            
           expression=float(text_var.get())
           text_var.set(f"sqrt({expression})")
        except :
            text_var.set('only numeric allowed')
        
        
        
def backspace():
    expression=text_var.get()
    text_var.set(expression[:-1])   

def power():
 try:
    expression=float(text_var.get())
    
    expression=str(f'pow({expression},power )')
    text_var.set(expression)
 except:
     text_var.set('only numeric values allowed')
def square_show():
    try:
        expression=float(text_var.get())
        text_var.set(f"square({expression})")
    except:
        text_var.set('only numeric values allowed')
def percentage():
  try:
    expression=float(text_var.get())
    expression=str(f"percent({expression},principal)")

    text_var.set(expression)
  except:
      text_var.set('only numeric values allowed')

root=Tk()
wid=6
from platform import system
if system()=='Linux':
        # root.geometry("310x436")
        theme='scidgreen'
        
        
        
elif system()=='Windows':
        theme='scidgreen'
        # root.geometry("240x380")
        wid=7
root.resizable(0,0)
ThemedStyle(root).set_theme(theme)
root.title("calculator")
text_var=StringVar()


#creating frame for entry
radiovar=IntVar()
radiovar.set(1)


ent_frame=Frame(root)
entry=tk.Entry(ent_frame,width=37,textvariable=text_var,cursor="hand1",highlightcolor='green',highlightbackground='green',justify='right',bd=10)
ent_frame.pack()

entry.bind("<Return>",lambda event: equals())
entry.bind("<Delete>",lambda event:clear())

entry.pack(ipady=15,pady=10)
radioframe=Frame(root)
radioframe.pack()
degre= Radiobutton(radioframe, text='deg.', variable =radiovar , value=0)
radian=Radiobutton(radioframe ,text='rad.', variable=radiovar,value=1) 
degre.grid(row=0,column=0)
radian.grid(row=0,column=1)



#frame just below button 
btn_frame=Frame(root)

btn_clear=Button(btn_frame,width=16,text="c",cursor="hand2",command=clear)


btn_bkspce=Button(btn_frame,width=wid,text="bksp", cursor="hand2",command= backspace)

#buttons
btn_divide=Button(btn_frame,width=wid,text="/",cursor="hand2",command=lambda : action("/"))
btn_1=Button(btn_frame,width=wid,text="1",cursor="hand2",command=lambda : action("1"))
btn_2=Button(btn_frame,width=wid,text="2",cursor="hand2",command=lambda : action("2"))
btn_3=Button(btn_frame,width=wid,text="3",cursor="hand2",command=lambda : action("3"))


btn_4=Button(btn_frame,width=wid,text="4",cursor="hand2",command=lambda : action("4"))
btn_5=Button(btn_frame,width=wid,text="5",cursor="hand2",command=lambda : action("5"))
btn_6=Button(btn_frame,width=wid,text="6",cursor="hand2",command=lambda : action("6"))

btn_7=Button(btn_frame,width=wid,text="7",cursor="hand2",command=lambda : action("7"))
btn_8=Button(btn_frame,width=wid,text="8",cursor="hand2",command=lambda : action("8"))
btn_9=Button(btn_frame,width=wid,text="9",cursor="hand2",command=lambda : action("9"))


btn_mult=Button(btn_frame,width=wid,text="*",cursor="hand2",command=lambda : action("*"))
btn_add=Button(btn_frame,width=wid,text="+",cursor="hand2",command=lambda : action("+"))
btn_subs=Button(btn_frame,width=wid,text="-",cursor="hand2",command=lambda : action("-"))


btn_0=Button(btn_frame,width=16,text="0",cursor="hand2",command=lambda : action("0"))
btn_dot=Button(btn_frame,width=wid,text=".",cursor="hand2",command=lambda : action("."))
btn_eqlas=Button(btn_frame,width=wid,text="=", cursor="hand2",command=equals)

btn_sqrt=Button(btn_frame,width=wid,text="sqrt",cursor="hand2",command=sqr_root)
btn_square=Button(btn_frame,width=wid,text="sqr",cursor="hand2",command=square_show)
btn_power=Button(btn_frame,width=wid,text="pow",cursor="hand2",command=power)
btn_per=Button(btn_frame,width=wid,text="%",cursor="hand2",command=percentage)

btn_cos=Button(btn_frame,width=wid,text="cos",cursor="hand2",command=cos_s)
btn_sin=Button(btn_frame,width=wid,text="sin",cursor="hand2",command=sin_s)
btn_tan=Button(btn_frame,width=wid,text="tan",cursor="hand2",command=tan_s)
btn_cot=Button(btn_frame,width=wid,text="cot",cursor="hand2",command=cot_s)




#packing it with grid method

btn_clear.grid(row=1,column=1,ipadx=13,ipady=13,columnspan=2)
btn_divide.grid(row=1,column=4,ipadx=13,ipady=13)
btn_bkspce.grid(row=1,column=3,ipadx=13,ipady=13)


btn_7.grid(row=2,column=1,ipadx=13,ipady=13)
btn_8.grid(row=2,column=2,ipadx=13,ipady=13)
btn_9.grid(row=2,column=3,ipadx=13,ipady=13)
btn_mult.grid(row=2,column=4,ipadx=13,ipady=13)

btn_4.grid(row=3,column=1,ipadx=13,ipady=13)
btn_5.grid(row=3,column=2,ipadx=13,ipady=13)
btn_6.grid(row=3,column=3,ipadx=13,ipady=13)
btn_subs.grid(row=3,column=4,ipadx=13,ipady=13)

btn_1.grid(row=4,column=1,ipadx=13,ipady=13)
btn_2.grid(row=4,column=2,ipadx=13,ipady=13)
btn_3.grid(row=4,column=3,ipadx=13,ipady=13)
btn_add.grid(row=4,column=4,ipadx=13,ipady=13)


btn_eqlas.grid(row=5,column=4,ipadx=13,ipady=13)
btn_0.grid(row=5,column=1,ipadx=13,ipady=13 ,columnspan=2)
btn_dot.grid(row=5,column=3,ipadx=13,ipady=13)

btn_square.grid(row=6,column=1,ipadx=13,ipady=13)
btn_sqrt.grid(row=6,column=2,ipadx=13,ipady=13)
btn_power.grid(row=6,column=4,ipadx=13,ipady=13)
btn_per.grid(row=6,column=3,ipadx=13,ipady=13)

btn_cos.grid(row=7,column=1,ipadx=13,ipady=13)
btn_sin.grid(row=7,column=2,ipadx=13,ipady=13)
btn_tan.grid(row=7,column=3,ipadx=13,ipady=13)
btn_cot.grid(row=7,column=4,ipadx=13,ipady=13)

btn_frame.pack(ipady=2)

root.mainloop()



