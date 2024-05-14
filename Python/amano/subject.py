# インポート
import sys

# 引数入力
args = sys.argv
# 変数初期化
math = 0
jap = 0
eng = 0
score_total = 0
# 点数代入
math = int(args[1])
jap = int(args[2])
eng = int(args[3])
score_total += math + jap + eng

# 判定
if math >= 50 and jap >= 50 and eng >= 50:
    if math >= 70 and jap >= 70 and eng >= 70:
        print("合格", end="")
    elif score_total >= 220:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")


'''
if math >= 70 and jap >= 70 and eng >= 70:
    if math >= 50 and jap >= 50 and eng >= 50:
        print("合格", end="")
    else:
        print("不合格", end="")
elif score_total >= 220:
    if math >= 50 and jap >= 50 and eng >= 50:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")
'''