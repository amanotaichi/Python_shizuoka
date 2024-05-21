from database import session
from tables import Holiday

import sys
args = sys.argv

from datetime import date

#引数を変数に代入
visiting_date = args[1]
adult_number = int(args[2])
child_number = int(args[3])

dt = date(int(visiting_date[0:4]), int(visiting_date[4:6]), int(visiting_date[6:8]))

#土日
if dt.strftime("%w") == 1 or dt.strftime("%w") == 6 :
    payment = adult_number *2400 + child_number *1500
#平日or祝日
else:
    public_hoiday = session.query(Holiday.holi_date).filter_by(holi_date = dt).first()
    if public_hoiday is None:
        payment = adult_number *2000 + child_number *1200
    else:      
        payment = adult_number *2400+ child_number *1500

print(payment, end="")
