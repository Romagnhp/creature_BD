import config
import sqlalchemy
from table_patern import BaseClass, Product, Order, OrderProduct

from sqlalchemy.orm import Session

class Creature_bd:

    bdEngine = sqlalchemy.create_engine(config.nameBD)
    bdConection = bdEngine.connect()

    BaseClass.metadata.drop_all(bdEngine)
    BaseClass.metadata.create_all(bdEngine)

    # заполнене таблицы Products для ПРИМЕРА    
    with Session(bdEngine) as db:
        row_1 = Product( 
            name = "Burger",
            description = 'veal cutlet, wheat bun, American mustard, red onion, mayonnaise, pickles, lettuce leaf, barbecue sauce',
            picture = config.pathPicture+"Burger.png", 
            price = 20,
            quantity = 5)    
        db.add(row_1)
        db.commit()

        row_2 = Product(
            name = "Cheeseburger",
            description = 'grilled natural beef steak,seasoning for grill,hamburger bun, toasted processed cheese Cheddar,mustard sauce,pickles,reconstituted onion',
            picture = config.pathPicture+"Cheeseburger.png",
            price = 20, 
            quantity = 6)
        db.add(row_2)
        db.commit()

        row_3 = Product(
            name = "French fries",
            description = 'potatoes',
            picture = config.pathPicture+"French fries.png",
            price = 22, 
            quantity = 7)
        db.add(row_3)
        db.commit()

        row_4 = Product(
            name = "Hamburger",
            description = 'grilled natural beef steak, toasted burger bun, seasoning for grill,mustard sauce,pickles, reconstituted onion,',
            picture = config.pathPicture+"Hamburger.png",
            price = 20, 
            quantity = 5)
        db.add(row_4)
        db.commit()

    # заполнене таблицы Orders для ПРИМЕРА
    with Session(bdEngine) as db:
        row_1 = Order(
            id_user = 1,
            pickupPoint = 'avenue Dmytro Yavornytsky 100',
            dateTime = 14,
            typePay = 'cash',
            status = 'ready'
            )
        db.add(row_1)
        db.commit()

        row_2 = Order(
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

        row_1 = OrderProduct(
            id_order = 1,
            id_product = 1,
            quantity = 10
        )
        db.add(row_1)
        db.commit()
    
        row_2 = OrderProduct(
            id_order = 2,
            id_product = 2,
            quantity = 11
        )
        db.add(row_2)
        db.commit()



    # функция добавления строки в таблицу Products
    def add_products(productDictionary:dict)->Product:
        with Session(Creature_bd.bdEngine) as db:
            row = Product( 
                name = productDictionary['name'],
                description = productDictionary['description'],
                picture = productDictionary['picture'], 
                price = productDictionary['price'],
                quantity = productDictionary['quantity']
                )    
            db.add(row)
            db.commit()        

  # функция добавления строки в таблицу Orders
    def add_orders(orderDictionary:dict)->Order:
        with Session(Creature_bd.bdEngine) as db:
            row = Order(
                id_user = orderDictionary['id_user'],
                pickupPoint = orderDictionary['pickupPoint'],
                dateTime = orderDictionary['dateTime'],
                typePay = orderDictionary['typePay'],
                status = orderDictionary['status']
            )
            db.add(row)
            db.commit()

    # функция добавления строки в таблицу Orders-Products
    def add_OrderPoduct(orderProductDictionary:dict)->OrderProduct:
        with Session(Creature_bd.bdEngine) as db:
            row = OrderProduct(
            id_order = orderProductDictionary['id_order'],
            id_product = orderProductDictionary['id_product'],
            quantity = orderProductDictionary['quantity']
        )
        db.add(row)
        db.commit()



    # функция выбора всех строк таблицы Products, возвращает список с вложенными кортежами
    def allProduct()->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = []
            for el in db.query(Product).all():
                listTable.append((el.id, el.name, el.description, el.picture, el.price, el.quantity))
        return listTable

     # функция выбора всех строк таблицы Orders, возвращает список с вложенными кортежами
    def allOrder()->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = []
            for el in db.query(Order).all():
                 listTable.append((el.id, el.id_user, el.pickupPoint, el.dateTime, el.typePay, el.status))
        return listTable

    # функция выбора всех строк таблицы Orders-Products, возвращает список с вложенными кортежами
    def allOrderProduct()->list:
        with Session(Creature_bd.bdEngine) as db:
            listTable = []
            for el in db.query(OrderProduct).all():
                listTable.append((el.id, el.id_order, el.id_product, el.quantity)) 
        return listTable


    # функция выбор укзанной строки таблицы Products по primay_key
    def selectProduct(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(Product, id)
            rowProoduct = {'name':row.name, 'description':row.description, 'picture':row.picture, 'price':row.price, 'quantity':row.quantity}
        return rowProoduct    

    # функция выбор укзанной строки таблицы Orders по primay_key
    def selectOrder(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(Order, id)
            rowProoduct = {'id_user':row.id_user, 'pickupPoint':row.pickupPoint, 'dateTime':row.dateTime, 'typePay':row.typePay, 'status':row.status}
        return rowProoduct 

    # функция выбор указанной сторки таблицы Orders-Products
    def selectOrderPoduct(id)->dict:
        with Session(Creature_bd.bdEngine) as db:
            row = db.get(OrderProduct, id)
            rowOrderProduct = {'id_order':row.id_order, 'id_product':row.id_product, 'quantity':row.quantity}
        return rowOrderProduct 

    # фунция изменения поля таблици Product
    # id - это id строки таблицы Product
    # calumn - это имя поля для изменения
    # value - новое значение поля
    def setProduct(id, calumn:str, value):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Product, id)
            match calumn:
                case 'id':
                    singleSelect.id = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'name':
                    singleSelect.name = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'description':
                    singleSelect.description = value
                case 'picture':
                    singleSelect.picture = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'quantity':
                    singleSelect.quantity = value
                    db.commit()
                    db.refresh(singleSelect)
                case other:
                    print ('There is no such calumn in a table')

    
    # фунция изменения поля таблици Orders
    # id - это id строки таблицы Orders
    # calumn - это имя поля для изменения
    # value - новое значение поля
    def setOrder(id, calumn:str, value):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Order, id)
            match calumn:
                case 'id':
                    singleSelect.id = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'id_user':
                    singleSelect.id_user = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'pickupPoint':
                    singleSelect.pickupPoint = value
                case 'dateTime':
                    singleSelect.dateTime = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'typePay':
                    singleSelect.typePay = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'status':
                    singleSelect.status = value
                    db.commit()
                    db.refresh(singleSelect)
                case other:
                    print ('There is no such calumn in a table')

     # фунция изменения поля таблици Orders-Products
    # id - это id строки таблицы Orders-Products
    # calumn - это имя поля для изменения
    # value - новое значение поля
    def setOrderProduct(id, calumn:str, value):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(OrderProduct, id)
            match calumn:
                case 'id':
                    singleSelect.id = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'id_order':
                    singleSelect.id_order = value
                    db.commit()
                case 'id_product':
                    singleSelect.id_product = value
                    db.commit()
                    db.refresh(singleSelect)
                case 'quantity':
                    singleSelect.quantity = value
                    db.commit()
                    db.refresh(singleSelect)
                case other:
                    print ('There is no such calumn in a table')


    # удаление строки таблицы Product по id
    def delProduct(id):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Product, id)
            db.delete(singleSelect)
            db.commit()
    
    # удаление строки таблицы Orders по id
    def delOrder(id):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(Order, id)
            db.delete(singleSelect)
            db.commit()

    # удаление строки таблицы OrderProduct по id
    def delOrderProduct(id):
        with Session(Creature_bd.bdEngine) as db:
            singleSelect = db.get(OrderProduct, id)
            db.delete(singleSelect)
            db.commit()


# ПРОВЕРКА ФУНКЦИЙ

# productDictionary = {'name':"French freies_1", 'description': "potetoes", 'picture':config.pathPicture+"French fries.png", 'price':200, 'quantity':9}
# Creature_bd.add_products(productDictionary)

# orderDictionary = {'id_user':10, 'pickupPoint':"avenue Dmytro Yavornytsky 100", 'dateTime':14, 'typePay':"cash", 'status': "ready"}
# Creature_bd.add_orders(orderDictionary)

# orderProductDictionary = {'id_order':1, 'id_product':4, 'quantity':3}
# Creature_bd.add_OrderPoduct(orderProductDictionary)

# print(Creature_bd.selectProduct(1))

# print(Creature_bd.selectOrder(1))

# print(Creature_bd.selectOrderPoduct(1))

# print(Creature_bd.allProduct())

# print(Creature_bd.allOrder())

# print(Creature_bd.allOrderProduct())

# изменения в таблице Product id=1 поля=name на значение 'Бургер' 
# Creature_bd.setProduct(1, 'n', 'Бургер')

# Удаление строки таблици Product по id
# Creature_bd.delProduct(1)
