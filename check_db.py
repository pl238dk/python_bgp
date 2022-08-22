import sqlite3 as sql

def do():
	with sql.connect('db.db') as con:
		o = con.execute('SELECT * FROM nlri')
		result = o.fetchall()
		print 'NLRI : '
		for i in result:
			print i
		o = con.execute('SELECT * FROM next_hop')
		result = o.fetchall()
		print 'NEXT_HOP : '
		for i in result:
			print i
	return

if __name__ == '__main__':
	do()