#import
from table_aqua import aqua
from datetime import date
from database import session
import sys
args = sys.argv

#引数から日付の格納処理
def input2date(input_date):
    return date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))
    
#連番処理
def seq():
    aqua_list = session.query(aqua).all()
    return len(aqua_list)

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

#メイン関数
def main():
    #引数取得
    input_date = str(args[1])
    adult = int(args[2])
    child = int(args[3])
    #date型へ変換
    dt = input2date(input_date)
    #連番取得
    num = seq()
    #挿入
    insert(dt,num,adult,child)

if __name__ == '__main__':
    main()