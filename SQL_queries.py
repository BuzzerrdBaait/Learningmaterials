import mysql

from mysql.connector.errors import Error




class SQLDatabase:
    
   
    def __init__(self, dbname, host, user, password):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
 
    def connect(self):
        try:
            self.database = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.dbname
            )
            print("Connected to database successfully!")
        except Error as e:
            print("Failed to connect to the database: {}".format(e))
 
    def insert(self, query):
        cursor = self.database.cursor()
        try:
            cursor.execute(query)
            self.database.commit()
            print("Data inserted successfully!")
        except Error as e:
            print("Failed to insert data: {}".format(e))
 
    def query(self, query):
        cursor = self.database.cursor()
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("Data queried successfully!")
            return records, print(records)
        except Error as e:
            print("Failed to query data: {}".format(e))
 

 
    def delete(self, query):
        cursor = self.database.cursor()
        try:
            cursor.execute(query)
            self.database.commit()
            print("Data deleted successfully!")
        except Error as e:
            print("Failed to delete data: {}".format(e))
 
    def disconnect(self):
        if self.database.is_connected():
            self.database.close()
            print("MySQL connection is closed")

db = SQLDatabase('DATABASE_NAME', 'LOCAL_HOST or IP ADDRESS', 'USER_NAME', 'PASSWORD')######################<<<<<<DATABASE INFOOO!!!!!


Table= ("NEEEEEEEEEEWWWWW_TAAAAAAAAAABBBBBBBBBLEEEEEEEEEEE")
column1=("Username")
column2=("User id")
column3=("comment")
column4=("comment_id")
search1=("A")
search2=("Jo")
search3=1
search4=5
searchoptionslist=['%','_']
zero=searchoptionslist[0]
one=searchoptionslist[1]
p1=['NEWTABLE']


db.connect()

class call_queries:

    def search_table(): 
        query = "SELECT * FROM {}".format(Table)
        print("This is searching {} and printing the results".format(Table))
        return query, (db.query(query))

    
    def search_column_startswith(): 
        query = "SELECT * FROM {} WHERE {} LIKE '{}{}{}'".format(Table,column1,one, search1, zero)
        print("This is searching {} for {} and printing results in the {} column".format(Table, search1, column1))
        return query, (db.query(query))
    
    def search_column_contains():             
        query = "SELECT * FROM {} WHERE {} LIKE '%{}%'".format(Table,column1,search1)
        print("This is searching {} for {} and printing results in the {} column".format(Table, search1, column1))
        return query, (db.query(query))
    
    def search_column_not_contains(): 
        query = "SELECT * FROM {} WHERE {} NOT LIKE '%{}%'".format(Table,column1,search1)
        print("This is searching {} for anything not containing {} and printing results in the {} column".format(Table, search1, column4))
        return query, (db.query(query))
    
                
    
    def create_table_if_not_exists():
        tableinp=input("What will your table's name be?")
        query = ("CREATE TABLE IF NOT EXISTS {} (column1 INT,column2 VARCHAR(255),column3 DATETIME);").format(tableinp)
        print("This is creating the table {} if it does not exist".format(tableinp))
        return query, (db.query(query))

    

call_queries.create_table_if_not_exists()
