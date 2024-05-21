import sys
import datetime
from databases import session
from tables_aqua import Attendnum

# 引数入力
args = sys.argv

# 日付の取得
date = datetime.datetime.strptime(args[1], '%Y%m%d')
# yyyymmdd timeからyyyymmddに変換
date = date.date()
# 人数の取得
adult_people = int(args[2])
child_people = int(args[3])
# 連番
r_num = 1

# リストをデータベースから持ってくる
attendnum = session.query(Attendnum).all()
# # リストの表示
# for attend in attendnum:
#     print(attend.entry_date, attend.seq, attend.adult, attend.child)

# 連番の判定
for attend in attendnum:
    if date == attend.entry_date:
        r_num += 1
    else:
        pass

# データベースに登録
attendnum = Attendnum(
    entry_date = date,
    seq = r_num,
    adult = adult_people,
    child = child_people
)
# insert処理
session.add(attendnum)
# commit処理
session.commit()
