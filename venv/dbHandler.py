from pymysql import *
class db:
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
    def execute_query(self, query, type_of_query, table, num):
        try:
            self.db_connection()
            if self.connection is not None:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    if type_of_query == "SELECT":
                        values = cursor.fetchall()  # Saving a list of dictionaries where each dictionary is a record
                        lst = [field[0] for field in cursor.description]
                        print()
                        for value in values:
                            if table == "customers":
                                print(value['cust_id'],'\t\t', value['first_name'],'\t\t', value['last_name'],'\t\t', value['phone_num'])
                            elif table == "projects":
                                print("project id:", value['proj_id'], "start date:", value['start_date'], "cust id:",
                                      value['cust_id'])
                    elif type_of_query == "INSERT": # type 3/4 = INSERT query, commit is required
                        self.connection.commit()
                    # print("The amount of students:", cursor.rowcount)  # Count the amount of rows being affected\
        except IntegrityError:
            print("A new record couldn't be added")
            return False
        finally:
            self.close_connection()  # Closing the opened connection
        return True

    def search_cust(self, id, query, table):
        try:
            self.connect_database()
            if self.connection is not None:  # If the database connection was established successfully
                self.connection.cursor().execute(query)
                result = cursor.fetchone()
                if result ==  id:
                    print(table + id +" was found")
                    return True
                print(table + id + " wasn't found!")
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