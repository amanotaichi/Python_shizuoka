# インポート
import sys
from decimal import Decimal, ROUND_HALF_UP

# 引数入力
args = sys.argv
# 初期化
nozomi = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪": 515.35
}
station_space = 0

# 計算
if nozomi[args[1]] < nozomi[args[2]]:
    station_space = nozomi[args[2]] - nozomi[args[1]]
else:
    station_space = nozomi[args[1]] - nozomi[args[2]]

# 四捨五入
station_space = Decimal(float(station_space)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)

# 出力
print(station_space, end="")