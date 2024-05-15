#給与計算演習
# 事前準備
from decimal import Decimal, ROUND_HALF_UP

import sys
args = sys.argv

# 引数設定
Money = int(args[1])

# program
# if
if Money < 1000000:
    tax_amount = Money * 0.1
else:
    tax_amount = int(Money * 0.2) + 100000

# 四捨五入
tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)

pay_amount = Money - tax_amount

print(f"支給額: {pay_amount}円、税額: {tax_amount}円",end="")