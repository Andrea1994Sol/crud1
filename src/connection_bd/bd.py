from flaskext.mysql import MySQL
from flask import Flask

connection = Flask(__name__)

connection.config['MYSQL_DATABASE_HOST'] = 'localhost'
connection.config['MYSQL_DATABASE_PORT'] = 3306
connection.config['MYSQL_DATABASE_USER'] = 'root'
connection.config['MYSQL_DATABASE_PASSWORD'] = ''
connection.config['MYSQL_DATABASE_DB'] = 'dbflask'

mysql = MySQL(connection)

#import mariadb

#config = {
#    'host' : 'localhost',
#    'port' : 3306,
#    'user' : 'root',
#    'password' : 'Jmerazo96*',
#    'database' : 'users',
#}

#DB = mariadb.connect(**config)
#DB.autocommit = True
