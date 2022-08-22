from flask import Flask
from flask import render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
	with sql.connect('db.db') as con:
		tmp = con.execute('SELECT nlri.net,next_hop.address,next_hop.state FROM next_hop JOIN nlri ON nlri.rowid = next_hop.nlri_id')
		result = tmp.fetchall()
	return render_template('bgp_table.html',result=result)

app.run(host='localhost',port=5001)