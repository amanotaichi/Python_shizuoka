# インポート
import sys

# 引数入力
args = sys.argv
# 判定
if int(args[1])%2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")