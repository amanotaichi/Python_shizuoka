# 引数で渡した整数を、繰り返し足し算する
import sys
args = sys.argv[1]
num = int(args)
sum = 0

while (sum < 100):
    sum += num
    if (sum == 100):
        print("Just 100!", end="")
    elif (sum > 100):
        print("Over!", end="")
