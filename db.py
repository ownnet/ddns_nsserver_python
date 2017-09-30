from peewee import *
import conf

if conf.DB_TYPE == 0:
    db = MySQLDatabase(conf.MYSQL_DBNAME,host=conf.MYSQL_HOST,user=conf.MYSQL_USERNAME,passwd=conf.MYSQL_PASSWORD)
if conf.DB_TYPE == 1:
    db = SqliteDatabase(conf.SQL_PATH)

db.connect()

class BashModel(Model):
    class Meta:
        database = db