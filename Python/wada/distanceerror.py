import sys
arg = sys.argv

#引数を変数に代入
i = str(arg[1])
j = str(arg[2])

#辞書を定義
nozomi = {
    "東京":0.00, 
    "品川":6.78, 
    "新横浜":25.54, 
    "名古屋":342.02, 
    "京都":476.31, 
    "新大阪":515.35
    }

#第2引数と第3引数に設定した駅間の距離を計算し出力（小数第2位まで出力）
#エラーメッセージを表示
try:
    distance = round(abs(nozomi[i]-nozomi[j]),2)
    print(distance,end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")
