#import
import sys
args = sys.argv
from datetime import datetime as dt

#料金表定義
#平日料金表
week_price = {
    "adult" : 2000,
    "child" : 1200
}
#週末料金表
weekend_price = {
    "adult" : 2400,
    "child" : 1500   
}
#入力内容整理
input_date = args[1]
adult = int(args[2])
child = int(args[3])

#料金
adt = dt.strptime(orgstr, '%Y%m%d')
day = adt.strftime('%a')
if day == "Sat" or "sun":



print(day)

"""

#メイン関数
def main():
    orgstr = args[1]
    date = orgstr[:4] + ',' + orgstr[4:6] + ',' + orgstr[6:]

    print(type(date))
    dt = datetime(date)
    print(dt.strftime('%B'))
    week  = date.strftime('%a')
    adult = int(args[2]) #
    child = int(args[3]) #
    print(date)


if __name__ == '__main__':
    main()
"""