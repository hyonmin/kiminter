from gettext import find
import sqlite3
import gain_xl_date

CREATE_ARTICLE_TABLE = """CREATE TABLE IF NOT EXISTS article_local (
    id INTEGER PRIMARY KEY,
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
    id
FROM article_local
WHERE modified = ?
AND deleted = ?;"""

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
WHERE id = ?;"""

DEL_MODIFIED = """UPDATE article_local SET modified = ? WHERE id = ?;"""

FIND_CREADED = """SELECT created FROM article_local WHERE id = ?;"""

DEL_ARTICLE = """
UPDATE article_local
SET deleted = ?
WHERE id = ?;
"""

def connect():
    return sqlite3.connect('/home/pi/projects/extrusion/DB/extrusion.db')


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
        return connection.execute(FIND_CREADED, var)

def get_article_modified(connection, var):
    with connection:
        connection.execute(GET_ARTICLE_MODIFIED, var)

def del_modified(connection, var):
    with connection:
        connection.execute(DEL_MODIFIED, var)

def delete_article(connection, del_var):
    with connection:
        connection.execute(DEL_ARTICLE, del_var)


print(CREATE_ARTICLE_TABLE)

