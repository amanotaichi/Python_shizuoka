import sys
from decimal import Decimal, ROUND_HALF_UP

# 1つ目の駅を入力
first_station = sys.argv[1]
# 2つ目の駅を入力
second_station = sys.argv[2]

# 引数に指定した駅間の距離を計算する関数を定義
def calc_distance(station1, station2):
    # 東京駅からの距離を定義した辞書を作成
    nozomi = {
        "東京": 0.00,
        "品川": 6.78,
        "新横浜": 25.54,
        "名古屋": 342.02,
        "京都": 476.31,
        "新大阪": 515.35
    }
    # 距離の数値を絶対値で取得
    distance = abs(nozomi[station2] - nozomi[station1])

    # 小数第2位で四捨五入
    distance = Decimal(str(distance)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return distance

# 例外処理
try:
    distance = calc_distance(first_station, second_station)
    print(distance, end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
