# 人数の入力
child = int(input("子供(13歳未満)の人数は？"))
normal = int(input("大人(13-64歳)の人数は？"))
elder = int(input("年配者(65歳以上)の人数は？"))
# 集計
total = child + normal + elder
child_price = child * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = child_price + normal_price + elder_price
# 割引対象か確認
if total >= 10:
    print("団体割引があります")
    total_price = total_price * 0.8
else:
    print("割引はありません")
# 結果表示
print("子供料金 :{0}人× 500= {1}円".format(child, child_price))
print("大人料金 :{0}人× 1000= {1}円".format(normal, normal_price))
print("年配者料金 :{0}人× 700= {1}円".format(elder, elder_price))
print("合計金額 :{0}人 {1}円".format(total, total_price))
print