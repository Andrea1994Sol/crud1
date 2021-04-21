from src.connection_bd.bd import mysql
from werkzeug.security import generate_password_hash, check_password_hash

class ShortenModel():

    def generate_short_link(self, url_to_shorten, url_shortened):
        cursor = mysql.get_db().cursor()
        cursor.execute('insert into urls_sht (url_shorten,url_to_shorten) values (%s,%s)',
                       (url_shortened, url_to_shorten,))
        mysql.get_db().commit()
        cursor.close()

    def redirect_url(self, url_shortened):
        cursor = mysql.get_db().cursor()
        cursor.execute(
            'SELECT url_to_shorten FROM urls_sht WHERE url_shorten = %s', (url_shortened,))
        data = cursor.fetchone()
        cursor.close()
        return data[0]
    
    def listUrls(self):
        cursor = mysql.get_db().cursor()
        cursor.execute(
            'SELECT url_shorten, url_to_shorten FROM urls_sht')
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def listUrlsUser(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("""SELECT s.url_shorten, url_to_shorten
                        FROM users AS u INNER JOIN urls_sht AS s ON u.urls = s.id
                        WHERE u.urls = %s""", (id,))
        data = cursor.fetchall()[0]
        cursor.close()
        return data       


class UsersModel():

    def create_user(self, user, email, password):
        cursor = mysql.get_db().cursor()
        cursor.execute('insert into users (user,email,password) values (%s,%s,%s)',
                       (user,email,password))
        mysql.get_db().commit()
        cursor.close()

class Authentication():

    def auth_user(self, email):
        cursor = mysql.get_db().cursor()
        cursor.execute(
            "SELECT email,password,user,id FROM users WHERE email=%s", (email))
        data = cursor.fetchone()
        cursor.close()
        return data



