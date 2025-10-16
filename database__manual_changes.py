import os, sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

# # Create table
#result=cur.execute("CREATE TABLE inventory (id INT PRIMARY KEY, name TEXT, type TEXT, have INT) ")
#con.commit()
#con.close()


# # Insert
#result=cur.execute("insert into inventory (id, name, type, have) values(14, 'warhammer', 'weapon', 0)")
#con.commit()
#con.close()


# # Update Value
result=cur.execute("update hero set exp = 295")
con.commit()
con.close()