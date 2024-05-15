# インポート
import sys

# 引数入力
args = sys.argv
# 変数初期化
count = int(args[1])

# 繰り返し
# 指定回数文字列を出力
for i in range(1, count+1):
    print("ひつじが{0}匹".format(i))

