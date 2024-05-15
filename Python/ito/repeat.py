#インポート
import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#入力内容(引数)を変数に代入
num = int(args[1])
result = 0
#合計が100以上になるまで繰り返し
while result < 100:
    result += num
if result == 100:
    #合計が100の時の表示
    print("Just 100!",end="")
else:
    #合計が100を超えているときの表示
    print("Over!",end="")

