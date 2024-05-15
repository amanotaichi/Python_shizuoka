#インポート
import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#入力内容(引数)を変数に代入
sal = int(args[1])
#税額の計算
if 1000000 < sal:
    #100万の10%である10万に100万を超える額×20%を足す
    tax = 100000 + (sal-1000000) * 0.2
else:
    #100万以下はそのまま10%を算出
    tax = sal * 0.1
#税額を四捨五入する
tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
#支給額は給与から税額を引く
pay = sal - tax
#str型に変換
tax = (str(tax))
pay = (str(pay))
#結果の表示
print("支給額:" + pay + "、" + "税額:" + tax, end="")