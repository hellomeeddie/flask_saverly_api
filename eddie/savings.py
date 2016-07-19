from flask import Flask,request,json
from py2neo import authenticate,Graph
from access import access
from delete import delete
from modify import modify
from insert import insert
app = Flask(__name__)

@app.route('/savings', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saving():
    jsonData = request.get_json(cache=False)
    user=jsonData["userName"]
    type = "Goal"
    if request.method =='GET':
        getData = access(graph, type, user, user)
    elif request.method=='POST':
        postData = [jsonData["userName"], jsonData["savingsName"], jsonData["amount"], jsonData["downpay"],jsonData["term"],jsonData["description"]]
        insert(graph,type,postData)
    elif request.method=='PUT':
        current=["currentItem"]
        mod = jsonData["modItem"]
        modify(graph,type,user,current,mod)
    elif request.method=='DELETE':
        delItem=jsonData["delItem"]
		delete(graph,type,user,delItem)
    return 'OK'

@app.route('/transactions', methods=['GET', 'POST', 'PUT', 'DELETE'])
def transaction():
    jsonData = request.get_json(cache=False)
    user=jsonData["userName"]
    type = "Transaction"
    if request.method =='GET':
        getData = access(graph, type, user, user)
    elif request.method=='POST':
        postData = [jsonData["userName"], jsonData["transName"], jsonData["transDate"], jsonData["transLocation"],jsonData["transAmount"]]
        insert(graph,type,postData)
    elif request.method=='PUT':
        current=["currentItem"]
        mod = jsonData["modItem"]
        modify(graph,type,user,current,mod)
    elif request.method=='DELETE':
        delItem=jsonData["delItem"]
		delete(graph,type,user,delItem)
    return 'OK'

if __name__ == '__main__':
    authenticate("localhost:7474", "neo4j", "neo")
    graph = Graph("http://localhost:7474/db/data/")
    app.run(debug=True)