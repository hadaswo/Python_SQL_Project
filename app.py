from flask import Flask, render_template, request
from inventory import *

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello DevOps Class</h1>'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'


@app.route('/inventory')
def get_items():
    PATH = "C:\\Users\\USER\\Devops 3\\22\SQL-Practice\\"
    FILENAME = "Inventory.db"
    FILE = PATH + FILENAME
    con = set_sql_connection(FILE)  # Creates connection
    cur = set_sql_cursor(con)  # Creates Cursor
    query = "SELECT * FROM Inventory"  # SQL QUERY
    data = cur.execute(query).fetchall()  # EXECUTING SQL QUERY
    dct = sort_as_dict(cur, data)
    close_sql_connection(con)  # Closing connection
    return f'{dct}'


@app.route('/insertitem', methods=['GET', 'POST'])  ##page to add a new item
def load_insert_item_html():
    if request.method == 'POST':
        #def add_item(item,category,quantity,price,date):
        date = todays_date()
        add_item(request.form['name'],request.form['category'],  request.form['quantity'], request.form['price'], date )
        return render_template('insertitem.html')
    return render_template('insertitem.html')

@app.route('/update_price', methods=['GET','POST']) ##page to update price of an item
def price_change():
    if request.method == 'POST':
        update_item_price(request.form['name'], request.form['price'])
        return render_template('update_price.html')
    return render_template('update_price.html')

@app.route('/update_quantity', methods=['GET','POST']) ##page to update quantity of an item
def quantity_change():
    if request.method == 'POST':
        update_item_quantity(request.form['name'], request.form['quantity'])
        return render_template('update_quantity.html')
    return render_template('update_quantity.html')

@app.route('/update_name', methods=['GET','POST']) ##page to update name of an item
def name_change():
    if request.method == 'POST':
        update_item_name(request.form['name'], request.form['new_name'])
        return render_template('update_name.html')
    return render_template('update_name.html')

@app.route('/update_category', methods=['GET','POST']) ##page to update category of an item
def category_change():
    if request.method == 'POST':
        update_item_category(request.form['name'], request.form['category'])
        return render_template('update_category.html')
    return render_template('update_category.html')

@app.route('/delete_item', methods=['GET','POST']) ##page to delete an item
def del_item():
    if request.method == 'POST':
        delete_item(request.form['name'])
        return render_template('delete_item.html')
    return render_template('delete_item.html')


@app.route('/highest') ##page to show one or a list of items with the highest quantity from the DB
def highest():
    html="<html><body><ul>"
    high = find_highest_quantity()
    for line in high:
        html+=f"<li>{line}</li>"
    html+='<br/> <a href="/">Back home</a> <br/> </ul></body></html>'
    return f'{html}'

@app.route('/lowest') ##page to show one or a list of items with the lowest quantity from the DB
def lowest():
    html="<html><body><ul>"
    lwst = find_lowest_quantity()
    for line in lwst:
        html+=f"<li>{line}</li>"
    html+='<br/> <a href="/">Back home</a> <br/> </ul></body></html>'
    return f'{html}'

@app.route('/sort') ##page to show list from the DB sorted by price in a descending order
def sort_by_price():
    html="<html><body><ul>"
    srt = sort_db_by_price()
    for line in srt:
        html+=f"<li>{line}</li>"
    html+='<br/> <a href="/">Back home</a> <br/> </ul></body></html>'
    return f'{html}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
