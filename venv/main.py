from dbHandler import *
from misc import *
import random as r

def main():
    choice = 0
    db1 = DbHandler('localhost', 'root', None, 'company', cursors.DictCursor)
    while choice != '5':
        print_menu()
        choice = input()
        if choice == '1': # print all customers
            db1.execute_query(get_queries(1, 0, 0), "SELECT", "customers")
        elif choice == '2': # print all projects
            db1.execute_query(get_queries(2, 0, 0), "SELECT", "projects")
        elif choice == '3': # add a new customer
            cust_id = r.randint(1, 99999)
            while db1.search_query(cust_id, get_queries(3, cust_id, 0), "Customer #", "cust_id"): # loop while cust_id exist
                cust_id = r.randint(1, 99999)
            db1.execute_query(get_queries(5, cust_id, 0), "INSERT", "customers")  # execute insert new customer query
        elif choice == '4': # add a new project
            cust_id = input("Enter customer id: ")
            try:
                cust_id = int(cust_id)  # check if cust_id is an int
                if db1.search_query(cust_id, get_queries(3, cust_id, 0), "Customer #", "cust_id"):  # check if customer_id exits
                    proj_id = r.randint(1, 99999)
                    while db1.search_query(proj_id, get_queries(4, 0, proj_id), "Project #", "proj_id"): # loop while proj_id exist
                        proj_id = r.randint(1, 99999)
                    db1.execute_query(get_queries(6, cust_id, proj_id), "INSERT", "projects")  # execute insert new project query
            except ValueError:
                print("invalid input!")
        elif choice == '5':
            print("Exiting...")
        else:
            print("invalid option, please try again!")

if __name__ == "__main__":
    main()
