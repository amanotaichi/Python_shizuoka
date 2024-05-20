# インポート
import sys
from decimal import Decimal, ROUND_HALF_UP
from func_salary import calcsalary

# 引数入力
args = sys.argv
# 変数初期化
under_hundred = 0.1
over_hundred = 0.2

for i in range(1, len(args), 1):
    result_salary = calcsalary(under_hundred, over_hundred, int(args[i]))

    # 表示
    print("支給額:{0}、税額:{1}".format(result_salary[0],result_salary[1]))