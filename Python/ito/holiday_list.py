from database import session
from tables import Holiday

holiday_list = session.query(Holiday).all()
for holiday in holiday_list:
    print(holiday.holi_date)
    print(holiday.holi_text)
