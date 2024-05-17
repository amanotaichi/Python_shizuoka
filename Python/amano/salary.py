# インポート
from decimal import Decimal, ROUND_HALF_UP
import sys

# 引数入力
args = sys.argv
# 変数代入・初期化
under_hundred = 0.1
over_hundred = 0.2
result_salary = 0
tax = 0

# 税額計算
if int(args[1]) <= 1000000:
    tax = int(args[1]) * under_hundred
else:
    tax = ((int(args[1]) - 1000000) * over_hundred) + (1000000 * under_hundred)
# 税額整数化
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
# 支給額計算
result_salary = int(args[1]) - tax
# 表示
print("支給額:{0}、税額:{1}".format(result_salary,tax))