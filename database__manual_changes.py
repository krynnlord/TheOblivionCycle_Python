import os, sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

# # Create table
#result=cur.execute("CREATE TABLE inventory (id INT PRIMARY KEY, name TEXT, type TEXT, have INT) ")
#con.commit()
#con.close()


# # Insert
#result=cur.execute("insert into inventory (id, name, type, have) values(7, 'Dagger', 'weapon', 1)")
#con.commit()
#con.close()


# # Update Value
result=cur.execute("update inventory set id = 8 where name = 'Dagger'")
con.commit()
con.close()