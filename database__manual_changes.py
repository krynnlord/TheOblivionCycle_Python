import os, sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

# # Create table
#result=cur.execute("CREATE TABLE equipment (id INT PRIMARY KEY, armor TEXT, weapon TEXT) ")
#con.commit()
#con.close()


# # Insert
#result=cur.execute("insert into equipment (id, armor, weapon) values(1,'tunic', 'hands')")
#con.commit()
#con.close()


# # Update Value
result=cur.execute("update equipment set armor = 1 where id = 1")
con.commit()
con.close()