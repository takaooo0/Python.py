print('0~100までの得点(整数値)を2つ入力してください。')
n=int(input('1つ目の得点:'))
m=int(input('2つ目の得点:'))
if n>=80 or m>=80:
    print('合格です')
else:
    print('不合格です')    