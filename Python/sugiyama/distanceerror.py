# 準備
import sys
args = sys.argv

# 引数設定
station1 = args[1]
station2 = args[2]

# 辞書
distance_dict = {'東京':0.00,
                 '品川':6.78,
                 '新横浜':25.54,
                 '名古屋':342.02,
                 '京都':476.31,
                 '新大阪':515.35
                 }
try:
    # 計算 abs()は計算式や数値の絶対値で出力
    answer = abs(distance_dict[station2] - distance_dict[station1])
    # 四捨五入
    answer = round(answer,2)
    # 出力
    print(answer, end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")