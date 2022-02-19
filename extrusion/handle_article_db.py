import sqlite3
import gain_xl_date

CREATE_ARTICLE_TABLE = """CREATE TABLE IF NOT EXISTS article (
    id INTEGER PRIMARY KEY,
    articles TEXT,
    prod_weight(kg) INTEGER,
    width(mm) INTEGER,
    length(mm) INTEGER,
    inner_pack_weight(kg) INTEGER,
    outer_pack_weight(kg) INTEGER,
    quantity(pcs) INTEGER,
    ref_weight(g) INTEGER,
    thickness(mm) INTEGER,
    active INTEGER,
    created INTEGER,
    modified INTEGER);"""

INSERT_ARTICLE = """INSERT INTO article (
    articles,
    prod_weight(kg),
    width(mm),
    length(mm),
    inner_pack_weight(kg),
    outer_pack_weight(kg),
    quantity(pcs),
    ref_weight(g),
    thickness(mm),
    active,
    created,
    modified) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""

GET_ALL_ARTICLES = "SELECT articles FROM article"

GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;" 

GET_BEST_PREPARATION_FOR_BEAN = """
SELECT name FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""

def connect():
    return sqlite3.connect('/home/pi/projects/extrusion/DB/articles.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_ARTICLE_TABLE)

# variables for *var, lookup 'INSERT_BEAN'
def add_article(connection, *var):
    with connection:
        connection.execute(INSERT_ARTICLE, var)

def get_all_articles(connection):
    with connection:
        return connection.execute(GET_ALL_ARTICLES).fetchall()

def get_beans_by_name(connection, name):
    with connection:
        connection.execute(GET_BEANS_BY_NAME,(name,)).fetchall()

def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()
