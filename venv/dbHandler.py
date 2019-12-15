from pymysql import *
class db:
    def init(self, conn_host, conn_user, conn_pw, conn_db, conn_cursor):
        self.host = conn_host
        self.user = conn_user
        self.password = conn_pw
        self.db = conn_db
        self.cursor = conn_cursor
        self.connection = None

    def db_connection(self):
        try:
            self.connection = connect(host=self.host, user=self.user, password = self.password, db = self.db, cursorclass = self.cursor)
    def execute_query(self, query, num):
        if(connection):
            with connection.cursor() as cursor:
                cursor.execute(query)
                values = cursor.fetchall()  # Saving a list of dictionaries where each dictionary is a record
                print("%s" % values)  # Get all records (fetchall)
                # for value in values:
                #     print(value['first_name'])
                # print("The amount of students:", cursor.rowcount)  # Count the amount of rows being affected