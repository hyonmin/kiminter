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

CREATE_TRASH_BIN = """
CREATE TABLE IF NOT EXISTS trash_roll(
    trash_id INTEGER PRIMARY KEY,
    roll_id INTEGER,
    article_id INTEGER,
    weight_roll REAL,
    machine_id INTEGER,
    equipe_id INTEGER,
    production_date TEXT,
    realtime TEXT,
    modified TEXT,
    deleted TEXT);
"""

ADD_ROLL = """
INSERT INTO production_ext(
    article_id,
    weight_roll,
    machine_id,
    equipe_id,
    production_date,
    realtime)
    VALUES
    (?,?,?,?,?,?);
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
    AND machine_id = (SELECT machine_id FROM machine WHERE machine_name = ?);
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
    AND machine_id = (SELECT machine_id FROM machine WHERE machine_name = ?);
"""
MOVE_TO_TRASH1 = """
SELECT * FROM production_ext WHERE roll_id = ?;
"""
MOVE_TO_TRASH2 = """
INSERT INTO trash_roll(
    roll_id,
    article_id,
    weight_roll,
    machine_id,
    equipe_id,
    production_date,
    realtime,
    modified,
    deleted)
    VALUES (?,?,?,?,?,?,?,?,?);
"""

DEL_ROLL = """
DELETE FROM production_ext
WHERE roll_id = ?;
"""

COMP_BEFORE_MODIF = """
SELECT
    article_id,
    weight_roll
FROM production_ext
WHERE
roll_id = ?
"""

MODIFIY = """
UPDATE production_ext
SET
    article_id = ?,
    weight_roll = ?,
    realtime = ?
WHERE roll_id = ?;
"""

def connect():
    import os
    a = os.getcwd()
    a = a + "/DB/extrusion.db"
    return sqlite3.connect(a)
    # return sqlite3.connect('/home/pi/projects/extrusion/DB/extrusion.db')

def create_tables(connection):
    with connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(CREATE_PROD_TABLE)

def create_trash_bin(connection):
    with connection:
        connection.execute(CREATE_TRASH_BIN)

def add_roll(connection, *var):
    with connection:
        connection.execute(ADD_ROLL, var)

def get_weights(connection, *var):
    with connection:
        return connection.execute(GET_WEIGHTS, var).fetchall()

def get_last_article(connection, *var):
    with connection:
        return connection.execute(GET_LAST_ARTICLE, var).fetchone()

def move_to_trash1(connection, var):
    with connection:
        return connection.execute(MOVE_TO_TRASH1, (var,)).fetchall()

def move_to_trash2(connection, var):
    with connection:
        connection.execute(MOVE_TO_TRASH2, var)

def delete_roll(connection, var):
    with connection:
        connection.execute(DEL_ROLL, (var,))

def comp_before_modif(connection, var):
    with connection:
        return connection.execute(COMP_BEFORE_MODIF, (var,)).fetchone()

def modify(connection, *var):
    with connection:
        connection.execute(MODIFIY, var)




CREATE_DECHET_TABLE = """
CREATE TABLE IF NOT EXISTS dechet(
    dechet_id INTEGER,
    article_id INTEGER NOT NULL,
    weight_dechet REAL NOT NULL,
    [noir or blanc] TEXT,
    machine_id INTEGER NOT NULL,
    equipe_id INTEGER NOT NULL,
    production_date TEXT NOT NULL,
    realtime TEXT NOT NULL,
        PRIMARY KEY (dechet_id),
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

INFO_DECHET = """
SELECT
    dechet_id,
    [noir or blanc],
    weight_dechet
FROM dechet
WHERE
    production_date = ?
    AND equipe_id = ?
    AND machine_id = (SELECT machine_id FROM machine WHERE machine_name = ?);
"""

MAKE_REPORT_PER_MACHINE = """
SELECT
    (SELECT machine_name
    FROM machine
    WHERE machine.machine_id = production_ext.machine_id),
    COUNT(weight_roll),
    printf("%.2f", SUM(weight_roll)),
    printf("%.2f", (SELECT SUM(weight_dechet) FROM dechet WHERE
    dechet.machine_id = production_ext.machine_id))
