# 給与から税金を差し引き、支給額を求める
import sys
args = sys.argv

# 給与を入力
salary = int(args[1])

# 給与が100万以上かそうでないかで条件分岐
if (salary > 1000000):
    # 100万円を超過した部分を取り出す
    over_milion = salary - 1000000
    # 税額の計算
    tax = over_milion * 0.2 + 100000
else:
    # 税額の計算
    tax = salary * 0.1

payment = salary - tax
print(f"支給額:{int(payment)}、税額:{int(tax)}", end="")