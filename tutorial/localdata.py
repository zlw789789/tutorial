# -*- coding: utf-8 -*-

import sqlite3

db=sqlite3.connect('movie.db')
cur=db.cursor()
cur.execute('''CREATE TABLE Movie
       (ID            INTEGER PRIMARY KEY autoincrement,
       NAME           VARCHAR(1024)     NOT NULL,
       movieInfo      VARCHAR(1024)     NOT NULL,
       star           VARCHAR(16)       DEFAULT NULL,
       quote          VARCHAR(1024)     DEFAULT NULL,
       createtime     DATETIME          DEFAULT CURRENT_TIMESTAMP);''')
db.commit()
db.close()