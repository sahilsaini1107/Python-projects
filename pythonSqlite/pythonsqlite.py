# sqlite comes with pythonno need to insatll anythong
import sqlite3

# here we have created database "customer.db" but it is not permanent
connection = sqlite3.connect('customer.db')

# soo instead we use
# with this we can save our database to use it later
# connection = sqlite3.connect(' :memory: ')

# create a cursor(it is sort of like, it tells database what we want to do)
c = connection.cursor()

# create a table( """ """ with this type of colon we can write multiple line together to create table)
# sqlite is case sensitive
# sqlite has only 5 datatype i.e 
# integer
# null
# real (decimal)
# text
# blob (stored as it is ex. image)
# c.execute("""CREATE TABLE customers(
#     first_name text,
#     last_name text,
#     email text
# )""")



# add data to table(before this i am commenting above code as it is already executed.)

# c.execute("INSERT INTO customers VALUES ('Sahil', 'Saini', 'sohil170246@gmail.com')")


#insert many records in table(commenting above code to only run this)
# many_customer =[('saket', 'soni', 'saket@gmail.com'), ('preksha', 'bhandari', 'prekss@gamil.com'), ('aman', 'saini', 'aman@gmail.com')]
# c.executemany("INSERT INTO customers VALUES (?,?,?)" , many_customer)

# query the database
# c.execute("SELECT * FROM customers")
c.execute("SELECT rowid, * FROM customers")

# also we can now update and delete the records whit sql commands
# now we can use where clause, orderby to select any particular record


# we can use a variable to store this data and then for loop to format this data

# print(c.fetchall())
print(c.fetchone())







# add to database
connection.commit()


# close connection
connection.close()


