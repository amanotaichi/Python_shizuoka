#インポート
import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#入力内容(引数)を変数に代入
num = int(args[1])
#num分繰り返し
for i in range(num):
    f = open('sheep.txt', 'a' , encoding='UTF-8')
    f.write(f"ひつじが{i+1}匹\n")
    f.close
    