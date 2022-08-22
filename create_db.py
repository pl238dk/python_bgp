import sqlite3 as sql

with sql.connect('db.db') as con:
	con.execute('CREATE TABLE nlri (net TEXT)')
	con.execute('CREATE TABLE next_hop (nlri_id INT, address TEXT, state INT)')
	con.commit()

'''

SELECT * FROM nlri;
+---------+---------------+
| rowid   | net           |
+---------+---------------+
|    1    | 10.10.10.0/24 |
+---------+---------------+
|    2    | 10.20.20.0/24 |
+---------+---------------+

SELECT * FROM next_hop;
+-------+---------+------------+-------+
| rowid | nlri_id | address    | state |
+-------+---------+------------+-------+
|   1   |    1    | 3.59.0.254 |   0   |
+-------+---------+------------+-------+
|   2   |    2    | 3.59.0.254 |   1   |
+-------+---------+------------+-------+

'''