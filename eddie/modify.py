#Written by Eddie Hwang (Ed. Daniel Engelberth)
from py2neo import authenticate, Graph, Node, Relationship


def modify(graph, MOD_TYPE, currentUser, currentItem, modItem):
    # mod User
    if MOD_TYPE == "User":
        graph.run("MATCH (u:User {userName: {currentUser}}) SET u.%s={modItem}" %currentItem, currentUser=currentUser, currentItem=currentItem, modItem=modItem)

    # mod Account
    elif MOD_TYPE == "Account":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(a:Account) SET a.%s={modItem}" %currentItem, currentUser=currentUser, currentItem=currentItem, modItem=modItem)

    # mod Transaction
    elif MOD_TYPE == "Transaction":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(Account)-[:HAS]->(t:Transaction) SET t.%s={modItem}" %currentItem, currentUser=currentUser, currentItem=currentItem, modItem=modItem)

    # mod Goal
    elif MOD_TYPE == "Goal":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(g:Goal) SET g.%s={modItem}" %currentItem,  currentUser=currentUser, currentItem=currentItem, modItem=modItem)

    # mod Wish
    elif MOD_TYPE == "Wish":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(w:Wish) SET w.%s={modItem}" %currentItem, currentUser=currentUser, currentItem=currentItem, modItem=modItem)

    # mod Bill
    elif MOD_TYPE == "Bill":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(b:Bill) SET b.%s={modItem}" %currentItem, currentUser=currentUser, currentItem=currentItem, modItem=modItem)

    # mod Budget
    elif MOD_TYPE == "Budget":
        graph.run("MATCH (User {userName: {currentUser}})-[:HAS]->(b:Budget) SET b.%s={modItem}" %currentItem, currentUser=currentUser, currentItem=currentItem, modItem=modItem)

    else:
        raise ValueError("MOD_TYPE must be a type of node {'User','Goal','Transaction', etc.")