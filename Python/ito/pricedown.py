import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]          #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
if hm_class == "果物類":
    hm_class = ("リンゴ", "みかん", "バナナ")
elif hm_class == "酒類":
    hm_class = ("ビール", "日本酒")  
elif hm_class == "麺類":
    hm_class = ("ラーメン", "うどん", "パスタ")

for i in hm_class:
    price = hinmoku[i]
    if hinmoku[i] < price_down:
        hinmoku[i] = 1
    else:
        hinmoku[i] = price-price_down

print(hinmoku, end="")




