import gspread
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


DeclarativeBase = declarative_base()

engine = create_engine("postgresql+psycopg2://root:postgres@localhost/dod", echo=True)
DeclarativeBase.metadata.create_all(engine)


class first_table(DeclarativeBase):
    __tablename__ = "first"

    id = Column(Integer, primary_key=True)
    first_first = Column('first_first', String)
    first_second = Column('first_second', String)


class second_table(DeclarativeBase):
    __tablename__ = "first"

    second_first = Column('second_first', String)
    second_second = Column('second_second', String)
    second_third = Column('second_third', String)


Session = sessionmaker(bind=engine)
session = Session()


def parce_into_db():
    gc = gspread.service_account(filename='DODQuest.json')
    sh = gc.open_by_key('1c2OEBIDEJIBGbxLN8DmX1hMGfku2W9FD9iTlObm51Aw')

    script_worksheet = sh.worksheet("script")
    buttons_worksheet = sh.worksheet("button")

    script_columns_values = script_worksheet.get('A:B')
    buttons_columns_values = buttons_worksheet.get('A:C')

    for item in script_columns_values:
        first_t = first_table(first_first=item[0], first_second=item[1])
        session.add(first_t)

    for item in buttons_columns_values:
        second_t = second_table(second_first=item[0], second_second=item[1], second_third=item[2])
        session.add(second_t)


parce_into_db()
