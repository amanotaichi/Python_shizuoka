from aquacalc import aqua_cacl
from database import session
from tables import Holiday
import datetime
import sys

# Holidayテーブルから祝日を取得
holidaylist = session.query(Holiday).all()
# for holidays in holidaylist:
#     print(holidays.holi_date,holidays.holi_text) 

date = sys.argv[1]
adult_number = sys.argv[2]
children_number = sys.argv[3]

def aqua_holi(date, adult_num, children_num):
    # 日付をstr型からdate型に変換
    date_list = list(date)
    year_str_list = date_list[0:4]
    year = int("".join(year_str_list))
    month_str_list = date_list[4:6]
    month = int("".join(month_str_list))
    day_str_list = date_list[6:8]
    day = int("".join(day_str_list))
    visit_date = datetime.date(year, month, day)

    adult_fee = 0
    children_fee = 0
    sum = 0
    for holiday in holidaylist:
        if visit_date == holiday.holi_date:
            adult_fee = 2400 * int(adult_num)
            children_fee = 1500 * int(children_num)
            sum = adult_fee + children_fee
    if (adult_fee == 0 and children_fee ==0):
        sum = aqua_cacl(date, int(adult_num), int(children_num))
    return sum

sum = aqua_holi(date, adult_number, children_number)
print(sum)
