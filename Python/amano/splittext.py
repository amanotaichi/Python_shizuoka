import sys

# 引数入力
args = sys.argv

cat = args[1].split()

print(cat[int(args[2]) - 1])