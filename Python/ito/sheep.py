#インポート
import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#入力内容(引数)を変数に代入
num = int(args[1])
#num分繰り返し
for i in range(num):
    print(f"ひつじが{i+1}匹")