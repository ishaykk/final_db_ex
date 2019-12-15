from dbHandler import *
import random as r
def get_random_num():
    random = r.randint()*100+1
    print(random)
    return random

def main():
    choice = input('''
    1: print all customers details
    2: print all projects
    3: add a new customer
    4: add a new project
    5: exit 
    ''')
    db1 = dbHandler('127.0.0.1', 'root', None, 'company', cursors.DictCursor)
    
    queries = ["SELECT * FROM customers", "SELECT * FROM projects", "SELECT cust_id FROM customers", "SELECT proj_id FROM projects"]
    while(choice !='5'):
        if(choice == '1'):
            db1.execute_query(queries[0])
        if(choice == '2'):
            db1.execute_query(queries[1])
        if(choice == '3'):
            db1.execute_query(queries[0], get_random_num())







