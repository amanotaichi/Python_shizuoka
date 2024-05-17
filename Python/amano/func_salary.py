from decimal import Decimal, ROUND_HALF_UP

def calcsalary(under_hundred, over_hundred, salary):
    result_salary = 0
    tax = 0
    # 税額計算
    if int(salary) <= 1000000:
        tax = int(salary) * under_hundred
    else:
        tax = ((int(salary) - 1000000) * over_hundred) + (1000000 * under_hundred)
    # 税額整数化
    tax = Decimal(tax).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    # 支給額計算
    result_salary = int(salary) - tax

    return result_salary, tax