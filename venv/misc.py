from dateHandler import *
def print_menu():
    """
    Method print a menu
    :return: nothing
    """
    print("1: print all customers details\n2: print all projects\n3: add a new customer\n4: add a new project\n5: exit")

def get_queries(index, cust_id, proj_id):
    """
    Method receive an index of query and 2 values and return a string accordingly
    :param index: query number
    :param cust_id: cust_id value in customers table
    :param proj_id: proj_id value in projects table
    :return: a string containing a SQL query
    """
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
