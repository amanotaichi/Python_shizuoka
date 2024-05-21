from database import session
from tables import attendnum

import sys
args = sys.argv

from datetime import date

visiting_date = args[1]
adult_number = int(args[2])
child_number = int(args[3])

dt = date(int(visiting_date[0:4]), int(visiting_date[4:6]), int(visiting_date[6:8]))

get = session.query(attendnum).filter_by(entry_date = dt).order_by(attendnum.seq.desc()).first()

if get != None:
    seq = get.seq + 1
else:
    seq = 1

attendnum = attendnum(
    entry_date = dt, 
    seq = seq, 
    adult = adult_number, 
    child = child_number
)

session.add(attendnum)

session.commit()
