import sys
arg = sys.argv

#引数を変数に代入
i = int(arg[1])

total = 0

#100まで計算
while total < 100:
    total += i

#合計が100のときの出力
if total == 100:
    print("Just 100!",end="")
#合計が100を超えるときの出力
else:
    print("Over!",end="") 