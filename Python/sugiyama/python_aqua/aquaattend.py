# 準備
import sys
args = sys.argv

#SELECT
from database import session
from attendnum import Attend

#平日/休日import
import datetime

attend_list = session.query(Attend).all()

#引数入力
day      = datetime.datetime.strptime(args[1], '%Y%m%d')
day      = day.date()
adult    = int(args[2])
children = int(args[3])

#seqを1にする
seq = 1

#databaseを回す
for attend_f in attend_list:
    if day == attend_f.entry_date:
        seq = seq + 1
    else:
        seq = seq


#登録するデータ
attend = Attend(
    entry_date = day,
    seq        = seq,
    adult      = adult,
    child      = children
)

#INSERT処理
session.add(attend)

#コミット
session.commit()
