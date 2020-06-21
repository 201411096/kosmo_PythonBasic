from tkinter import *
from vo.product import *

root = Tk()
image = PhotoImage(file=("../../image/unnamed.png"))
label = Label(root, image=image)
label.pack()
root.mainloop()

