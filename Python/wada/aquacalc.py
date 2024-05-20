import sys
args = sys.argv

import datetime

#引数を変数に代入
visiting_date = datetime.datetime.strptime(args[1], '%Y%m%d')
adult_number = int(args[2])
child_number = int(args[3])

#入園料を計算して表示する関数
def calc_entrancefee(visiting_date,adult_number,child_number):
    weekday = int(visiting_date.strftime("%w"))
    
    #平日
    if 1 <= weekday <= 5: 
        entrancefee = (adult_number*2000 + child_number*1200)

    #休日
    else:
        entrancefee = (adult_number*2400+ child_number*1500)
    print(entrancefee,end="")

calc_entrancefee(visiting_date,adult_number,child_number)