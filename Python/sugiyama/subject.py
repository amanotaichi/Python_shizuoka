# テストだ～い
# 準備
import sys
args = sys.argv

# program

# 変数に代入
Sugaku = int(args[1])
Kokugo = int(args[2])
Eigo   = int(args[3])

# もしもボックス
if (Sugaku >= 70 and Kokugo >= 70 and Eigo >= 70) or (Sugaku + Kokugo + Eigo >= 220):
    if (Sugaku >= 50 and Kokugo >= 50 and Eigo >= 50):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")