import sqlite3

CREATE_ARTICLE_TABLE = """CREATE TABLE IF NOT EXISTS article_local (
    article_id INTEGER PRIMARY KEY,
    articles TEXT,
    [prod_weight(kg)] REAL,
    [width(cm)] REAL,
    [length(cm)] REAL,
    [inner_pack_weight(kg)] REAL,
    [outer_pack_weight(kg)] REAL,
    [quantity(pcs)] INTEGER,
    [gusset(cm)] REAL,
    [ref_weight(g)] REAL,
    [thickness(μm)] REAL,
    active INTEGER,
    created INTEGER,
    modified INTEGER,
    deleted INTEGER);"""

INSERT_ARTICLE = """INSERT INTO article_local (
    articles,
    [prod_weight(kg)],
    [width(cm)],
    [length(cm)],
    [inner_pack_weight(kg)],
    [outer_pack_weight(kg)],
    [quantity(pcs)],
    [gusset(cm)],
    [ref_weight(g)],
    [thickness(μm)],
    active,
    created,
    modified,
    deleted) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

GET_ALL_ARTICLES = "SELECT articles FROM article_local WHERE modified = ? AND deleted = ?;"

GET_INFO_TREEVIEW = """
SELECT
    articles,
    [ref_weight(g)],
    [width(cm)],
    [length(cm)],
    [gusset(cm)],
    [prod_weight(kg)],
    [quantity(pcs)],
    [inner_pack_weight(kg)],
    [outer_pack_weight(kg)],
    [thickness(μm)],
    article_id
FROM article_local
WHERE modified = ?
AND deleted = ?;"""

GET_LISTBOX = """
SELECT article_id, articles
FROM article_local
WHERE modified = ?
AND deleted = ?
AND active = ?;"""

GET_ARTICLE_MODIFIED = """
UPDATE article_local
SET
    [prod_weight(kg)] = ?,
    [width(cm)] = ?,
    [length(cm)] = ?,
    [inner_pack_weight(kg)] = ?,
    [outer_pack_weight(kg)] = ?,
    [quantity(pcs)] = ?,
    [gusset(cm)] = ?,
    [ref_weight(g)] = ?,
    [thickness(μm)] = ?,
    modified = ?
WHERE article_id = ?;"""

DEL_MODIFIED = """UPDATE article_local SET modified = ? WHERE article_id = ?;"""

FIND_CREADED = """SELECT created FROM article_local WHERE article_id = ?;"""

DEL_ARTICLE = """
UPDATE article_local
SET deleted = ?
WHERE article_id = ?;
"""
MAKE_ACT_INACT = """
UPDATE article_local
SET active = ?
WHERE
article_id = ?;
"""

ARTICLE_ID = """
SELECT article_id
FROM article_local
WHERE
articles = ? AND deleted = ? AND modified = ?;"""

def connect():
    import os
    a = os.getcwd()
    a = a + "/DB/extrusion.db"
    return sqlite3.connect(a)
    # return sqlite3.connect('/home/pi/projects/extrusion/DB/extrusion.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_ARTICLE_TABLE)

# variables for *var, lookup 'INSERT_BEAN'
def add_article(connection, info_article):
    with connection:
        connection.execute(INSERT_ARTICLE, info_article)

def get_all_names(connection):
    with connection:
        return connection.execute(GET_ALL_ARTICLES, ('0','0')).fetchall()

def get_info_treeview(connection):
    with connection:
        return connection.execute(GET_INFO_TREEVIEW,('0','0')).fetchall()

def find_created(connection, var):
    with connection:
        return connection.execute(FIND_CREADED, var).fetchone()

def get_article_modified(connection, var):
    with connection:
        connection.execute(GET_ARTICLE_MODIFIED, var)

def del_modified(connection, var):
    with connection:
        connection.execute(DEL_MODIFIED, var)

def delete_article(connection, var):
    with connection:
        connection.execute(DEL_ARTICLE, var)

def get_listbox(connection, var):
    with connection:
        return connection.execute(GET_LISTBOX, (0, 0, str(var))).fetchall()    # with var = 0 , callback active, var = 1, callback inactive

def make_acf_inacf(connection, var):
    with connection:
        connection.execute(MAKE_ACT_INACT, var)

def lookup_articleID(connection, var):
    with connection:
        return connection.execute(ARTICLE_ID, (var,'0','0')).fetchone()