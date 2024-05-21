# 準備
import sys
args = sys.argv

#SELECT
from database import session
from tables import Holiday

#平日/休日import
import datetime

holidaylist = session.query(Holiday).all()

#引数入力
day      = datetime.datetime.strptime(args[1], '%Y%m%d')
adult    = int(args[2])
children = int(args[3])

#条件分岐/平日or休日
if day.strftime("%w") == 1 or day.strftime("%w") == 6:
    entrancefee = (adult*2400+ children*1500)

else:  
    aqua_holiday = session.query(Holiday.holi_date).filter_by(holi_date=day).first()
    if aqua_holiday is None:
        entrancefee = (adult*2000+ children*1200)

    else:
        entrancefee = (adult*2400+ children*1500)

print(entrancefee)