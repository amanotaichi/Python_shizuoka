import sys
import collections
num = int(sys.argv[1])

prime_factor = []
# 入力した整数、numの回数ループを回す
for i in range(1, num, 1):
    if (num % i == 0):
        # 素数は1と自身を含まないので除外
        if (i != 1 and i != num):
            # 素因数を求めるため、さらにループを回す
            # iを割った余りが0となるものを数える
            count = 0
            for j in range(1, i, 1):
                if (i % j == 0):
                    count += 1
                    if (count == 2):
                        prime_factor.append(j)
prime_factor = list(sorted(set(prime_factor)))
print(prime_factor, end="")