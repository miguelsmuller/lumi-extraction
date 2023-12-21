from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()
metadata = MetaData()

class DataBaseManager:
    def __init__(self):
        self.__conn_string = "postgresql+psycopg2://postgres:root@localhost/lumi"
        self.__engine = self.__create_db_engine()

        if not database_exists(self.__engine.url):
            create_database(self.__engine.url)
            
        self.session = None
        
    def __create_db_engine(self):
        engine = create_engine(self.__conn_string)
        Base.metadata.bind = engine
        return engine
    
    @property
    def get_engine(self):
        return self.__engine 
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
