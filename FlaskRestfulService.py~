from flask import Flask, jsonify, request
from flask_restful import Api, Resource

noOfVisitors = 0

webapp = Flask(__name__)
api = Api(webapp)

@api.resource('/hello')
class HelloWorld(Resource):
	def get(self):
		return 'Hello from API - get'
	def post(self):
		#retureve json data from Request and store it in local variable
		jsonData = request.get_json(cache=False)
		for key in jsonData:
			import json 
			print(json.dumps(jsonData, indent=2, sort_keys=True))
		global noOfVisitors
		noOfVisitors = noOfVisitors + 1
		return jsonify(totalVisits = noOfVisitors)
	def delete(self):
		return 'Hello from API - delete'

if __name__=='__main__':
	webapp.run(debug=True)



