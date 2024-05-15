# インポート
import sys

# 引数入力
args = sys.argv
# 変数初期化
animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# リストに挿入
animal.insert(int(args[1]), args[2])
# 要素削除
del animal[-1]
# ソート
animal.sort(key=str)
# 出力
print(animal)