from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from configuration import CONNECTION_ROW_DB


Model = declarative_base(name='Model')

engine = create_engine(
    CONNECTION_ROW_DB
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)

session = Session()
