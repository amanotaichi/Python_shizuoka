import sys

# 引数入力
args = sys.argv

# 初期化
cate = args[1]
priced = int(args[2])
price = {
    "リンゴ":80 ,
    "みかん":198,
    "バナナ":150,
    "ビール":360,
    "日本酒":580,
    "ラーメン":380,
    "うどん":128,
    "パスタ":258
}

fruits = ["リンゴ", "みかん", "バナナ"]
alcohol = ["ビール", "日本酒"]
noodles = ["ラーメン", "うどん", "パスタ"]

# 値下げ処理
if cate == "果物類":
    for i in fruits:
        price[i] = price[i] - priced

elif cate == "酒類":
    for i in alcohol:
        price[i] = price[i] - priced

elif cate == "麺類":
    for i in noodles:
        price[i] = price[i] - priced

for i in price:
    if price[i] <= 0:
        price[i] = 1

print(price)