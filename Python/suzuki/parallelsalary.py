# 複数の給与の支払い額を計算
from func_salary import calc_salary
import sys

input_salary = sys.argv
input_salary.pop(0)

for i in input_salary:
    payment, tax = calc_salary(int(i))
    print(f"支給額:{payment}、税額:{tax}")
