from datetime import date
from database import session
from tables import Holiday
#import datetime    #モジュールごとのimportする記述
import sys
args = sys.argv

#引数を変数に代入
input_date = args[1]
adult = int(args[2])
child = int(args[3])

#引数から日付の格納
dt = date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))
print(dt)
#dt = datetime.date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))　#from無しの場合の記述方法

#土日は、大人2,400円、子供1,500円
#祝日データ取得
a = 0
holiday_list = session.query(Holiday).all()
for holiday in holiday_list:
    if dt == holiday.holi_date:
        a = 1

if dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun" :
    a = 1

#平日は、大人2,000円、子供1,200円
if a == 1:
    pay = 2400 * adult + 1500 * child
else:
    pay = 2000 * adult + 1200 * child

#合計金額の出力
print(pay)
