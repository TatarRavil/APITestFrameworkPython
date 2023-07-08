from sqlalchemy import Integer, Boolean, String, Column

from database.db import Model


class Films(Model):
    __tablename__ = 'films'

    film_id = Column(Integer, primary_key=True)
    status = Column(String, index=True)
    title = Column(String)
    is_premiere = Column(Boolean)
