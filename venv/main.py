from dbHandler import *
from dateHandler import *
import random as r

def print_menu():
    print("1: print all customers details\n2: print all projects\n3: add a new customer\n4: add a new project\n5: exit")

def get_queries(index, cust_id, proj_id):
    if index == 1:
        return "SELECT * FROM customers"
    elif index == 2:
        return "SELECT * FROM projects"
    elif index == 3:
        return "SELECT cust_id FROM customers WHERE cust_id = %d" % (cust_id)
    elif index == 4:
        return "SELECT proj_id FROM projects WHERE proj_id = %d" % (proj_id)
    elif index == 5:
        return "INSERT INTO customers(cust_id, first_name, last_name, phone_num) VALUES('%d', '%s', '%s', '%s')" % (
        cust_id, input("Enter first name: "), input("Enter last name: "), input("Enter phone number: "))
    elif index == 6:
        return "INSERT INTO projects(proj_id, proj_name, start_date, cust_id) VALUES('%d', '%s', '%s', '%d')" % (
            proj_id, input("Enter project name: "), date_format(), cust_id)
    else:
        print("index out of bound")

def main():
    choice = 0
    db1 = DbHandler('localhost', 'root', None, 'company', cursors.DictCursor)

    while choice != '5':
        print_menu()
        choice = input()
        if choice == '1':
            db1.execute_query(get_queries(1, 0, 0), "SELECT", "customers")
        elif choice == '2':
            db1.execute_query(get_queries(2, 0, 0), "SELECT", "projects")
        elif choice == '3':
            num = r.randint(1, 99999)
            print(get_queries(3, num, 0))
            while db1.search_cust(num, get_queries(3, num, 0), "Customer #", "cust_id"):
                num = r.randint(1, 99999)
            db1.execute_query(get_queries(5, num, 0), "INSERT", "customers")  # execute insert new customer query
        elif choice == '4':
            cust_id = input("Enter customer id: ")
            try:
                cust_id = int(cust_id)
                if db1.search_cust(cust_id, get_queries(3, cust_id, 0), "Customer #", "cust_id"):  # check if customer_id exits
                    print(get_queries(3, cust_id, 0))
                    print(cust_id, " was found!!!")
                    proj_id = r.randint(1, 99999)
                    while db1.search_cust(proj_id, get_queries(4, 0, proj_id), "Project #", "proj_id"): # loop while proj_id exist
                        proj_id = r.randint(1, 99999)
                    print("inserting project #" + str(proj_id))
                    db1.execute_query(get_queries(6, cust_id, proj_id), "INSERT", "projects")  # execute insert new project query
            except ValueError:
                print("invalid input!")
        elif choice == '5':
            print("Exiting...")
        else:
            print("invalid option, please try again!\n")

if __name__ == "__main__":
    main()
