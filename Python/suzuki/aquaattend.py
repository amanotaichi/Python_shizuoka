from database import session
from attendnum import AttendNum
import datetime
import sys

date = sys.argv[1]
adult_number = int(sys.argv[2])
children_number = int(sys.argv[3])

aqua_attend_list = session.query(AttendNum).all()
attend_date = datetime.datetime.strptime(date, '%Y%m%d')
attend_date = attend_date.date()

seq_num = 1
for aquanum in aqua_attend_list:
    if (attend_date == aquanum.entry_date):
        seq_num += 1

aqua_attend = AttendNum(
    entry_date = attend_date,
    seq = seq_num,
    adult = adult_number,
    child = children_number
)

session.add(aqua_attend)
session.commit()