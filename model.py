from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

Base = declarative_base()


class ErrorCode(Base):
    __tablename__ = "error_code"

    id = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    desc = Column(String(100))
    upload_time = Column(DateTime)

    def __repr__(self):
        return "{},{},{},{}".format(
            self.id,
            self.upload_time,
            self.code,
            self.desc)
