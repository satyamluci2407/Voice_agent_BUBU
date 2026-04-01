import sqlite3


conn = sqlite3.connect("bubu.db")

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# # to insert values
# query = "INSERT INTO sys_command VALUES (null,'Discord', 'C:\\Users\\Satyam Shandilya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.exe')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done


# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# to insert values
# query = "INSERT INTO web_command VALUES (null,'Canva', 'https://www.canva.com')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done

#Delete
query = "DELETE FROM web_command WHERE name='Hery'"
cursor.execute(query)
conn.commit()
conn.close()

#testing module
# query = "OneNote"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
# results = cursor.fetchall()
# print(results[0][0])