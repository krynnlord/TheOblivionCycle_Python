import os, sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

# # Create table
# result=cur.execute("CREATE TABLE options (id INT PRIMARY KEY, option TEXT, value INT) ")
# con.commit()
# con.close()


# # Insert
# result=cur.execute("insert into options (id, option, value) values(2,'skip_intro', 1)")
# con.commit()
# con.close()


# # Update Value
result=cur.execute("update options set value = 1 where id = 3")
con.commit()
con.close()