def mondai1():#
    print("あいうえお")

def mondai2():#
    a=abs(1)
    b=bool(True)
    d=float(10.0)

def mondai3():#
    a=12
    b=34
    format(type(a+b))

def mondai4():#
    print('0~100までの得点(整数値)を入力してください。')
n=int(input('整数値:'))
if n>=80:
    print('合格です。')

def mondai6():#
    for i in range(10):
        print("forのプログラムです")

def mondai7():#
    x=1
    y=100
    z=0
    while x<=y:
        z+=x
        x+=1
        print("合計:",z)

def mondai14():#
    s=input("文字列：")
    for i in range(len(s)):
        print("s[{}]={}".format(i,s[i]))