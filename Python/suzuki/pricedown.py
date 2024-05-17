# 値下げした価格を出力
import sys
# 値下げ対象の種類を指定
kinds = sys.argv[1]
# 値下げ価格を指定
discount_price = int(sys.argv[2])

# 価格表を作成
price_dict = {
    "リンゴ": 80,
    "みかん": 198,
    "バナナ": 150,
    "ビール": 360,
    "日本酒": 580,
    "ラーメン": 380,
    "うどん": 128,
    "パスタ": 258
}

# 種類ごとの商品を定義した配列を作成
fruit = ["リンゴ", "みかん", "バナナ"]
alcohol = ["ビール", "日本酒"]
noodle = ["ラーメン", "うどん", "パスタ"]

# 種類で条件分岐し、値下げ
if (kinds == "果物類"):
    for i in fruit:
        price_dict[i] -= discount_price
        if (price_dict[i] < 1):
            price_dict[i] = 1
elif (kinds == "酒類"):
    for j in alcohol:
        price_dict[j] -= discount_price
        if (price_dict[j] < 1):
            price_dict[j] = 1
elif (kinds == "麺類"):
    for k in noodle:
        price_dict[k] -= discount_price
        if (price_dict[k] < 1):
            price_dict[k] = 1
else:
    pass

print(price_dict, end="")
