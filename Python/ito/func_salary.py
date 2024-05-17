from decimal import Decimal, ROUND_HALF_UP
def calcsalary(i):
    if 1000000 < i:
        #100万の10%である10万に100万を超える額×20%を足す
        tax = 100000 + (i-1000000) * 0.2
    else:
        #100万以下はそのまま10%を算出
        tax = i * 0.1
    #税額を四捨五入する
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    #支給額は給与から税額を引く
    pay = i - tax
    #str型に変換
    tax = (str(tax))
    pay = (str(pay))
    return pay, tax
