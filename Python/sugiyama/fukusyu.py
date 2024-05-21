# 準備
import sys
args = sys.argv

#代入
sheep = int(args[1])

#変数定義
total = 1

#while分
while sheep >= total:
    print("ひつじが" + str(total) + "匹")
    total += 1
else:
    pass