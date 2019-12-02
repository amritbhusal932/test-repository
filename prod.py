from flask import Flask,request, jsonify, render_template, request, make_response
from flask_restful import Api, Resource
from flask_mysqldb import MySQL

app=Flask(__name__)
api=Api(app)



prod=[{'id' : 1,
      'name' : 'Chair',
      'price' : 230}]

class Products(Resource):
	def get(self):	
		return prod

	def post(self,_id):
		self.id=_id
		cur=database.connection.cursor()
		cur.execute('select prod_name, prod_price from product where prod_id=self.id');

api.add_resource(Products,'/')

if __name__=='__main__':
	app.run(debug=True)
