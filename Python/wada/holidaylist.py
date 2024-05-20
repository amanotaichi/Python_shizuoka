from database import session
from tables import Holiday

holidaylist = session.query(Holiday).all()

for holidays in holidaylist:
    print(holidays.holi_date,holidays.holi_text) 