from tkinter import Button, Checkbutton, Entry,Frame, Grid, Label, Listbox, NoDefaultRoot, Radiobutton, StringVar, Tk,ttk,IntVar
from tkinter.constants import ACTIVE, ANCHOR, END
import tkinter as tk
win=tk.Tk()
win.title("whatsup")
win.iconbitmap("icon.ico")
win.minsize(width=1010,height=250)
win.maxsize(width=1010,height=250)


var=tk.StringVar()
ent=ttk.Entry(win,state="readonly",textvariable=var)
ent.grid(rowspan=1,columnspan=100,ipadx=999,ipady=20)

win.configure(bg="pink")

q=ttk.Button(win,text="Q",width=6,command=lambda : press('q'))
q.grid(row=1,column=0,ipadx=3,ipady=5)

w=ttk.Button(win,text="w",width=6,command=lambda : press('w'))
w.grid(row=1,column=1,ipadx=3,ipady=10)

e=ttk.Button(win,text="e",width=6,command=lambda : press('e'))
e.grid(row=1,column=2,ipadx=3,ipady=10)

r=ttk.Button(win,text="R",width=6,command=lambda : press('r'))
r.grid(row=1,column=3,ipadx=3,ipady=10)

t=ttk.Button(win,text="T",width=6,command=lambda : press('t'))
t.grid(row=1,column=4,ipadx=3,ipady=10)

y=ttk.Button(win,text="Y",width=6,command=lambda : press('y'))
y.grid(row=1,column=5,ipadx=3,ipady=10)

u=ttk.Button(win,text="U",width=6,command=lambda : press('u'))
u.grid(row=1,column=6,ipadx=3,ipady=10)

i=ttk.Button(win,text="I",width=6,command=lambda : press('i'))
i.grid(row=1,column=7,ipadx=3,ipady=10)

o=ttk.Button(win,text="O",width=6,command=lambda : press('o'))
o.grid(row=1,column=8,ipadx=3,ipady=10)

p=ttk.Button(win,text="P",width=6,command=lambda : press('p'))
p.grid(row=1,column=9,ipadx=3,ipady=10)

p=ttk.Button(win,text="{",width=6,command=lambda : press('p'))
p.grid(row=1,column=10,ipadx=3,ipady=10)
p=ttk.Button(win,text="}",width=6,command=lambda : press('p'))
p.grid(row=1,column=11,ipadx=3,ipady=10)
p=ttk.Button(win,text="\\",width=6,command=lambda : press('p'))
p.grid(row=1,column=12,ipadx=3,ipady=10)
p=ttk.Button(win,text="Clear",command=lambda : press('p'))
p.grid(row=1,column=13,ipadx=20,ipady=10)








a=ttk.Button(win,text="A",command=lambda : press('a'))
a.grid(row=2,column=0,ipadx=6,ipady=10)
s=ttk.Button(win,text="S",command=lambda : press('s'))
s.grid(row=2,column=1,ipadx=6,ipady=10)
d=ttk.Button(win,text="D",command=lambda : press('d'))
d.grid(row=2,column=2,ipadx=6,ipady=10)
f=ttk.Button(win,text="F",command=lambda : press('f'))
f.grid(row=2,column=3,ipadx=6,ipady=10)
g=ttk.Button(win,text="G",command=lambda : press('g'))
g.grid(row=2,column=4,ipadx=6,ipady=10)
h=ttk.Button(win,text="H",command=lambda : press('h'))
h.grid(row=2,column=5,ipadx=6,ipady=10)
j=ttk.Button(win,text="J",command=lambda : press('j'))
j.grid(row=2,column=6,ipadx=6,ipady=10)
k=ttk.Button(win,text="K",command=lambda : press('k'))
k.grid(row=2,column=6,ipadx=6,ipady=10)
l=ttk.Button(win,text="L",command=lambda : press('l'))
l.grid(row=2,column=6,ipadx=6,ipady=10)
z=ttk.Button(win,text="Z",command=lambda : press('z'))
z.grid(row=3,column=0,ipadx=6,ipady=10)
x=ttk.Button(win,text="X",command=lambda : press('x'))
x.grid(row=3,column=1,ipadx=6,ipady=10)
c=ttk.Button(win,text="C",command=lambda : press('c'))
c.grid(row=3,column=2,ipadx=6,ipady=10)
v=ttk.Button(win,text="V",command=lambda : press('v'))
v.grid(row=3,column=3,ipadx=6,ipady=10)
b=ttk.Button(win,text="B",command=lambda : press('b'))
b.grid(row=3,column=4,ipadx=6,ipady=10)
n=ttk.Button(win,text="N",command=lambda : press('n'))
n.grid(row=3,column=5,ipadx=6,ipady=10)
m=ttk.Button(win,text="M",command=lambda : press('m'))
m.grid(row=3,column=6,ipadx=6,ipady=10)

win.mainloop()