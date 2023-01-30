import sqlalchemy
from table_patern import BaseClass, RowTableProducts, RowTableUsers
from sqlalchemy.orm import Session

class Creature_bd:
    bdEngine = sqlalchemy.create_engine("sqlite:///bot_BD.db")
    bdConection = bdEngine.connect()

    BaseClass.metadata.drop_all(bdEngine)
    BaseClass.metadata.create_all(bdEngine)

    # заполнене таблицы Products для ПРИМЕРА     
    with Session(bdEngine) as db:
        row_1 = RowTableProducts(
            picture = "picture/Burger.png", 
            product_name = "Burger", 
            pickUp_point = 'Dmitra Yavornitskogo avenue 50', 
            price = 20, 
            quantity = 5)
        db.add(row_1)
        db.commit()

        row_2 = RowTableProducts(
            picture = "picture/Cheeseburger.png", product_name = "Cheeseburger", 
            pickUp_point = 'Dmitra Yavornitskogo avenue 51', 
            price = 20, 
            quantity = 6)
        db.add(row_2)
        db.commit()

        row_3 = RowTableProducts(
            picture = "picture/French fries.png",
            product_name = "French fries", 
            pickUp_point = 'Dmitra Yavornitskogo avenue 52', 
            price = 22, 
            quantity = 7)
        db.add(row_3)
        db.commit()

        row_4 = RowTableProducts(
            picture = "picture/Hamburger.png", 
            product_name = "Hamburger", 
            pickUp_point = 'Dmitra Yavornitskogo avenue 53', 
            price = 20, 
            quantity = 5)
        db.add(row_4)
        db.commit()

    # заполнене таблицы Users для ПРИМЕРА
    with Session(bdEngine) as db:
        row_1 = RowTableUsers(
            first_name = 'Roman', 
            last_name = 'Honcharov', 
            mail = 'qwert@gmail.com', 
            card_naumber = 111122223333444)
        db.add(row_1)
        db.commit()

        row_2 = RowTableUsers(
            first_name = 'Roman_1', 
            last_name = 'Honcharov_1', 
            mail = 'qwert1@gmail.com', 
            card_naumber = 111122223333445)
        db.add(row_2)
        db.commit()

        row_3 = RowTableUsers(
            first_name = 'Roman_2', 
            last_name = 'Honcharov_2', 
            mail = 'qwert2@gmail.com', 
            card_naumber = 111122223333446)
        db.add(row_3)
        db.commit()

    # функция добавления строки в таблицу Products
    def row_add_products(productDictionary:dict)->RowTableProducts:
        with Session(Creature_bd.bdEngine) as db:
            row = RowTableProducts(
                picture = productDictionary['picture'], 
                product_name = productDictionary['product_name'], 
                pickUp_point = productDictionary['pickUp_point'], 
                price = productDictionary['price'], 
                quantity = productDictionary['quantity'])
            db.add(row)
            db.commit()

    # функция добавления строки в таблицу Products
    def row_add_users(userDictionary:dict)->RowTableUsers:
        with Session(Creature_bd.bdEngine) as db:
            row = RowTableUsers(
                first_name = userDictionary['first_name'], 
                last_name = userDictionary['last_name'], 
                mail = userDictionary['mail'], 
                card_naumber = userDictionary['card_naumber']
            )
            db.add(row)
            db.commit()

    # выбор укзанной строки
    def singleSelect(id): 
        singleSelect = db.get(RowTableProducts, 2) # второй аргумент  - id таблици с БД
        # print(singleSelect) # вывод адреса ячейки в памяти ПК
    
        # вывод значений полей БД
        # for i in selectCondition:
        #print(i.login, i.password)

        # изменения значений полей БД
        # singleSelect.password = "1"
        # db.commit()
        # db.refresh(singleSelect) # обновление значениея поля БД рекомендуется после изм. знач. поля в БД


# для проверки функции row_add_products
# myDictionary = {'picture':"picture/Burger.png", 'product_name':"Sandvich", 'pickUp_point':'avenue', 'price':200, 'quantity':9}
# Creature_bd.row_add_products(myDictionary)

print(Creature_bd.singleSelect)