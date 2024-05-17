# 給与から税金を差し引き、支給額を求める関数を定義
from decimal import Decimal, ROUND_HALF_UP

def calc_salary(salary):
    if (salary > 1000000):
        # 100万円を超過した部分を取り出す
        over_milion = salary - 1000000
        # 税額の計算
        tax = over_milion * 0.2 + 100000
    else:
        # 税額の計算
        tax = salary * 0.1
    tax = Decimal(tax).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    payment = salary - tax
    return payment, tax