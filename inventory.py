import sqlite3
from datetime import date

PATH = "C:\\Users\\USER\\Devops 3\\22\SQL-Practice\\"
FILENAME = "Inventory.db"
FILE = PATH + FILENAME

def set_sql_connection():
    """
    this function connect to a DB with sqlite3 module and then return a connection object.
    """
    con = sqlite3.connect(FILE)
    # print(f"connected")
    return con

def set_sql_cursor(con):
    """
    this function create a curser object after a connection has been made with set_sql_connect.
    IN: con
    TYPE: sqlite3.connect
    OUT: cur
    TYPE: sqlite3.connect.curser
    """
    cur = sqlite3.Cursor(con)
    # print(f"curser up")
    return cur

def close_sql_connection(con):
    """
    this function commit the changes that been made to the DB via open connection and then close the connection to the DB.
    IN: con
    TYPE: sqlite3.connect
    """
    con.commit()
    # print(f"commited change in DB")
    con.close()


def get_items():
    """
    this function read and retrive all the informtion from the DB
    OUT: Values from DB as LIST
    TYPE: LIST
    """
    con = set_sql_connection()
    cur = set_sql_cursor(con)
    query = "SELECT * FROM Inventory"
    data = cur.execute(query).fetchall()
    dct= sort_as_dict(cur,data)
    close_sql_connection(con)
    return dct

def sort_as_dict(cur, data):
    columns = [desc[0] for desc in cur.description]
    result=[]
    for row in data:
        row=dict(zip(columns,row))
        result.append(row)
    return result

#print(get_items())


def is_item_exists(item):
    """
    this function chack if an object exist in the DB and return True or False.
    IN: an object to check if exist in DB
    TYPE: str
    OUT: True or False
    TYPE: bool
    """
    con = set_sql_connection()  ## Creates connection
    cur = set_sql_cursor(con)  ## Creates Cursor
    query = "SELECT * FROM Inventory"  ## SQL QUERY
    data = cur.execute(query).fetchall()  ## EXECUTING SQL QUERY
    close_sql_connection(con)  ##Closing connection
    for row in data:
        if row[1]== item:
            return True
    return False

#print(is_item_exists('Tent'))


def add_item(item,category,quantity,price,date):
    """
    This function inserts a new item (without number id) into an existing database, once validating that the item doesnt exist.
    commit the change to the DB and close connection.
    IN: an objects as values to add as item and check if exist in DB
    TYPE: str / int / date
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    if not is_item_exists(item): ## is exist validation
        query="INSERT INTO Inventory('item','category','quantity','price','date') VALUES (?,?,?,?,?)"
        cur.execute(query,(item,category,quantity,price,date)) ##Prepared statements
        print(f"New item has been added with the values of: {item,category,quantity,price,date}")
    else:
        print("Item already exists")
    close_sql_connection(con)

#add_item('Table','Furniture',10,200,today)


def update_item_price(item,price):
    """
    check if item exist and update the price of a specific Item by name.
    commit the change to the DB and close connection.
    IN: an item name to chack if exist and new price for the item
    TYPE: str / int
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    if not is_item_exists(item): ## is exist validation
        query = " UPDATE Inventory SET Price = ? WHERE Item = ? "
        value = (price,item)
        cur.execute(query,value)
        print(f"Item has been updated with the values of: {price,item}")
    else:
        print("Item doesn't exist")
    close_sql_connection(con)

#update_item_price("Table2",500)


def update_item_quantity(item,quantity):
    """
    check if item exist and update the quantity of a specific Item by name.
    commit the change to the DB and close connection.
    IN: an item name to chack if exist and new quantity for the item
    TYPE: str / int
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    if not is_item_exists(item): ## is exist validation
        query = " UPDATE Inventory SET Quantity = ? WHERE Item = ? "
        value = (quantity,item)
        cur.execute(query,value)
        print(f"Item has been updated with the values of: {quantity,item}")
    else:
        print("Item doesn't exist")
    close_sql_connection(con)

#update_item_quantity("Table3",100)


def update_item_name(item,name):
    """
    check if item exist and change item name.
    commit the change to the DB and close connection.
    IN: an item name to chack if exist and new name for the item
    TYPE: str
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    if not is_item_exists(item): ## is exist validation
        query = " UPDATE Inventory SET Item = ? WHERE Item = ? "
        value = (name,item)
        cur.execute(query,value)
        print(f"Item has been updated with the values of: {name,item}")
    else:
        print("Item doesn't exist")
    close_sql_connection(con)

#update_item_name("Table4","Table04")


def update_item_category(item,category):
    """
    check if item exist and update the Category of a specific Item by name.
    commit the change to the DB and close connection.
    IN: an item name to chack if exist and new Category for the item
    TYPE: str
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    if not is_item_exists(item): ## is exist validation
        query = " UPDATE Inventory SET Category = ? WHERE Item = ? "
        value = (category,item)
        cur.execute(query,value)
        print(f"Item has been updated with the values of: {category,item}")
    else:
        print("Item doesn't exist")
    close_sql_connection(con)

#update_item_category("Table5","Other")


def delete_item(item):
    """
    delete item from DB by a specific name (deletes a row)
    commit the change to the DB and close connection.
    IN: an object to delete from DB
    TYPE: str
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    if not is_item_exists(item): ## is exist validation
        query = f"DELETE FROM Inventory WHERE Item = '{item}'"
        cur.execute(query)
        print(f"Item with the values of: {item} has been deleted")
    else:
        print("Item doesn't exist")
    close_sql_connection(con)

#delete_item('Table10')


def find_highest_quantity():
    """
    this function read and retrive an item row with the highest quantity informtion from the DB
    OUT: Values from DB as LIST
    TYPE: LIST
    """
    con = set_sql_connection() ## CREATE CONNECTION
    cur = set_sql_cursor(con) ## CREATE CURSOR
    query = "SELECT * FROM Inventory WHERE Quantity = (SELECT Max(Quantity) FROM Inventory)"
    high = cur.execute(query).fetchall()
    print(f"{high}")
    close_sql_connection(con)
    return high

#find_highest_quantity()


def find_lowest_quantity():
    """
    this function read and retrive an item row with the lowest quantity informtion from the DB
    OUT: Values from DB as LIST
    TYPE: LIST
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    query = "SELECT * FROM Inventory WHERE Quantity = (SELECT Min(Quantity) FROM Inventory)"
    low = cur.execute(query).fetchall()
    print(f"{low}")
    close_sql_connection(con)
    return low

#find_lowest_quantity()


def sort_db_by_price():
    """
    this function read and retrive all the informtion from the DB sort by price in desc
    OUT: Values from DB as LIST
    TYPE: LIST
    """
    con = set_sql_connection()  ## CREATE CONNECTION
    cur = set_sql_cursor(con)  ## CREATE CURSOR
    query = f"SELECT * FROM Inventory ORDER BY Price DESC"
    data = cur.execute(query).fetchall()
    print(f"{data}")
    close_sql_connection(con)
    return data

#sort_db_by_price()

def todays_date():
    return date.today()
#print("Today's date:", today)

