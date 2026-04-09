import os
import sys
import MySQLdb
import logging
logger = logging.getLogger(__file__)
logging.basicConfig(filename="./logs.log", level="DEBUG")
sys.stdout= open("./logs.log", "a")


conf = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "test",
    "password": "asdasdasd",
    "database": "test_base",
    "connect_timeout": 3
}



def error_handler(fn):
    def wrapper(*args, **kwargs):
        print(kwargs)
        try:
            fn(**kwargs)
        except MySQLdb.Error or Exception as err:
            print(err.args)
            print("CONNECTION FAILRD" if err.args[0] == 2002 else err.args)
            raise err
    return wrapper




@error_handler
def db(*args, **kwargs):
    
    query = "SELECT * FROM app_users WHERE username='name'"

    connection = MySQLdb.Connection(**kwargs)
    cursor = connection.cursor()
    # print(cursor.__dir__())
    cursor.execute(query)
    res = cursor.fetchone()
    print(res if res is not None else "NOT FOUND")


db(**conf)

