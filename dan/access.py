#Daniel Engelberth
from py2neo import authenticate, Graph, Node, Relationship


#Params: t - String, type of node being accessed (User, Goal, Budget, etc.), name - name of target node, username - name of accessing user (may be same as name in case of user access)
#Returns: None (Not yet finished)
#Description: Inserts a new node into the Neo4j database that corresponds with the requested data type as well as any required relationships
def access(graph, t, username, name):
    if t == "User":
        info = graph.data("MATCH (u:User {userName: {name}}) RETURN u", name=name)
    elif t == "Goal":
        info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(g:Goal{name: {name}}) RETURN g", currentUser=username, name=name)
    elif t == "Budget":
        info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(b:Budget{name: {name}}) RETURN b", currentUser=username, name=name)
    elif t == "Wish":
        info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(w:Wish{name: {name}}) RETURN w", currentUser=username, name=name)
    elif t == "Transaction":
        info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(t:Transaction{name: {name}}) RETURN t", currentUser=username, name=name)
    elif t == "Bill":
        info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(b:Bill{name: {name}}) RETURN b", currentUser=username, name=name)
        #elif t == "Tag":
        #info = graph.data("MATCH (t:Tag{name: {name}}) RETURN t", name=name)
    elif t == "Merchant":
        info = graph.data("MATCH (m:Merchant {name: {name}}) RETURN m", name=name)
    elif t == "Category":
        info = graph.data("MATCH (c:Category{name: {name}}) RETURN c", name=name)
    else:
        raise ValueError("t must be a type of node {'User','Goal','Transaction', etc.")
    print (info)

def accessAll(graph, t, username):
    if t == "User":
        info = graph.data("MATCH (u:User) RETURN u")
    elif (username != ""):
        if t == "Goal":
            info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(g:Goal) RETURN g", currentUser=username)
        elif t == "Budget":
            info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(b:Budget) RETURN b", currentUser=username)
        elif t == "Wish":
            info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(w:Wish) RETURN w", currentUser=username)
        elif t == "Transaction":
            info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(t:Transaction) RETURN t", currentUser=username)
        elif t == "Bill":
            info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(b:Bill) RETURN b", currentUser=username)
            #elif t == "Tag":
            #info = graph.data("MATCH (t:Tag{name: {name}}) RETURN t", name=name)
        elif t == "Merchant":
            info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(m:Merchant) RETURN m", currentUser=username)
        elif t == "Category":
            info = graph.data("MATCH (u:User {userName: {currentUser}})-[:HAS]->(c:Category) RETURN c", currentUser=username)
        else:
            raise ValueError("t must be a type of node {'User','Goal','Transaction', etc.")
    else:
        if t == "Goal":
            info = graph.data("MATCH (g:Goal) RETURN g")
        elif t == "Budget":
            info = graph.data("MATCH (b:Budget) RETURN b", currentUser=username)
        elif t == "Wish":
            info = graph.data("MATCH (w:Wish) RETURN w", currentUser=username)
        elif t == "Transaction":
            info = graph.data("MATCH (t:Transaction) RETURN t", currentUser=username)
        elif t == "Bill":
            info = graph.data("MATCH (b:Bill) RETURN b", currentUser=username)
            #elif t == "Tag":
            #info = graph.data("MATCH (t:Tag{name: {name}}) RETURN t", name=name)
        elif t == "Merchant":
            info = graph.data("MATCH (m:Merchant) RETURN m")
        elif t == "Category":
            info = graph.data("MATCH (c:Category) RETURN c")
        else:
            raise ValueError("t must be a type of node {'User','Goal','Transaction', etc.")
    print (info)