import sys
arg = sys.argv

#引数を変数に代入
start = str(arg[1])
end = str(arg[2])
#駅名をキーに距離を値にしてタプル作成
nozomi = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}
nozomi_key = list(nozomi.keys())
start_pos = nozomi_key.index(start)
end_pos = nozomi_key.index(end)
nozomi_value = list(nozomi.values())
#駅名別の距離をそれぞれ取り出す
dis1 = nozomi_value[start_pos]
dis2 = nozomi_value[end_pos]
#距離の算出
dis = abs(dis2 - dis1)
dis = round(dis,2)
#結果の表示
print(dis, end="")
