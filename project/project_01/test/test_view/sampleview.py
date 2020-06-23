# tkinter는 Lightweight GUI 모듈
import tkinter as tk
from tkinter import messagebox
from tkinter import *

price = {'coffee': 3500, 'latte': 4000, 'smoothie': 4500, 'tea': 3000}
order = []  #주문 리스트
sum = 0     # 총 금액

def add(item):
    global sum  #전역 변수 사용을 위해 global 이용

    if item not in price:
        print("no drink")
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    textarea.insert(tk.INSERT, item+" \n")
    label1['text'] = "금액: " + str(sum) + "원"

def btn_exit():
    msgbox = tk.messagebox.askquestion('확인', '주문을 마치시겠습니까?')
    if msgbox == 'yes':
        exit()

window = tk.Tk()    # 화면을 띄움
window.title("음료 주문")
window.geometry("1200x800+350+100")  #화면 크기 설정
window.resizable(False, False)

# 윈도우 안에 있는 프레임 형성, 프레임에 버튼 나열을 위한 프레임 형성)
topframe=tk.Frame(window, width=1100, height=50)
topframe.pack(side=TOP)
frame0 = tk.Frame(window, width=1100, height=700)
frame0.pack()
frame1 = tk.Frame(frame0, width=850, height=700)
frame1.pack(side=LEFT)

frame2 = tk.Frame(frame0, width=250, height=700)
frame2.pack(side=RIGHT)

# 프레임 안에 버튼 들 배열
tk.Button(frame1, text='coffee', command=lambda: add('coffee'), width=30, height=15).grid(row=0, column=0)
tk.Button(frame1, text='latte', command=lambda: add('latte'), width=30, height=15).grid(row=0, column=1)
tk.Button(frame1, text='smoothie', command=lambda: add('smoothie'), width=30, height=15).grid(row=0, column=2)
tk.Button(frame1, text='tea', command=lambda: add('tea'), width=30, height=15).grid(row=1, column=0)
tk.Button(frame1, text='coffee', command=lambda: add('coffee'), width=30, height=15).grid(row=1, column=1)
tk.Button(frame1, text='latte', command=lambda: add('latte'), width=30, height=15).grid(row=1, column=2)
tk.Button(frame1, text='smoothie', command=lambda: add('smoothie'), width=30, height=15).grid(row=2, column=0)
tk.Button(frame1, text='tea', command=lambda: add('tea'), width=30, height=15).grid(row=2, column=1)
tk.Button(frame1, text='tea', command=lambda: add('tea'), width=30, height=15).grid(row=2, column=2)


# 선택한 메뉴를 나열하는 textarea 형성
textarea = tk.Text(frame2, width=70, height=33)
textarea.pack()

# 총금액이 표시되는 label 추가
label1 = tk.Label(frame2, text="금액: 0원", width=20, height=2, fg='blue')
label1.pack()



window.mainloop()   # .mainloop(): 이벤트 메시지 루프로서 키보드나 마우스 혹은 화면 Redraw와 같은 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역활을 한다.