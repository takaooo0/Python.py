print("長方形を描写します。")
print("2~20までの整数値を入力して下さい。")
n=int(input("行数の入力:"))
m=int(input("列数の入力:"))

for i in range(n):
    for j in range(m):
        print("*", end="")
    print()
else:
    print("値が正しくありません。")    