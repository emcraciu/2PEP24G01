import sqlite3 as sql

def insertUser(username, password, email, name):
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, password, email, name) VALUES (?,?,?,?)",
                (username, password, email, name))
    con.commit()
    con.close()

# insertUser('csporea','asd', 'sporea.ciprian@gmail.com', 'Ciprian Sporea')
# insertUser('rbrig','def', 'rbrig@gmail.com', 'Rebecca Brig')

def deleteUser(table, id):
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM {table} WHERE id = {id}")
    con.commit()
    con.close()

# deleteUser('users', 4)

def updateUserColumn(table, id, col_name, col_value):
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    query = f"UPDATE {table} SET {col_name} = {col_value} WHERE id = {id}"
    cur.execute(query)
    con.commit()
    con.close()

# updateUserColumn('users', 1, 'id', 1)

def retrieveUsers():
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    con.close()
    return users

def insertCookie(username, expiry_days, sgnkey, cookiename):
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    cur.execute("INSERT INTO cookies (username, expiry_days, sgnkey, name) VALUES (?,?,?,?)",
                (username, expiry_days, sgnkey, cookiename))
    con.commit()
    con.close()

# insertCookie('csporea',30, 'some_signature_key', 'some_cookie_name')
# insertCookie('rbrig',30, 'some_signature_key', 'some_cookie_name')

def deleteCookie(table, id):
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM {table} WHERE id = {id}")
    con.commit()
    con.close()

# deleteCookie('cookies', 3)

def updateCookieColumn(table, id, col_name, col_value):
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    query = f"UPDATE {table} SET {col_name} = {col_value} WHERE id = {id}"
    cur.execute(query)
    con.commit()
    con.close()

# updateCookieColumn('cookies', 3, 'username', str('new_name'))

def retrieveCookie():
    con = sql.connect(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM cookies")
    users = cur.fetchall()
    con.close()
    return users

def Users():
    users_dict = {'credentials': {'usernames': {}}}
    users = retrieveUsers()
    for val in users:
        users_dict['credentials']['usernames'][val[1]] = {'email': val[3],
                                                        'failed_login_attempts': 0,
                                                        'logged_in': False,
                                                        'name': val[4],
                                                        'password': val[2]
                                                        }
    return users_dict

def Cookies():
    cookies_dict = {'cookie': {}}
    cookies = retrieveCookie()
    for val in cookies:
        cookies_dict['cookie'][val[1]] = {'expiry_days': val[2], 'key': val[3], 'name': val[4]}
    return cookies_dict

def Preauthorized():
    preauthorized_dict = {'pre-authorized': {'emails': ['sporea.ciprian@gmail.com']}}
    return preauthorized_dict
