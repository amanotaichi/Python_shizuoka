# #準備
# import sys
# args = sys.argv

# #第二引数
# item = args[2]

# #第三引数
# markdown = int(args[3])

# #辞書設定
# # 初期値 {'リンゴ':80, 'みかん':198, 'バナナ':150, 'ビール':360,'日本酒':580, 'ラーメン':380,'うどん':128, 'パスタ':258}
# fruits = ('リンゴ':80, 'みかん':198, 'バナナ':150)
# alcohol = ('ビール':360, '日本酒':580)
# noodles = ('ラーメン':380,'うどん':128, 'パスタ':258)

# #条件分岐


# #出力
# print(price_table)

import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く

#条件分岐
if hm_class == '果物類':
    for fruit in fruits:
        hinmoku[fruit] = hinmoku[fruit] - price_down

elif hm_class == '酒類':
    for osake in alcohol:
        hinmoku[osake] = hinmoku[osake] - price_down
elif hm_class == '麺類':
    for noodle in noodles:
        hinmoku[noodle] = hinmoku[noodle] - price_down


for fruit in fruits:
    if hinmoku[fruit] < 1:
        hinmoku[fruit] = 1

for osake in alcohol:
    if hinmoku[osake] < 1:
        hinmoku[osake] = 1

for noodle in noodles:
    if hinmoku[noodle] < 1:
        hinmoku[noodle] = 1

#出力
print(hinmoku)
        