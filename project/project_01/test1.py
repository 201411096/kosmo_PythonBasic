# 윈도우 테스트
from tkinter import *
from vo.product import *

if __name__ == "__main__":
    print("메인 테스트")
    root = Tk()
    lbl = Label(root, text="이름")
    lbl.pack()

    txt = Entry(root)
    txt.pack()
    root.mainloop()
