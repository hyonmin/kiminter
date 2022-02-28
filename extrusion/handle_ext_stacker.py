import sqlite3
CREATE_PROD_TABLE = """
CREATE TABLE IF NOT EXISTS production_ext(
    roll_id INTEGER,
    article_id INTEGER NOT NULL,
    weight_roll REAL NOT NULL,
    machine_id INTEGER NOT NULL,
    equipe_id INTEGER NOT NULL,
    production_date TEXT NOT NULL,
    realtime TEXT NOT NULL,
    deleted TEXT,
    modified TEXT,
        PRIMARY KEY (roll_id),
        FOREIGN KEY(article_id) REFERENCES article_local(article_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY(machine_id) REFERENCES machine(machine_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
        FOREIGN KEY(equipe_id) REFERENCES equipe(group_id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
    );
"""
ADD_ROLL = """
INSERT INTO production_ext(
    article_id,
    weight_roll,
    machine_id,
    equipe_id,
    production_date,
    realtime,
    deleted,
    modified)
    VALUES
    (?,?,?,?,?,?,?,?);
"""

GET_WEIGHTS = """
SELECT
    roll_id,
    (SELECT articles
    From article_local
    WHERE article_local.article_id = production_ext.article_id),
    weight_roll
FROM production_ext
WHERE
    production_date = ?
    AND equipe_id = ?
    AND machine_id = (SELECT machine_id FROM machine WHERE machine_name = ?)
    AND deleted = '0'
    AND modified = '0';
"""
GET_MACHINE="""
SELECT machine_id
FROM machine
WHERE machine_name = ?;
"""

GET_LAST_ARTICLE = """
SELECT
    MAX(roll_id),
    article_id,
    (SELECT articles
    From article_local
    WHERE article_local.article_id = production_ext.article_id)
FROM production_ext
WHERE
    production_date = ?
    AND equipe_id = ?
    AND machine_id = (SELECT machine_id FROM machine WHERE machine_name = ?)
    AND deleted = '0'
    AND modified = '0';
"""
DEL_PROD = """
UPDATE production_ext
SET deleted = ?,
modified = ?
WHERE
roll_id = ?;
"""

COMP_BEFORE_MODIF = """
SELECT
    article_id,
    weight_roll
FROM production_ext
WHERE
roll_id = ?
"""

def connect():
    return sqlite3.connect('/home/pi/projects/extrusion/DB/extrusion.db')

def create_tables(connection):
    with connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(CREATE_PROD_TABLE)

def add_roll(connection, *var):
    with connection:
        connection.execute(ADD_ROLL, var)

def get_machine(connection, var):
    with connection:
        return connection.execute(GET_MACHINE, (var,)).fetchone()

def get_weights(connection, *var):
    with connection:
        return connection.execute(GET_WEIGHTS, var).fetchall()

def get_last_article(connection, *var):
    with connection:
        return connection.execute(GET_LAST_ARTICLE, var).fetchone()

def del_prod(connection, *var):
    with connection:
        connection.execute(DEL_PROD, var)

def comp_before_modif(connection, var):
    with connection:
        return connection.execute(COMP_BEFORE_MODIF, (var,)).fetchone()

#create_tables(connect())