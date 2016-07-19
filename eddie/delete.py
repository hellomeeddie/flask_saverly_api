#Written by Eddie Hwang (Ed. Daniel Engelberth)
from py2neo import authenticate, Graph, Node, Relationship

#DEL_TYPE =
def delete (graph, DEL_TYPE, currentUser, delItem):

    #del User
    if DEL_TYPE == "User":
        #removes second layer relationships
        graph.run("MATCH (u:User {userName: {currentUser}})-[r]-(data)-[r2]-(data2) DELETE r,data,r2,data2", currentUser=currentUser)
        #removes first layer relationships + User node
        graph.run("MATCH (u:User {userName: {currentUser}})-[r]-(data) DELETE u,r,data", currentUser=currentUser)

    #del Account
    elif DEL_TYPE == "Account":
        graph.run("MATCH (User {userName: {currentUser}})-[r]->(a:Account)-[r2]->(data) WHERE a.name={delItem} DELETE r,a,r2,data", currentUser=currentUser, delItem=delItem)

    #del Transaction
    elif DEL_TYPE == "Transaction":
        # removes transaction relationships
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(Account)-[r:HAS]->(t:Transaction) WHERE t.name={delItem} DELETE r,t", currentUser=currentUser, delItem=delItem)

    #del Goal
    elif DEL_TYPE == "Goal":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(g:Goal) WHERE g.name={delItem} DETACH DELETE g", currentUser=currentUser, delItem=delItem)

    #del Wish
    elif DEL_TYPE == "Wish":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(w:Wish) WHERE w.name={delItem} DETACH DELETE w", currentUser=currentUser, delItem=delItem)

    #del Bill
    elif DEL_TYPE == "Bill":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(b:Bill) WHERE b.name={delItem} DETACH DELETE b", currentUser=currentUser, delItem=delItem)

    #del Budget
    elif DEL_TYPE == "Budget":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(b:Budget) WHERE b.name={delItem} DETACH DELETE b", currentUser=currentUser, delItem=delItem)

    else:
        raise ValueError("DEL_TYPE must be a type of node {'User','Goal','Transaction', etc.")

#authenticate("localhost:7474", "neo4j", "neo")
#graph = Graph("http://localhost:7474/db/data/")
