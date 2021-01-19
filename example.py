# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import create_engine
from model import Base, ErrorCode

import pandas

from client import DBClient
from datetime import datetime


def init_db():
    client = DBClient(Base)
    Base.metadata.create_all(client.engine)


def insert_db(data_frame):
    client = DBClient(Base)
    Base.metadata.bind = client.engine

    # DB Session
    for i, r in data_frame.iterrows():
        new_error_code = ErrorCode(
            code=r["错误码"],
            desc=r["错误描述"],
            upload_time=datetime.strptime(r["上报时间"], "%Y-%m-%d %H:%M:%S")
        )
        client.session.add(new_error_code)

    client.session.commit()


def show_db():
    client = DBClient(Base)
    client.show_records(ErrorCode)


if __name__ == "__main__":
    init_db()
    data_frame = pandas.read_csv("error_code.csv")
    insert_db(data_frame)
    show_db()
