from py2neo import authenticate, Graph, Node, Relationship
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from access import *
from insert import insert
from modify import modify
from delete import delete
import json


noOfVisitors = 0

webapp = Flask(__name__)
api = Api(webapp)

@api.resource('/users')
class api_users(Resource):
	def get(self):
		jsonData = request.get_json(cache=False)
		type = "User"
		#user = jsonData["userName"]
		#name = jsonData["name"] //same as username
		nodeData = accessAll(graph, type, "")
		print (jsonify(nodeData))
		return nodeData
	def post(self):
		#retureve json data from Request and store it in local variable
		jsonData = request.get_json(cache=False)
		type= "User"
		info = [jsonData["userName"], jsonData["firstName"], jsonData["lastName"], jsonData["email"], jsonData["password"]]
		#print(json.dumps(jsonData, indent=2, sort_keys=True))
		#print(type)
		insert(graph, type, info)
	def put(self):
		jsonData = request.get_json(cache=False)
		type = "User"
		user = jsonData["userName"]
		current = jsonData["currentItem"]
		mod = jsonData["modItem"]
		modify(graph, type, user, current, mod)
	def delete(self):
		jsonData = request.get_json(cache=False)
		type = "User"
		user = jsonData["userName"]
		#delItem = jsonData["delItem"] //Same as username
		delete(graph, type, user, user)

"""@api.resource('/users/<id>')
class api_user(id):
	def get(self):
		jsonData = request.get_json(cache=False)
		type = "User"
		user = jsonData["userName"]
		name = jsonData["name"]
		nodeData = access(graph, type, id, id)
		return jsonify(nodeData)
	def post(self):
		#retureve json data from Request and store it in local variable
		jsonData = request.get_json(cache=False)
		type= "User"
		info = [jsonData["userName"], jsonData["firstName"], jsonData["lastName"], jsonData["email"], jsonData["password"]]
		#print(json.dumps(jsonData, indent=2, sort_keys=True))
		#print(type)
		insert(graph, type, info)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def put(self):
		jsonData = request.get_json(cache=False)
		type = "User"
		user = jsonData["userName"]
		current = jsonData["currentItem"]
		mod = jsonData["modItem"]
		modify(graph, type, user, current, mod)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def delete(self):
		jsonData = request.get_json(cache=False)
		type = "User"
		user = jsonData["userName"]
		delItem = jsonData["delItem"]
		delete(graph, user, delItem)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)"""

@api.resource('/users/bills')
class api_bills(Resource):
	def get(self):
		jsonData = request.get_json(cache=False)
		type = "Bill"
		user = jsonData["userName"]
		name = jsonData["name"]
		nodeData = accessAll(graph, type, user)
		return jsonify(nodeData)
	def post(self):
		#retureve json data from Request and store it in local variable
		jsonData = request.get_json(cache=False)
		type= "Bill"
		info = [jsonData["userName"], jsonData["firstName"], jsonData["lastName"], jsonData["email"], jsonData["password"]]
		#print(json.dumps(jsonData, indent=2, sort_keys=True))
		#print(type)
		insert(graph, type, info)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def put(self):
		jsonData = request.get_json(cache=False)
		type = "Bill"
		user = jsonData["userName"]
		current = jsonData["currentItem"]
		mod = jsonData["modItem"]
		modify(graph, type, user, current, mod)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def delete(self):
		jsonData = request.get_json(cache=False)
		type = "Bill"
		user = jsonData["userName"]
		delItem = jsonData["delItem"]
		delete(graph, user, delItem)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)

@api.resource('/users/budgets')
class api_budgets(Resource):
	def get(self):
		jsonData = request.get_json(cache=False)
		type = "Budget"
		user = jsonData["userName"]
		name = jsonData["name"]
		nodeData = accessAll(graph, type, user)
		return jsonify(nodeData)
	def post(self):
		#retureve json data from Request and store it in local variable
		jsonData = request.get_json(cache=False)
		type= "Budget"
		info = [jsonData["userName"], jsonData["firstName"], jsonData["lastName"], jsonData["email"], jsonData["password"]]
		#print(json.dumps(jsonData, indent=2, sort_keys=True))
		#print(type)
		insert(graph, type, info)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def put(self):
		jsonData = request.get_json(cache=False)
		type = "Budget"
		user = jsonData["userName"]
		current = jsonData["currentItem"]
		mod = jsonData["modItem"]
		modify(graph, type, user, current, mod)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def delete(self):
		jsonData = request.get_json(cache=False)
		type = "Budget"
		user = jsonData["userName"]
		delItem = jsonData["delItem"]
		delete(graph, user, delItem)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)

@api.resource('/users/wishes')
class api_wishes(Resource):
	def get(self):
		jsonData = request.get_json(cache=False)
		type = "Wish"
		user = jsonData["userName"]
		name = jsonData["name"]
		nodeData = accessAll(graph, type, user)
		return jsonify(nodeData)
	def post(self):
		#retureve json data from Request and store it in local variable
		jsonData = request.get_json(cache=False)
		type= "Wish"
		info = [jsonData["name"], jsonData["purchaseLink"], jsonData["date"], jsonData["description"], jsonData["password"]]
		#print(json.dumps(jsonData, indent=2, sort_keys=True))
		#print(type)
		insert(graph, type, info)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def put(self):
		jsonData = request.get_json(cache=False)
		type = "Wish"
		user = jsonData["userName"]
		current = jsonData["currentItem"]
		mod = jsonData["modItem"]
		modify(graph, type, user, current, mod)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def delete(self):
		jsonData = request.get_json(cache=False)
		type = "Wish"
		user = jsonData["userName"]
		delItem = jsonData["delItem"]
		delete(graph, user, delItem)
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)

if __name__=='__main__':
	authenticate("localhost:7474","neo4j","Gr4aphing1sG00d")
	graph = Graph("http://localhost:7474/db/data/") #place info here for online database when ready
	webapp.run(debug=True)


