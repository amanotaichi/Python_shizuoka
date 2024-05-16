# 準備
import sys
args = sys.argv

# 引数設定
Rank = int(args[1])

# タプル定義
Kuni = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# そのまま引数を持ってくると、インデックスの1から先しか持ってこれない
print(Kuni[Rank-1], end="")