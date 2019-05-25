import random
def config(app):
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
        app.config['MYSQL_DATABASE_DB'] = 'urls'

def set_url(cursor, conn, urlorig,number):
    newurl = ('http://localhost:5000/')+ str(number)
    cursor.execute(f'insert into urls.lessurl (idlessurl,urlorig, newurl) values("{number}","{urlorig}", "{newurl}")')
    conn.commit()


def random_number():
    number = random.randint(5000, 10001)
    return number


def get_links(cursor):
    cursor.execute(f'SELECT urlorig, newurl, acessos FROM urls.lessurl')

    newurls = cursor.fetchall()

    return newurls

