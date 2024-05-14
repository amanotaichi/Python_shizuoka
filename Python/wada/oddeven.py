import sys
arg = sys.argv

#引数を変数に代入
num = int(arg[1])

#余りが0なら偶数、それ以外なら奇数を判定
if num % 2 == 0:
    print("偶数",end="")
else:
    print("奇数",end="")