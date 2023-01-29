from sqlalchemy.orm import declarative_base
from sqlalchemy import BLOB,FLOAT,TEXT, INTEGER, Column

BaseClass = declarative_base()

class RowTable(BaseClass):
    __tablename__ = 'products'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    picture = Column(TEXT)
    product_name = Column(TEXT)
    pickUp_point = Column(TEXT)
    price = Column(FLOAT)
    quantity = Column(INTEGER)