def calcsalary(salary):
    
    #四捨五入のモジュールをインポート
    from decimal import Decimal, ROUND_HALF_UP

    #税額の計算
    #100万円より大きいときの計算
    if salary > 1000000:
        tax = 100000 + (salary-1000000)*0.2
    #100万円以下のときの計算
    else:
        tax = salary*0.1

    #taxを四捨五入
    tax = Decimal(int(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

    #支給額を計算
    price = salary - tax

    return price ,tax

#支給額と税額を表示
# print("支給額:"+str(price)+"、税額:"+str(tax),end="")
    