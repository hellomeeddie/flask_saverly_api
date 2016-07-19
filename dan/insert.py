#Daniel Engelberth
from py2neo import authenticate, Graph, Node, Relationship


#Params: t - String, type of node being inserted (User, Goal, Budget, etc.), info - Array, array of all other info to be used to set up node properties
#Returns: None
#Description: Inserts a new node into the Neo4j database that corresponds with the requested data type as well as any required relationships
def insert(graph, t, info):
    if t == "User":
        graph.run("CREATE (n:User {userName: {userName},firstName: {firstName},lastName: {lastName},email: {email},password: {password}})",userName=info[0],firstName=info[1],lastName=info[2],email=info[3],password=info[4])
    elif t == "Goal":
        graph.run("CREATE (n:Goal {name: {name},amount: {amount},downpay: {downpay},term: {term},description: {description}})",name=info[0],amount=info[1],downpay=info[2],term=info[3],description=info[4])
        for category in info[5]:
            insert(graph, "Category", category)
            graph.run("MATCH (a:Goal),(b:Category) WHERE a.name = {name} AND b.name = {category} CREATE (a)-[r:HAS]->(b)",name=info[0],category=category)
        graph.run("MATCH (a:User),(b:Goal) WHERE a.userName = {userName} AND b.name = {name} CREATE (a)-[r:HAS]->(b)",userName=info[5],name=info[0])
    elif t == "Budget":
        graph.run("CREATE (n:Budget {name: {name},amount: {amount},startDate: {startDate},endDate: {endDate},description: {description}})",name=info[0],amount=info[1],startDate=info[2],endDate=info[3],description=info[4])
        for category in info[5]:
            insert(graph, "Category", category)
            graph.run("MATCH (a:Budget),(b:Category) WHERE a.name = {name} AND b.name = {category} CREATE (a)-[r:HAS]->(b)",name=info[0],category=category)
        graph.run("MATCH (a:User),(b:Budget) WHERE a.userName = {userName} AND b.name = {name} CREATE (a)-[r:HAS]->(b)",userName=info[6],name=info[0])
    elif t == "Wish":
        graph.run("CREATE (n:Wish {name: {name},purchaseLink: {purchaseLink},date: {date},description: {description}})",name=info[0],purchaseLink=info[1],date=info[2],description=info[3])
        for category in info[4]:
            insert(graph, "Category", category)
            graph.run("MATCH (a:Wish),(b:Category) WHERE a.name = {name} AND b.name = {category} CREATE (a)-[r:HAS]->(b)",name=info[0],category=category)
        graph.run("MATCH (a:User),(b:Wish) WHERE a.userName = {userName} AND b.name = {name} CREATE (a)-[r:HAS]->(b)",userName=info[5],name=info[0])
    elif t == "Transaction":
        graph.run("CREATE (n:Transaction{name: {name},amount: {amount},date: {date},location: {location}})",name=info[0],amount=info[1],date=info[2],location=info[3])
        for category in info[4]:
            insert(graph, "Category", category)
            graph.run("MATCH (a:Transaction),(b:Category) WHERE a.name = {name} AND b.name = {category} CREATE (a)-[r:HAS]->(b)",name=info[0],category=category)
        insert(graph, "Merchant",info[5])
        graph.run("MATCH (a:Transaction),(b:Merchant) WHERE a.name = {name} AND b.name = {merchantName} CREATE (a)-[r:HAS]->(b)",name=info[0],merchantName=info[5])
        graph.run("MATCH (a:User),(b:Transaction) WHERE a.userName = {userName} AND b.name = {name} CREATE (a)-[r:HAS]->(b)",userName=info[7],name=info[0])
    elif t == "Bill":
        graph.run("CREATE (n:Bill {name: {name},amount: {amount},startDate: {startDate},endDate: {endDate},description: {description},freq: {freq}})",name=info[0],amount=info[1],startDate=info[2],endDate=info[3],description=info[4],freq=info[5])
        for category in info[6]:
            insert(graph, "Category", category)
            graph.run("MATCH (a:Bill),(b:Category) WHERE a.name = {name} AND b.name = {category} CREATE (a)-[r:HAS]->(b)",name=info[0],category=category)
        graph.run("MATCH (a:User),(b:Bill) WHERE a.userName = {userName} AND b.name = {name} CREATE (a)-[r:HAS]->(b)",userName=info[7],name=info[0])
        """elif t == "Tag":
        graph.run("MERGE (t:Tag { name: {name} })",name=info)"""
    elif t == "Merchant":
        graph.run("MERGE (t:Merchant { name: {name} })",name=info)
    elif t == "Category":
        graph.run("MERGE (c:Category {name: {name})",name=info)
    else:
        raise ValueError("t must be a type of node {'User','Goal','Transaction', etc.")