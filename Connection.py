import mysql.connector
from mysql.connector import errorcode
import pandas as pd



#make MySQL connection object
class MYSQLConnection:
    def __init__(self):
        try:
            self.mydb=mysql.connector.connect(
                host="",
                user="",
                passwd="",
                database=""
                    )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        
    #call to make connection, returns a cursor which can be queried
    def getConnect(self):
        mycursor = self.mydb.cursor()
        return mycursor
    #call to close connection
    def closeConnection(self):
        self.mydb.close()


def getcsv():
    df = pd.read_csv('event_data_complete.csv', encoding = "ISO-8859-1")
    
    
    #this may need to be changed it will take the first row of csv and make each the column header
    
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    
    ###########################################
    return df



connect = MYSQLConnection()
mycursor = connect.getConnect()
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

df = getcsv()

print(df.head())

connect.closeConnection()
  
  
  
