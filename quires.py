import pymysql
from config import Config
import logging


def create_db():
    con = pymysql.connect(host=Config.host, user=Config.user, password=Config.password)
    with con:
        cur = con.cursor()
        try:
            cur.execute(f'CREATE DATABASE {Config.d_name}')
            con.commit()
            logging.debug(f"DATABASE '{Config.d_name}' is create!")
        except:
            logging.error('Database is exist!')



#TODO: была создана main, чтобы не плодить вызывать так
def create_table(table_name: str):
    con = pymysql.connect(host=Config.host, user=Config.user, password=Config.password, database=Config.d_name)
    with con:
        cur = con.cursor()
        try:
            cur.execute(
                f"CREATE TABLE {table_name} (`uid` INT NOT NULL AUTO_INCREMENT, `username` TEXT NOT NULL, `age` INT NULL, PRIMARY KEY (`uid`))")
            logging.debug(f"Table {table_name} is create!")
        except:
            logging.error("Table is exist!")


def add_user(username: str, age: int):
    con = pymysql.connect(host=Config.host, user=Config.user, password=Config.password, database=Config.d_name)
    with con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO `main`(`username`, `age`) VALUES ('{username}','{age}')")
        con.commit()
        logging.info(f"Note for {username} is create!")


def get_user_age(username: str):
    con = pymysql.connect(host=Config.host, user=Config.user, password=Config.password, database=Config.d_name)
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT `username`, `age` FROM main WHERE `username` = '{username}'")
        data = cur.fetchone()
        out = f"{data[0]} is {data[1]}"
    return out


