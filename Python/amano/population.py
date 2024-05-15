# インポート
import sys

# 引数入力
args = sys.argv
# 初期化
rank = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
# 表示
print(rank[int(args[1]) - 1])