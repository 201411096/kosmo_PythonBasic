from tkinter import *
from vo.product import *
class ProductListWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("ProductListFrame")
        self.window.geometry("640x400+400+400")
        self.makeProductList()
        print("생성자 함수 호출 확인")
        self.window.mainloop()
    def makeProductList(self):
        productList = Product.select_product()
        for product in productList:
            tempLabel = Label(self.window, text=product.name)
            tempLabel.pack()

productListWindow = ProductListWindow()