import sys
args = sys.argv

#引数を変数に代入
i = int(args[1])
j = int(args[2])
k = int(args[3])

numbers = [i,j,k]

# リストで代入する方法
# numbers = [int(arg) for arg in args[1:]]

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

for num in numbers:
    calcvalue(num)