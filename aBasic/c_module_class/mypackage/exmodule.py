# exmodule.py

def sum(a, b):
    if type(a) != type(b):
        print("자료형이 다르면 계산이 안됩니다.")
        return
    else:
        return a+b