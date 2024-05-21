import datetime
import sys

date = sys.argv[1]
adult_number = sys.argv[2]
children_number = sys.argv[3]

# 引数で渡した日付をstr型からdate型に変換する関数を定義
def get_day_of_week(date):
    # 日付（str型）を1文字ごとの配列にする
    date_list = list(date)
    # 日付の年の部分のみを取り出す
    year_str_list = date_list[0:4]
    # list型からstr型に変換
    year = int("".join(year_str_list))
    month_str_list = date_list[4:6]
    month = int("".join(month_str_list))
    day_str_list = date_list[6:8]
    day = int("".join(day_str_list))

    # str型からdate型に変換
    attend_date = datetime.date(year, month, day)
    # 日付から曜日番号を取得
    day_of_week = attend_date.strftime("%w")
    return day_of_week


# 入園料を計算する関数を定義
def aqua_calc(date, adult_num, children_num):
    # 日付から曜日を取得するget_day_of_week関数で曜日を取得
    day_of_week = get_day_of_week(date)
    # 日曜: 0, 土曜: 6であれば土日料金
    if ((int(day_of_week) == 0)
        or (int(day_of_week == 6))):
        adult_fee = 2400 * adult_num
        childrem_fee = 1500 * children_num
    else:
        adult_fee = 2000 * adult_num
        childrem_fee = 1200 * children_num
    
    sum_fee = adult_fee + childrem_fee
    return sum_fee

try:
    sum_fee = aqua_calc(date, int(adult_number), int(children_number))
    print(sum_fee, end="")
except ValueError:
    print("日付または人数の入力が不正です。やり直してください。")
