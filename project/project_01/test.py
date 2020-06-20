from tkinter import *

if __name__ == "__main__":
    print("메인 테스트")
    root = Tk()
    lbl = Label(root, text="이름")
    lbl.pack()

    txt = Entry(root)
    txt.pack()
    root.mainloop()
