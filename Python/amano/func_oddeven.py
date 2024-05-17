# インポート
import sys

# 引数入力
args = sys.argv

def calcvalue(num):
    # 判定
    if int(num) % 2 == 0:
        print(num +"は偶数", end="")
    else:
        print(num +"は奇数", end="")
    return

for i in range(1, len(args), 1):
    calcvalue(args[i])


'''
def calcvalue(*num):
    # 判定
    for i in num:
        if int(i) %2 == 0:
            print("偶数", end="")
        else:
            print("奇数", end="")
        return 0

calcvalue(args)
'''
