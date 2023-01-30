from sqlalchemy.orm import declarative_base
from sqlalchemy import BLOB,FLOAT,TEXT, INTEGER, Column, ForeignKey
from sqlalchemy.orm import relationship

BaseClass = declarative_base()

class RowTableProducts(BaseClass):
    __tablename__ = 'products'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    picture = Column(TEXT)
    product_name = Column(TEXT)
    pickUp_point = Column(TEXT)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

class RowTableUsers(BaseClass):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    first_name = Column(TEXT)
    last_name = Column(TEXT)
    mail = Column(TEXT)
    card_naumber = Column(INTEGER)

class RowTableOrders(BaseClass):    
    __tablename__ = 'orders'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    id_products = Column(INTEGER, ForeignKey('products.id', ondelete='CASCADE'),)
    id_users = Column(INTEGER, ForeignKey('users.id', ondelete='CASCADE'),)

    # user = relationship('Users', backref='orders')