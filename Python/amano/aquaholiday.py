import sys
import datetime
from databases import session
from tables import Holiday

# 引数入力
args = sys.argv
# 入園料設定(平日大人、平日子供、土日大人、土日子供
price = [2000, 1200, 2400, 1500]
# 合計金額初期化
total_price = 0
# 休日のリストをデータベースから持ってくる
holidaylist = session.query(Holiday).all()
# 休日リストの表示
for holiday in holidaylist:
    print(holiday.holi_date, holiday.holi_text)

# 日付の取得
date = datetime.datetime.strptime(args[1], '%Y%m%d')
# yyyymmdd timeからyyyymmddに変換
date = date.date()
# 人数の取得
adult_people = int(args[2])
child_people = int(args[3])
# 祝日のフラグ（1なら祝日、0なら平日土日
flag = 0

print(date)

# 祝日の判定
for holiday in holidaylist:
    if date == holiday.holi_date:
        print("祝日料金")
        total_price += adult_people * price[2]
        total_price += child_people * price[3]
        flag = 1
        break
    else:
        pass

# 土日の判定
if flag == 0:
    print("祝日ではない")
    if date.weekday() != 5 and date.weekday() != 6:
        # 平日
        print("平日料金")
        total_price += adult_people * price[0]
        total_price += child_people * price[1]
    else:
        # 土日
        print("土日料金")
        total_price += adult_people * price[2]
        total_price += child_people * price[3]

print(total_price)