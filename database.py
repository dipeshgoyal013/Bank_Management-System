#Database Management banking
import mysql.connector as sql

# Establishing the connection
mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="bank"
)

# Creating a cursor object
cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

# Creating the customer table if it doesn't exist
def createcustomertable():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers 
        (username VARCHAR(20),
        password VARCHAR(20),
        name VARCHAR(20),
        age INTEGER,
        city VARCHAR(20),
        balancee INTEGER NOT NULL,
        account_NUMBER INTEGER,
        status BOOLEAN)
    ''')

# Committing the changes
mydb.commit()

if __name__ == "__main__":
    createcustomertable()