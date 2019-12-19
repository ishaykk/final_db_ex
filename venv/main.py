from dbHandler import *
import random as r
def get_random_num():
    random = r.randint()*100+1
    print(random)
    return random

def print_menu():
    print('''
        1: print all customers details
        2: print all projects
        3: add a new customer
        4: add a new project
        5: exit 
        ''')
def get_queries(index):
    if index == 1: return "SELECT * FROM customers"
    elif index == 2: return "SELECT * FROM projects"
    elif index == 3: return "SELECT cust_id FROM customers"
    elif index == 4: return "INSERT INTO customers(cust_id, first_name, last_name, phone_num) VALUES(num, '%s', '%s', '%s')" % (
                   input("Enter first name"), input("Enter last name"), input("enter phone number")),
    elif index == 5: return "INSERT INTO projects(proj_id, proj_name, start_date, cust_id) VALUES(num, '%s', '%s', '%s')" % (
                   input("Enter project name"), input("Enter prject start date"), input("enter customer id"))
    else:
        print("index out of bound")

def main():
    choice = 0
    db1 = db('127.0.0.1', 'root', None, 'company', cursors.DictCursor)

    while choice !='5':
        print_menu()
        choice = input()
        if choice == '1':
            db1.execute_query(get_queries(1), "SELECT", "customers", 0)
        elif choice == '2':
            db1.execute_query(get_queries(1), "SELECT", "projects", 0)
        elif choice == '3':
            num = get_random_num()
            while(db1.search_cust(num, get_queries(2), "Customer #")):
                num = get_random_num()
            db1.execute_query(get_queries(4), "INSERT", r)
        elif choice == '4':
            num = get_random_num()
            while (not db1.search_cust(num, get_queries(3), "Project #")):
                num = get_random_num()
            db1.execute_query(get_queries(5), "INSERT", r)
        elif choice == '5':
            print("Exiting...")
        else:
            print("invalid option, please try again!\n")






if __name__ == "__main__":
    main()












