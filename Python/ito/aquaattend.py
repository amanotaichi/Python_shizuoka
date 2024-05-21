#import
from table_aqua import aqua
from datetime import date
from database import session
from tables import Holiday
import sys
args = sys.argv

#引数から日付の格納処理
def input2date(input_date):
    dt = date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))
    return dt

#連番処理
def seq():
    aqua_list = session.query(aqua).all()
    num = len(aqua_list)
    return num

#INSERT処理
def insert(dt,num,adult,child):
    new_data = aqua(
        entry_date = dt,
        seq = num,
        adult = adult,
        child = child
    )
    session.add(new_data)
    session.commit()

def main():
    #引数を変数に代入
    input_date = args[1]
    adult = int(args[2])
    child = int(args[3])
    dt = input2date(input_date)
    num = seq()
    insert(dt,num,adult,child)

if __name__ == '__main__':
    main()