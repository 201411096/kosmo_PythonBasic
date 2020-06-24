# tkinter는 Lightweight GUI 모듈
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from dao.buyList import *

price = {'제품1': 1500, '제품2': 2000, '제품3': 1000, '제품4': 500, '제품5': 300, '제품6': 4500,'제품7': 900, '제품8': 600, '제품9': 300}
orderList = {}
sum = 0     # 총 금액

def add(item):
    global sum
    global orderList
    this_price = price.get(item)
    sum += this_price
    if item in orderList.keys():
        orderList[item] = int(orderList[item])+1
    else:
        orderList[item] = 1
    orderList = dict(sorted(orderList.items()))
    textarea.delete('1.0', END)
    for product in orderList.keys():
        tempLine = str(product) + " : " + str(orderList[product]) + '개 ' + str(int(orderList[product])*int(price[product])) + "원 \n";
        textarea.insert(tk.INSERT, tempLine)
    label1['text'] = "금액: " + str(sum) + "원"
def order():
    global sum
    buyList.insert_buyList(sum, orderList, price)
    orderList.clear()
    textarea.delete('1.0', END)
    sum = 0
    label1['text'] = "금액: 0원"

def btn_exit():
    msgbox = tk.messagebox.askquestion('확인', '주문을 마치시겠습니까?')
    if msgbox == 'yes':
        exit()

def btn_clear():
    global sum
    sum = 0
    orderList.clear()
    textarea.delete('1.0', END)
    label1['text'] = "금액: 0원"

def btn_orderList():
    textarea2.delete('1.0', END)
    textarea2.insert(tk.INSERT, buyList.select_buyList())

window = tk.Tk()    # 화면을 띄움
window.title("음료 주문")
window.geometry("1500x800+350+100")  #화면 크기 설정
window.resizable(False, False)

# 윈도우 안에 있는 프레임 형성, 프레임에 버튼 나열을 위한 프레임 형성)
topframe = tk.Frame(window, width=1100, height=50)
topframe.pack(side=TOP)
frame0 = tk.Frame(window, width=1100, height=700)
frame0.pack()
frame1 = tk.Frame(frame0, width=850, height=700)
frame1.pack(side=LEFT)
frame2 = tk.Frame(frame0, width=250, height=700)
frame2.pack(side=RIGHT)

frame2_bottom = tk.Frame(frame2, width=250, height=10)
frame2_bottom.pack(side=BOTTOM)


#버튼 이미지

#img1 = PhotoImage(file ="../image/image.png")
img1 = PhotoImage(file ="../image/1.png")
img2 = PhotoImage(file ="../image/2.png")
img3 = PhotoImage(file ="../image/3.png")
img4 = PhotoImage(file ="../image/4.png")
img5 = PhotoImage(file ="../image/5.png")
img6 = PhotoImage(file ="../image/6.png")
img7 = PhotoImage(file ="../image/7.png")
img8 = PhotoImage(file ="../image/8.png")
img9 = PhotoImage(file ="../image/9.png")

# 프레임 안에 버튼 들 배열
tk.Button(frame1, text='제품1', image=img1, command=lambda: add('제품1'), width=200, height=200).grid(row=0, column=0)
tk.Button(frame1, text='제품2', image=img2, command=lambda: add('제품2'), width=200, height=200).grid(row=0, column=1)
tk.Button(frame1, text='제품3', image=img3, command=lambda: add('제품3'), width=200, height=200).grid(row=0, column=2)
tk.Button(frame1, text='제품4', image=img4, command=lambda: add('제품4'), width=200, height=200).grid(row=1, column=0)
tk.Button(frame1, text='제품5', image=img5, command=lambda: add('제품5'), width=200, height=200).grid(row=1, column=1)
tk.Button(frame1, text='제품6', image=img6, command=lambda: add('제품6'), width=200, height=200).grid(row=1, column=2)
tk.Button(frame1, text='제품7', image=img7, command=lambda: add('제품7'), width=200, height=200).grid(row=2, column=0)
tk.Button(frame1, text='제품8', image=img8, command=lambda: add('제품8'), width=200, height=200).grid(row=2, column=1)
tk.Button(frame1, text='제품9', image=img9, command=lambda: add('제품9'), width=200, height=200).grid(row=2, column=2)




# 선택한 메뉴를 나열하는 textarea 형성
textarea = tk.Text(frame2, width=100, height=20)
textarea.pack()

# 매출 목록을 나열하는 textarea 형성
textarea2 = tk.Text(frame2, width=100, height=20)
textarea2.pack()

# 총금액이 표시되는 label 추가
label1 = tk.Label(frame2, text="금액: 0원", width=20, height=2, fg='blue')
label1.pack()

orderCancelButton = tk.Button(frame2_bottom, command=lambda: btn_clear(), text="주문초기화", width=15, height=2)
orderCancelButton.grid(row=0, column=0)

orderButton = tk.Button(frame2_bottom, command=lambda: order(), text="결제", width=15, height=2)
orderButton.grid(row=0, column=1)

orderListButton = tk.Button(frame2_bottom, command=lambda: btn_orderList(), text="매출 목록", width=15, height=2)
orderListButton.grid(row=0, column=2)

exitButton = tk.Button(frame2_bottom, command=lambda: btn_exit(), text="주문종료하기", width=15, height=2)
exitButton.grid(row=0, column=3)




window.mainloop()   # .mainloop(): 이벤트 메시지 루프로서 키보드나 마우스 혹은 화면 Redraw와 같은 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역활을 한다.