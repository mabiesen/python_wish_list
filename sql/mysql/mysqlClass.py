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

    # data is provided as an object
    def insert_into_links_table(self,tablename,data):
        query_placeholders = ', '.join(['%s'] * len(data))
        query_columns = ', '.join(list(data.keys()))
        try:
           statement = ''' INSERT INTO table (%s) VALUES (%s) ''' %(query_columns, query_placeholders)
           self.cur.execute(statement, list(data.values()))
           self.db.commit()
        except Exception as e:
           self.db.rollback()
           print("FAIL")
           print(e)

    def close(self):
        self.db.close()
