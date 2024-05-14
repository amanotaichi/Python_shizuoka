# 遊園地の入場料を計算
# 人数の入力
children = int(input("子供料金(13才未満)は何人 ? "))
normal = int(input("通常料金(13~64才)は何人 ? "))
elder = int(input("年配者料金(65才以上)は何人 ? "))

# 集計
total_num = children + normal + elder
children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price

# 割引対象か確認
if total_num >= 10:
    print("団体割引があります")
    total_price *= 0.8
else:
    print("割引はありません")

# 結果を表示
print(f"子供料金  :{children}人x 500= {children_price}円")
print(f"通常料金  :{normal}人x 1000= {normal_price}円")
print(f"年配者料金  :{elder}人x 700= {elder_price}円")
print(f"合計: {total_num}人 {total_price}円")