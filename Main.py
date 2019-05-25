#Gabriel Rocha Meneses    RA: 21804708


from flask import Flask, render_template, request, url_for , redirect
from flaskext.mysql import MySQL
from Fun import config, get_links, random_number, set_url


app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)
config(app)


@app.route('/')
def home():
    conn = mysql.connect()
    cursor = conn.cursor()

    links=get_links(cursor)

    cursor.close()
    conn.close()
    return (render_template('home.html', links = links))


@app.route('/gerar', methods=['post'])
def gerando():
    if request.method == 'POST':
        url = request.form.get('url')
        number = random_number()
        conn = mysql.connect()
        cursor = conn.cursor()
        set_url(cursor,conn,url,number)
        cursor.close()
        conn.close()
        return (redirect(url))

    else:
        return home()

if __name__ == '__main__':
    app.run(debug=True)

print(redirect(dsadsa))