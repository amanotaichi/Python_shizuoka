# 準備
import sys
args = sys.argv

# 代入
sheep = int(args[1])

# 変数の定義
total = 0

# for文
for i in range(0, sheep):
    if sheep >= total:
        total = total + 1
        print("ひつじが" + str(total) + "匹")
    else:
        break
