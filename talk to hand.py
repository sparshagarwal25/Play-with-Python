from tkinter import *
parent=Tk()
name=Label(parent,text='name').grid(row=0,column=0)
a1=Entry(parent).grid(row=0,column=1)
password=Label(parent,text="password").grid(row=1,column=0)
a2=Entry(parent).grid(row=1,column=1)
roll=Label(parent,text='Roll no').grid(row=2,column=0)
a3=Entry(parent).grid(row=2,column=1)
branch=Label(parent,text='Branch').grid(row=3,column=0)
a4=Entry(parent).grid(row=3,column=1)
submit=Button(parent,text="submit").grid(row=4,column=1)
parent.mainloop()
