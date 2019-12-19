from dbHandler import *
from Date import *
import random as r


def get_random_num():
    random = r.randint(1, 99999)
    print(random)
    return random


def print_menu():
    print("1: print all customers details\n2: print all projects\n3: add a new customer\n4: add a new project\n5: exit")


def get_queries(index, num):
    if index == 1:
        return "SELECT * FROM customers"
    elif index == 2:
        return "SELECT * FROM projects"
    elif index == 3:
        return "SELECT cust_id FROM customers WHERE cust_id = %d" % int(num)
    elif index == 4:
        return "SELECT proj_id FROM projects WHERE proj_id = %d" % int(num)
    elif index == 5:
        return "INSERT INTO customers(cust_id, first_name, last_name, phone_num) VALUES('%d', '%s', '%s', '%s')" % (
        num, input("Enter first name"), input("Enter last name"), input("enter phone number"))
    elif index == 6:
        return "INSERT INTO projects(proj_id, proj_name, start_date, cust_id) VALUES('%d', '%s', '%s', '%s')" % (num,
                                                                                                                 input(
                                                                                                                     "Enter project name"),
                                                                                                                 "2019-12-15",
                                                                                                                 input(
                                                                                                                     "enter customer id"))
    else:
        print("index out of bound")


def date_input():
    day, month, year = map(int, input('Enter start date in DD/MM/YYYY format').split('/'))
    date1 = Date(day, month, year)
    print(date1.print_date())


def main():
    choice = 0
    db1 = DbHandler('localhost', 'root', None, 'company', cursors.DictCursor)

    while choice != '5':
        print_menu()
        choice = input()
        if choice == '1':
            db1.execute_query(get_queries(1, 0), "SELECT", "customers")
        elif choice == '2':
            db1.execute_query(get_queries(2, 0), "SELECT", "projects")
        elif choice == '3':
            num = get_random_num()
            print(get_queries(3, num))
            while db1.search_cust(num, get_queries(3, num), "Customer #", "cust_id"):
                num = get_random_num()
            db1.execute_query(get_queries(5, num), "INSERT", "customers")  # execute insert new customer query
        elif choice == '4':
            cust_id = input("Enter customer id")
            if db1.search_cust(cust_id, get_queries(3, cust_id), "Customer #", "cust_id"):  # check if customer_id exits
                print(get_queries(3, cust_id))
                print(cust_id, " was found!!!")
                num = get_random_num()  # generate a random number for proj_id
                while not db1.search_cust(num, get_queries(4, 0), "Project #",
                                          "proj_id"):  # loop till proj_id does not exist
                    num = get_random_num()
                db1.execute_query(get_queries(6, num), "INSERT", "projects")  # execute insert new project query
        elif choice == '5':
            print("Exiting...")
        else:
            print("invalid option, please try again!\n")


if __name__ == "__main__":
    main()












