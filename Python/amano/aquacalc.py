import sys
import datetime

# 引数入力
args = sys.argv
# 入園料設定(平日大人、平日子供、土日大人、土日子供
price = [2000, 1200, 2400, 1500]
# 合計金額初期化
total_price = 0

def calc(date, adult_people, child_people):
    # 曜日ごとの処理
    if date.weekday() != 5 and date.weekday() != 6:
        # 平日
        total_price += adult_people * price[0]
        total_price += child_people * price[1]
    else:
        # 土日
        total_price += adult_people * price[2]
        total_price += child_people * price[3]

    print(total_price)
    return

try:
    # 日付の取得
    date = datetime.datetime.strptime(args[1], '%Y%m%d')
    # 人数の取得
    adult_people = int(args[2])
    child_people = int(args[3])
    calc(date, adult_people, child_people)
except:
    print("YYYYMMDD 大人人数 子供人数 のフォーマットで入力してください")


# # 引数入力
# args = sys.argv
# # 入園料設定(平日大人、平日子供、土日大人、土日子供
# price = [2000, 1200, 2400, 1500]
# # 合計金額初期化
# total_price = 0

# # 日付の取得
# date = datetime.datetime.strptime(args[1], '%Y%m%d')
# # 人数の取得
# adult_people = int(args[2])
# child_people = int(args[3])
# # 曜日ごとの処理
# if date.weekday() != 5 and date.weekday() != 6:
#     # 平日
#     total_price += adult_people * price[0]
#     total_price += child_people * price[1]
# else:
#     # 土日
#     total_price += adult_people * price[2]
#     total_price += child_people * price[3]

# print(total_price, end="")