from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SERVER = "you server"
PORT = 5432
USER = "your name"
PASS = "your password"
DBNAME = "data_process"


class DBClient():
    def __init__(self, base):
        db_string = "postgres://{}:{}@{}:{}/{}".format(
            USER, PASS, SERVER, PORT, DBNAME)
        self.engine = create_engine(db_string)
        base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def show_tables(self):
        result_set = self.engine.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
        for r in result_set:
            print(r)

    def show_records(self, model):
        results = self.session.query(model).all()
        for r in results:
            print(r)
