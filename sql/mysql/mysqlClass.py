# https://stackoverflow.com/questions/46499191/dynamic-mysql-insert-statement-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import MySQLdb

class Mysql:
    def __init__(self, uhost, uuser, upasswd, udb):
        self.db = MySQLdb.connect(host=uhost,    # your host, usually localhost
                             user=uuser,         # your username
                             passwd=upasswd,  # your password
                             db=udb)        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        self.cur = self.db.cursor()
        
        
    def print_all_data_in_table(self, tablename):
        # Use all the SQL you like
        self.cur.execute("SELECT * FROM " + tablename)

        # print all the first cell of all the rows
        for row in self.cur.fetchall():
            for x in range(0,len(row)):
                print(row[x])
            print("\n\n")
            

    # data is provided as an object
    def insert_into_links_table(self,tablename,data):
        query_placeholders = ', '.join(['%s'] * len(data))
        query_columns = ', '.join(list(data.keys()))
        try:
           statement = ''' INSERT INTO %s (%s) VALUES (%s) ''' %(tablename, query_columns, query_placeholders)
           self.cur.execute(statement, list(data.values()))
           self.db.commit()
        except Exception as e:
           self.db.rollback()
           print("FAIL")
           print(e)

    def close(self):
        self.db.close()
