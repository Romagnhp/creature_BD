import sqlalchemy
from row_patern import BaseClass, RowTable
from sqlalchemy.orm import Session
import pickle


bdEngine = sqlalchemy.create_engine("sqlite:///bot_BD.db")
bdConection = bdEngine.connect()

BaseClass.metadata.drop_all(bdEngine)
BaseClass.metadata.create_all(bdEngine)
     
with Session(bdEngine) as db:
    row_1 = RowTable(picture = "picture/IMG_2670.PNG", product_name = "Burger", pickUp_point = 'Dmitra Yavornitskogo avenue 50', price = 20, quantity = 5)
    db.add(row_1)
    db.commit()

    row_3 = RowTable(picture = "picture/IMG_2822.PNG", product_name = "French fries", pickUp_point = 'Dmitra Yavornitskogo avenue 51', price = 22, quantity = 7)
    db.add(row_3)
    db.commit()