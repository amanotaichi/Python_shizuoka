from database import session
from attendnum import AttendNum
import datetime
import sys

date = sys.argv[1]
adult_number = int(sys.argv[2])
children_number = int(sys.argv[3])

# AttendNumテーブルを取得
aqua_attend_list = session.query(AttendNum).all()
# 引数をstr型からdate型に変換
attend_date = datetime.datetime.strptime(date, '%Y%m%d')
# YYYYMMDD形式に変換
attend_date = attend_date.date()

# 連番を保存する変数seq_numを初期化
seq_num = 1
# for文でAttendNum内に同じ日付がいくつあるか確認
# 日付が一致した分だけ、seq_numを1追加する
for aquanum in aqua_attend_list:
    if (attend_date == aquanum.entry_date):
        seq_num += 1

# AttendNumに追加
aqua_attend = AttendNum(
    entry_date = attend_date,
    seq = seq_num,
    adult = adult_number,
    child = children_number
)

session.add(aqua_attend)
session.commit()