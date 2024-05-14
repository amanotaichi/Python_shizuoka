import sys

# 標準入力
args = sys.argv
# 変数初期化
sum = 0
# 計算
sum += int(args[1]) + int(args[2]) + int(args[3])
# 出力
print(sum, end="")