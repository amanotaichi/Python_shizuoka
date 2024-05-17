import datetime
import sys

date = sys.argv[1]
adult_number = sys.argv[2]
children_number = sys.argv[3]

def aqua_cacl(date, adult_num, chlidren_num):
    # 日付をstr型からdate型に変換
    date_list = list(date)
    year_str_list = date_list[0:4]
    year = int("".join(year_str_list))
    month_str_list = date_list[4:6]
    month = int("".join(month_str_list))
    day_str_list = date_list[6:8]
    day = int("".join(day_str_list))

    visit_date = datetime.date(year, month, day)
    day_of_week = visit_date.strftime("%w")

    if (
        int(day_of_week) == 0 
        or int(day_of_week) == 6):
        adult_fee = 2400 * adult_num
        childrem_fee = 1500 * chlidren_num
    else:
        adult_fee = 2000 * adult_num
        childrem_fee = 1200 * chlidren_num
    
    return adult_fee+childrem_fee

try:
    sum = aqua_cacl(date, int(adult_number), int(children_number))
    print(sum, end="")
except:
    print("指定の形式で入力してください")
