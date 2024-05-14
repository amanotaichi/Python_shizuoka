# 奇数偶数判定
# 準備
import sys
args = sys.argv

# 数字入力
number = int(args[1])

# 条件分岐
if number % 2 == 0:
    print("入力された値は偶数です。", end="")
else:
    print("入力された数字は奇数です。", end="")