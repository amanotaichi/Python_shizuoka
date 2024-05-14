# 奇数・偶数判定
import sys
args = sys.argv
num = int(args[1])

# numを2で割った余りが0かそうでないかで条件分岐
if (num % 2 == 0):
    print("偶数", end="")
else:
    print("奇数", end="")