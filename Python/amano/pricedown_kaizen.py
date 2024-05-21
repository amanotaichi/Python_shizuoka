import sys

# 引数入力
args = sys.argv
try:
    # 値下げする商品名と値段を代入
    cate = args[1]
    priced = int(args[2])
except:
    print("引数が足りません")
    exit()

# 初期化
# 商品名と値段の辞書を作成
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
# カテゴリのリストを作成
fruits = ["リンゴ", "みかん", "バナナ"]
alcohol = ["ビール", "日本酒"]
noodles = ["ラーメン", "うどん", "パスタ"]

# 値下げ処理
# カテゴリ別値下げ処理
if cate == "果物類":
    for i in fruits:
        price[i] -= priced
elif cate == "酒類":
    for i in alcohol:
        price[i] -= priced
elif cate == "麺類":
    for i in noodles:
        price[i] -= priced
else:
    print("存在しない商品カテゴリです")
    exit()

# 値下げ後価格が0以下の場合に価格を１円にする
for i in price:
    if price[i] <= 0:
        price[i] = 1

# 値下げ後の辞書型を表示
print(price)