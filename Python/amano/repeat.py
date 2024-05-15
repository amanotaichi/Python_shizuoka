# インポート
import sys

# 引数入力
args = sys.argv
# 変数初期化
num = int(args[1])
add = 0

# 繰り返し
# 計算
while 1:
    add += num
    # 判定
    # ちょど100
    if add == 100:
        print("Just 100!")
        break
    # 100以上
    elif add > 100:
        print("Over!")
        break
    # 100以下
    else:
        pass