from pymysql import *
from tabulate import tabulate

class DbHandler:
    def __init__(self, conn_host, conn_user, conn_pw, conn_db, conn_cursor):
        self.host = conn_host
        self.user = conn_user
        self.password = conn_pw
        self.db = conn_db
        self.cursor = conn_cursor
        self.connection = None

    def db_connection(self):
        try:
            self.connection = connect(host=self.host, user=self.user, password = self.password, db = self.db, cursorclass = self.cursor)
        except MySQLError:
            print("DB Error")

    def execute_query(self, query, type_of_query, table):
        try:
            self.db_connection()
            if self.connection is not None:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    if type_of_query == "SELECT":
                        res = cursor.fetchall()  # Saving a list of dictionaries where each dictionary is a record
                        headers = {element: element for element in {field[0] for field in cursor.description}} # tabulate require a dictionary (each header has a key and value)
                        print(tabulate(res, headers=headers, tablefmt='grid')) # print table with nice stlye
                    elif type_of_query == "INSERT": # type 3/4 = INSERT query, commit is required
                        self.connection.commit()
        except IntegrityError:
            print("A new record couldn't be added")
            return False
        finally:
            self.close_connection()  # Closing the opened connection
        return True

    def search_cust(self, num, query, table, field):
        try:
            self.db_connection()
            if self.connection is not None:  # If the database connection was established successfully
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchone()
                    print(type(result))
                    if result is not None and result[field] == num: # check if query result is None and pk equal to num
                        print(table + str(num), "was found")
                        return True
                    else:
                        print(table + str(num), "wasn't found")
                        return False
        except IntegrityError:
            print("A new record couldn't be added")
            return False
        finally:
            self.close_connection()  # Closing the opened connection
        return True

    def close_connection(self):
        """
        Method is responsible for closing a database connection
        :return: No return value
        """
        if self.connection is not None:
            self.connection.close()
