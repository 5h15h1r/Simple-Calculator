from tkinter import *

root=Tk()
root.title("Calculator")
root.wait_visibility(root)
root.wm_attributes('-alpha',0.8)
root.iconphoto(True, PhotoImage(file="calculator.png"))

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0 , column=0,columnspan=3, padx=10, pady=10)



def button_click(num):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(num))


def button_clear():
    e.delete(0,END)

def button_add():
    first_no=e.get()
    global f_no
    global math
    math="addition"
    f_no=int(first_no)
    e.delete(0,END)


def button_substract():
     first_no=e.get()
     global f_no
     global math
     math="substraction"
     f_no=int(first_no)
     e.delete(0,END)

def button_multiply():
     first_no=e.get()
     global f_no
     global math
     math="multiplication"
     f_no=int(first_no)
     e.delete(0,END)

def button_divide():
     first_no=e.get()
     global f_no
     global math
     math="division"
     f_no=int(first_no)
     e.delete(0,END)


def button_equals():
     second_no=e.get()
     e.delete(0,END)

     if math=="addition":
        e.insert(0,f_no + int(second_no))

     if math=="substraction":
        e.insert(0,f_no - int(second_no))

     if math=="multiplication":
        e.insert(0,f_no * int(second_no))

     if math=="division":
        e.insert(0,f_no // int(second_no))


#making buttons for calc
butt1=Button(root ,text="1", padx=40 ,pady=20,command=lambda: button_click(1))
butt2=Button(root ,text="2", padx=40 ,pady=20,command=lambda: button_click(2))
butt3=Button(root ,text="3", padx=40 ,pady=20,command=lambda: button_click(3))
butt4=Button(root ,text="4", padx=40 ,pady=20,command=lambda: button_click(4))
butt5=Button(root ,text="5", padx=40 ,pady=20,command=lambda: button_click(5))
butt6=Button(root ,text="6", padx=40 ,pady=20,command=lambda: button_click(6))
butt7=Button(root ,text="7", padx=40 ,pady=20,command=lambda: button_click(7))
butt8=Button(root ,text="8", padx=40 ,pady=20,command=lambda: button_click(8))
butt9=Button(root ,text="9", padx=40 ,pady=20,command=lambda: button_click(9))
butt0=Button(root ,text="0", padx=40 ,pady=20,command=lambda: button_click(0))
butt_add=Button(root, text="+", padx=39,pady=20,command=button_add)
butt_clear=Button(root,text="C",padx=92,pady=20,command=lambda:button_clear())
butt_equals=Button(root,text="=",padx=91,pady=20,command=button_equals)
butt_substract=Button(root,text="-",padx=41 ,pady=20,command=button_substract)
butt_multiply=Button(root,text="x",padx=40,pady=20,command=button_multiply)
butt_divide=Button(root,text="/",padx=42,pady=20,command=button_divide)



butt1.grid(row=3,column=0)
butt2.grid(row=3,column=1)
butt3.grid(row=3,column=2)

butt4.grid(row=2,column=0)
butt5.grid(row=2,column=1)
butt6.grid(row=2,column=2)

butt7.grid(row=1,column=0)
butt8.grid(row=1,column=1)
butt9.grid(row=1,column=2)

butt0.grid(row=4,column=0)
butt_clear.grid(row=4,column=1,columnspan=2)
butt_equals.grid(row=5,column=1,columnspan=2)
butt_add.grid(row=5,column=0)

butt_substract.grid(row=6,column=0)
butt_multiply.grid(row=6,column=1)
butt_divide.grid(row=6,column=2)

root.mainloop()