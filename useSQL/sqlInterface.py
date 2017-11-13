import sqlite3
import sys


class UseSqlite:
    con = None
    db = ""

    def __init__(self, thisdb=""):
        self.db = thisdb

    def createDatabase(self, dbfile):
        try:
            self.con = sqlite3.connect(dbfile)

        except sqlite3.Error, e:
            self.handleError(e)

        finally:
            self.closeConnection()

    def retrieveMultipleRows(self, myquery):
        self.con = sqlite3.connect(self.db)
        try:
            cur = self.con.cursor()
            cur.execute(myquery)
            data = cur.fetchall()

        except sqlite3.Error, e:
            self.handleError(e)

        finally:
            self.closeConnection()
            return data

    def retrieveOneRow(self, myquery):
        data = ""
        self.con = sqlite3.connect(self.db)
        try:
            cur = self.con.cursor()
            cur.execute(myquery)
            data = cur.fetchone()

        except sqlite3.Error, e:
            self.handleError(e)

        finally:
            self.closeConnection()
            return data


    def createTable(self, tablecommand):
        self.con = sqlite3.connect(self.db)
        try:
            self.con.execute(tablecommand)

        except sqlite3.Error, e:
            self.handleError(e)

        finally:
            self.closeConnection()

    def insertFullRows(self, tablename, myrowslistoftuples):
        ## should allow for 1 row or multiple
        if type(myrowslistoftuples[0]) is tuple:
            numquestionmarks = len(myrowslistoftuples[0])
        else:
            numquestionmarks = len(myrowslistoftuples)
        questionmarks = self.parameterized(numquestionmarks)

        sql = "insert into " + tablename + " values " + questionmarks

        self.con = sqlite3.connect(self.db)
        try:
            c = self.con.cursor()
            c.executemany(sql,myrowslistoftuples)
            self.con.commit()

        except sqlite3.Error, e:
            self.handleError(e)

        finally:
            self.closeConnection()

    @staticmethod
    def parameterized(numq):
        questionmarks = "("
        i = 1
        while i < numq:
            questionmarks += "?,"
            i+=1
        questionmarks += "?)"
        return questionmarks

    def closeConnection(self):
        if self.con:
            self.con.close()

    @staticmethod
    def handleError(e):
        print "Error %s:" % e.args[0]
        sys.exit(1)
