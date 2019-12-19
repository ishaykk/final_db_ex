from pymysql import *
from tabulate import tabulate # to print sql tables

class DbHandler:
    def __init__(self, conn_host, conn_user, conn_pw, conn_db, conn_cursor):
        """
        DatabaseHandler constructor
        :param connection_host: Host to connect to
        :param connection_user: Username to connect with
        :param connection_password: Password to connect with
        :param connection_db: Database to connect to
        :param connection_cursor: Cursor to work with
        """
        self.host = conn_host
        self.user = conn_user
        self.password = conn_pw
        self.db = conn_db
        self.cursor = conn_cursor
        self.connection = None

    def db_connection(self):
        """
        Method is responsible for database connection process
        :return: No return value
        """
        try:
            self.connection = connect(host=self.host, user=self.user, password = self.password, db = self.db, cursorclass = self.cursor)
        except MySQLError:
            print("DB Error")

    def execute_query(self, query, type_of_query, table):
        """
        Method executes a given query
        :param query: Query to execute
        :param type_of_query: "SELECT" or "INSERT"
        :param table: Name of the table
        :return: True if the query was executed successfully and False if not
        """
        try:
            self.db_connection()
            if self.connection is not None:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    if type_of_query == "SELECT":
                        res = cursor.fetchall()  # Saving a list of dictionaries where each dictionary is a record
                        headers = {element: element for element in {field[0] for field in cursor.description}} # tabulate requires a dict (each header has key and value)
                        print(tabulate(res, headers=headers, tablefmt='grid')) # print table with nice style
                    elif type_of_query == "INSERT": # INSERT query, commit is required
                        self.connection.commit()
        except IntegrityError:
            print("A new record couldn't be added")
            return False
        finally:
            self.close_connection()  # Closing the opened connection
        return True

    def search_query(self, num, query, table, field):
        """
            Method executes a "SELECT" query
            :param num: value to search
            :param query: Query to execute
            :param type_of_query: "SELECT" or "INSERT"
            :param field: name of column
            :return: True if the query was executed successfully and the "num" was found in column "field", false otherwise
            """
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
            exit()
        finally:
            self.close_connection()  # Closing the opened connection

    def close_connection(self):
        """
        Method is responsible for closing a database connection
        :return: No return value
        """
        if self.connection is not None:
            self.connection.close()