FROM
    production_ext
WHERE
    equipe_id = ?
    AND
    production_date = ?
GROUP BY
    (SELECT machine_name
    FROM machine
    WHERE machine.machine_id = production_ext.machine_id);
"""
ADD_DECHET = """
INSERT INTO dechet(
    article_id,
    weight_dechet,
    [noir or blanc],
    machine_id,
    equipe_id,
    production_date,
    realtime)
    VALUES (?,?,?,?,?,?,?);
"""
DEL_DECHET = """
DELETE FROM dechet WHERE dechet_id=?;
"""

MOVE_TO_TRASH_DECHET1 = """
SELECT * FROM dechet WHERE dechet_id = ?;
"""
MOVE_TO_TRASH_DECHET2 = """
INSERT INTO trash_dechet(
    dechet_id,
    article_id,
    weight_dechet,
    [noir or blanc],
    machine_id,
    equipe_id,
    production_date,
    realtime,
    deleted)
    VALUES (?,?,?,?,?,?,?,?,?);
"""
TRASH_DECHET= """
CREATE TABLE IF NOT EXISTS trash_dechet(
    trash_id INTEGER PRIMARY KEY,
    dechet_id INTEGER,
    article_id INTEGER NOT NULL,
    weight_dechet REAL NOT NULL,
    [noir or blanc] TEXT,
    machine_id INTEGER NOT NULL,
    equipe_id INTEGER NOT NULL,
    production_date TEXT NOT NULL,
    realtime TEXT NOT NULL,
    deleted TEXT);
"""
REPORT_TOTAL = """
SELECT
    COUNT(weight_roll),
    printf("%.2f", SUM(weight_roll)),
    printf("%.2f", (SELECT SUM(weight_dechet) FROM dechet WHERE [noir or blanc] = 'blanc')),
    printf("%.2f", (SELECT SUM(weight_dechet) FROM dechet WHERE [noir or blanc] = 'noir'))
FROM production_ext
WHERE equipe_id = ?
AND production_date = ?
"""

REPORT_ARTICLE = """
SELECT
    (SELECT articles FROM article_local WHERE production_ext.article_id = article_local.article_id),
    SUM(weight_roll)
FROM production_ext
WHERE equipe_id = ?
AND production_date = ?
GROUP BY
    (SELECT articles FROM article_local WHERE production_ext.article_id = article_local.article_id)
"""
def create_dechet_table(connection):
    with connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(CREATE_DECHET_TABLE)

def create_dechet_trash(connection):
    with connection:
        connection.execute(TRASH_DECHET)

def info_dechet(connection, *var):
    with connection:
        return connection.execute(INFO_DECHET, var).fetchall()

def release_report_per_machine(connection, var1, var2):
    with connection:
        return connection.execute(MAKE_REPORT_PER_MACHINE, (var1, var2,)).fetchall()

def add_dechet(connection, *var):
    with connection:
        connection.execute(ADD_DECHET, var)

def move_to_trash_dechet1(connection, var):
    with connection:
        return connection.execute(MOVE_TO_TRASH_DECHET1, (var,)).fetchall()

def move_to_trash_dechet2(connection, var):
    with connection:
        connection.execute(MOVE_TO_TRASH_DECHET2, var)

def del_dechet(connection, var):
    with connection:
        connection.execute(DEL_DECHET, (var,))

def report_total(connection, var1, var2):
    with connection:
        return connection.execute(REPORT_TOTAL, (var1, var2,)).fetchall()    

def report_article(connection, var1, var2):
    with connection:
        return connection.execute(REPORT_ARTICLE, (var1, var2,)).fetchall()



#create_tables(connect())
#create_trash_bin(connect())
#create_dechet_table(connect())
##a = connect()
#create_dechet_table(a)
#create_tables(a)

#b = release_report_per_machine(a, 2, '02/03/2022')
#c= report_total(a, 2, '02/03/2022')
#print(b)
#print(c)
#d= report_article(a, 2, '02/03/2022')
#print(d)