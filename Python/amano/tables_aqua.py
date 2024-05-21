import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from databases import Base
from databases import ENGINE

#テーブル：attendnumの定義
class Attendnum(Base):
    __tablename__ = 'attendnum'
    entry_date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', int, primary_key = True)
    adult = Column('adult', int)
    child = Column('child', int)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)