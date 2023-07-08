from database.db import session

from database import tables


result = session.query(tables.Films.film_id, tables.Films.title).all()
result1 = session.query(tables.Films.film_id).first()
result2 = session.query(tables.Films.film_id).one_or_none()

result3 = session.query(
    tables.Films.film_id, tables.Films.title
    ).filter(tables.Films.film_id > 100, tables.Films.film_id < 150)
