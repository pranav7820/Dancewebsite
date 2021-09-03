from tkinter import Button, Canvas, Checkbutton, Entry, Frame, Label, NoDefaultRoot, Radiobutton, StringVar, Tk,ttk,IntVar
from tkinter.constants import EXTENDED
win=Tk()
win.title("whatsup")
win.iconbitmap("icon.ico")
win.minsize(width=600,height=300)
win.maxsize(width=600,height=300)

Canvs=Canvas(win)
cord=10,20,80,210
Canvs.create_arc(cord,start=0,extent=170,fill="green")
canvs.create_line(cord)


Canvs.pack()



win.mainloop()