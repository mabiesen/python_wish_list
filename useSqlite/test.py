import sqliteInterface

x = sqliteInterface.UseSqlite("mydb.db")

def makeDb():
    x.createDatabase("mydb.db")

def makeTable():
    x.createTable("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT, Color TEXT);")

def insertRows():
    x.insertFullRows("Friends",[(3,"jake", "blue"),(4,"john","red")])

def queryOneRowData():
    return x.retrieveOneRow('''Select * from Friends''')

def queryMultiple():
    return x.retrieveMultipleRows('''Select * from Friends''')

def parameterd():
    print(x.parameterized(4))

print(queryMultiple())

