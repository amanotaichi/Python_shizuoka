from Python_shizuoka.Python.sugiyama.python_aqua.database import session
from Python_shizuoka.Python.sugiyama.python_aqua.tables import Holiday

holidaylist = session.query(Holiday).all()

for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)