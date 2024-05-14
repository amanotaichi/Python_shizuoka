#インポート
import sys
args = sys.argv

#引数を変数に代入
math = int(args[1])
jap = int(args[2])
eng = int(args[3])
#判定用変数用意
total = math + jap + eng
#判定
if (70 <= math <= jap <= eng ) or 220 <= total:
    if 50 <= math <= jap <= eng:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")