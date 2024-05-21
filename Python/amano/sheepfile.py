import sys

# 引数入力
args = sys.argv
# 変数初期化
count = int(args[1])

# ファイルパス指定
path = "other/sheep.txt"
# ファイルオープン
f = open(path, "w")

# 繰り返し
# 指定回数文字列を出力
for i in range(1, count+1):
    f.write("ひつじが{0}匹\n".format(i))

f.close()