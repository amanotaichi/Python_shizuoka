children = int(input("子供料金は何人？"))
normal = int(input("通常料金は何人？"))
elder = int(input("年配者料金は何人？"))

total_num = children + normal + elder
children_price = children*500
normal_price = normal*1000
elder_price = elder*700
total_price = children_price + normal_price + elder_price

if total_num >= 10:
    print("団体料金があります")
    total_price = total_price*0.8
else:
    print("割引はありません")

print("子供料金  :{0}人x 500= {1}円".format(children,children_price))
print("通常料金  :{0}人x1000= {1}円".format(normal,normal_price))
print("年配者料金:{0}人x 700= {1}円".format(elder,elder_price))
print("合計: {0}人 {1}円".format(total_num,total_price))
