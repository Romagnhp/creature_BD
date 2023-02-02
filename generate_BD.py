import sqlalchemy
from table_patern import BaseClass, RowTableProduct, RowTableOrder, RowTableOrderProduct
# RowTableRole,  RowTablePickupPoint, RowTableUser,  
from sqlalchemy.orm import Session

class Creature_bd:
    bdEngine = sqlalchemy.create_engine("sqlite:///bot_BD.db")
    bdConection = bdEngine.connect()

    BaseClass.metadata.drop_all(bdEngine)
    BaseClass.metadata.create_all(bdEngine)

    # заполнене таблицы Products для ПРИМЕРА    
    with Session(bdEngine) as db:
        row_1 = RowTableProduct( 
            name = "Burger",
            description = '''
                            veal cutlet, 
                            wheat bun, 
                            American mustard, 
                            red onion, 
                            mayonnaise, 
                            pickles, 
                            lettuce leaf, 
                            barbecue sauce;
                            ''',
            picture = "picture/Burger.png", 
            price = 20,
            quantity = 5)    
        db.add(row_1)
        db.commit()

        row_2 = RowTableProduct(
            name = "Cheeseburger",
            description = '''
                            grilled natural beef steak,
                            seasoning for grill,
                            hamburger bun, toasted,
                            processed cheese Cheddar,
                            mustard sauce,
                            pickles,
                            reconstituted onion
                        ''',
            picture = "picture/Cheeseburger.png",
            price = 20, 
            quantity = 6)
        db.add(row_2)
        db.commit()

        row_3 = RowTableProduct(
            name = "French fries",
            description = 'potatoes',
            picture = "picture/French fries.png",
            price = 22, 
            quantity = 7)
        db.add(row_3)
        db.commit()

        row_4 = RowTableProduct(
            name = "Hamburger",
            description = '''
                        grilled natural beef steak,
                        toasted burger bun,
                        seasoning for grill,
                        mustard sauce,
                        pickles,
                        reconstituted onion,
                        ''',
            picture = "picture/Hamburger.png",
            price = 20, 
            quantity = 5)
        db.add(row_4)
        db.commit()

    # заполнене таблицы Orders для ПРИМЕРА
    with Session(bdEngine) as db:
        row_1 = RowTableOrder(
            id_user = 1,
            pickupPoint = 'avenue Dmytro Yavornytsky 100',
            dateTime = 14,
            typePay = 'cash',
            status = 'ready'
            )
        db.add(row_1)
        db.commit()

        row_2 = RowTableOrder(
            id_user = 2,
            pickupPoint = 'avenue Dmytro Yavornytsky 50',
            dateTime = 13,
            typePay = 'cash',
            status = 'wait'
            )
        db.add(row_2)
        db.commit()

    # заполнене таблицы Orders-Products для ПРИМЕРА
    with Session(bdEngine) as db:

        row_1 = RowTableOrderProduct(
            id_order = 1,
            id_product = 1,
            quantity = 10
        )
        db.add(row_1)
        db.commit()
    
        row_2 = RowTableOrderProduct(
            id_order = 2,
            id_product = 2,
            quantity = 11
        )
        db.add(row_2)
        db.commit()


    # функция добавления строки в таблицу Products
    def row_add_products(productDictionary:dict)->RowTableProduct:
        with Session(Creature_bd.bdEngine) as db:
            row = RowTableProduct( 
                name = productDictionary['name'],
                description = productDictionary['description'],
                picture = productDictionary['picture'], 
                price = productDictionary['price'],
                quantity = productDictionary['quantity']
                )    
            db.add(row)
            db.commit()        

  # функция добавления строки в таблицу Orders
    def row_add_orders(orderDictionary:dict)->RowTableOrder:
        with Session(Creature_bd.bdEngine) as db:
            row = RowTableOrder(
                id_user = orderDictionary['id_user'],
                pickupPoint = orderDictionary['pickupPoint'],
                dateTime = orderDictionary['dateTime'],
                typePay = orderDictionary['typePay'],
                status = orderDictionary['status']
            )
            db.add(row)
            db.commit()

    # функция добавления строки в таблицу Orders-Products
    def row_add_OrderPoduct(orderProductDictionary:dict)->RowTableOrderProduct:
        with Session(Creature_bd.bdEngine) as db:
            row = RowTableOrderProduct(
            id_order = orderProductDictionary['id_order'],
            id_product = orderProductDictionary['id_product'],
            quantity = orderProductDictionary['quantity']
        )
        db.add(row)
        db.commit()

    # функция выбора всех строк таблицы
    def tableSelect(tableName)->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = db.query(tableName).all() 
        return listTable


    # функция выбор укзанной строки таблицы Products по primay_key
    def rowSelectProduct(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(RowTableProduct, id)
            rowProoduct = {'name':row.name, 'description':row.description, 'picture':row.picture, 'price':row.price, 'quantity':row.quantity}
        return rowProoduct    

    # функция выбор укзанной строки таблицы Orders по primay_key
    def rowSelectOrder(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(RowTableOrder, id)
            rowProoduct = {'id_user':row.id_user, 'pickupPoint':row.pickupPoint, 'dateTime':row.dateTime, 'typePay':row.typePay, 'status':row.status}
        return rowProoduct 

    # функция выбор указанной сторки таблицы Orders-Products
    def rowSelectOrderPoduct(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(RowTableOrderProduct, id)
            rowOrderProduct = {'id_order':row.id_order, 'id_product':row.id_product, 'quantity':row.quantity}
        return rowOrderProduct 

    # функция изменение значения поля таблицы Products 
    def changeValesProduct(poductPrimary_key, nameValues, newValues):
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(RowTableProduct, poductPrimary_key)
            row.nameValues = newValues
            db.commit()
            db.refresh(row)


# ПРОВЕРКА ФУНКЦИЙ

productDictionary = {'name':"French freies_1", 'description': "potetoes", 'picture':"picture/French fries.png", 'price':200, 'quantity':9}
Creature_bd.row_add_products(productDictionary)

orderDictionary = {'id_user':10, 'pickupPoint':"avenue Dmytro Yavornytsky 100", 'dateTime':14, 'typePay':"cash", 'status': "ready"}
Creature_bd.row_add_orders(orderDictionary)

orderProductDictionary = {'id_order':1, 'id_product':4, 'quantity':3}
Creature_bd.row_add_OrderPoduct(orderProductDictionary)

# print(Creature_bd.rowSelectProduct(1))

# print(Creature_bd.rowSelectOrder(1))

# print(Creature_bd.rowSelectOrderPoduct(1))

# Creature_bd.changeValesProduct(3, 'name', 'бургер1111')

print(Creature_bd.tableSelect(RowTableProduct))
