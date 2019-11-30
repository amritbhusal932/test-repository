from flask import Flask,request, jsonify, render_template, request, make_response
from flask_restful import Api, Resource
from flask_mysqldb import MySQL

app=Flask(__name__)
api=Api(app)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'product'
database=MySQL(app)

prod=[]

class Products(Resource):
	def get(self):
		cur=database.connection.cursor()
		cur.execute("Select * from product")		
		data=cur.fetchall()
		for row in data:
			json_data= {'id': row[0], 'name' : row[1],'price': row[2]}
			prod.append(json_data)
		cur.connection.commit()
		cur.close()
		return prod

	def post(self,_id):
		self.id=_id
		cur=database.connection.cursor()
		cur.execute('select prod_name, prod_price from product where prod_id=self.id');

api.add_resource(Products,'/')

if __name__=='__main__':
	app.run(debug=True)
