# 値下げした価格を出力
import sys
# 値下げ対象の種類を指定
kinds = sys.argv[1]
# 値下げ価格を指定
discount_price = int(sys.argv[2])

# 価格表を作成
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

# 種類ごとの商品を定義した配列を作成
fruits = ["リンゴ", "みかん", "バナナ"]
alcohol = ["ビール", "日本酒"]
noodle = ["ラーメン", "うどん", "パスタ"]

# 種類で条件分岐し、値下げ
if (kinds == "果物類"):
    for i in fruits:
        hinmoku[i] -= discount_price
        if (hinmoku[i] < 1):
            hinmoku[i] = 1
elif (kinds == "酒類"):
    for j in alcohol:
        hinmoku[j] -= discount_price
        if (hinmoku[j] < 1):
            hinmoku[j] = 1
elif (kinds == "麺類"):
    for k in noodle:
        hinmoku[k] -= discount_price
        if (hinmoku[k] < 1):
            hinmoku[k] = 1
else:
    pass

print(hinmoku, end="")