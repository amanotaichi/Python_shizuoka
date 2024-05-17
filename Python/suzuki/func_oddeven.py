# 複数の整数の奇数・偶数を判定
import sys
# 3つの整数を定義
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

# 引数の整数の奇数・偶数判定する関数を定義
def calcValue(l, m, n):
    # 引数をすべてリストに入れる
    num_list = [l, m, n]
    # ループを回してそれぞれ奇数・偶数判定する
    for i in num_list:
        if (i%2 == 0):
            print(f"{str(i)}は偶数")
        else:
            print(f"{str(i)}は奇数")

calcValue(num1, num2, num3)