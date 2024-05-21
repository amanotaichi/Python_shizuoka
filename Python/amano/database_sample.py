from databases import session
from tables import Holiday

holidaylist = session.query(Holiday).all()

# holidaylist = session.query(holiday.holi_date).filter_by(holi_text = '建国記念日').all()

for holiday in holidaylist:
    print(holiday.holi_date, holiday.holi_text)

