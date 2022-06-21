from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta, engine

categories = Table ("categories", meta, 
Column("id", Integer, primary_key=True),
Column("ref", Integer),
Column("name", String(250)))

meta.create_all(engine)


