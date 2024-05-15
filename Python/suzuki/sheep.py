# 引数で渡した整数の回数分繰り返し羊を数える
import sys

num = int(sys.argv[1])
for i in range(num):
    print(f"ひつじが{i+1}匹")
