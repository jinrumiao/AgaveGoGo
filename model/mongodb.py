from pymongo import MongoClient
import datetime

stockDB = "line_bot_usage"
collection = "stock"


def constructor_stock():
    client = MongoClient("mongodb://test123:test321@ac-1mop3l8-shard-00-00.yexjncx.mongodb.net:27017,ac-1mop3l8-shard-00-01.yexjncx.mongodb.net:27017,ac-1mop3l8-shard-00-02.yexjncx.mongodb.net:27017/?ssl=true&replicaSet=atlas-1zn633-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client[stockDB]
    return db


def update_my_stock(user_name, stockNumber, condition, target_price):
    """
    更新暫存的股票名稱
    """
    db = constructor_stock()
    collection = db[user_name]
    collection.update_many(
        {"favorite_stock": stockNumber}, 
        {"$set": {"condition": condition, "price": target_price}}
    )
    content = f"股票{stockNumber}更新成功"

    return content


def write_my_stock(userID, user_name, stockNumber, condition, target_price):
    """
    新增使用者的股票
    """
    db = constructor_stock()
    collect = db[user_name]
    is_exist = collect.find_one({"favorate_stock": stockNumber})
    if is_exist != None:
        content = update_my_stock(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one(
            {
                "userID": userID, 
                "favorite_stock": stockNumber, 
                "condition": condition, 
                "price": target_price, 
                "tag": "stock", 
                "date_info": datetime.datetime.now()
            }
        )

        return f"{stockNumber}已新增至您的股票清單"
