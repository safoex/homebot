import sqlite3

"""
items    : id | userid | name | qty | price | checkid | part | categories 

users    : userid | name  

payments : checkid | finished | needtofinish | total | time | place | shop | filename | shared | userid

"""



#conn = sqlite3.connect('Chinook_Sqlite.sqlite')
conn2 = sqlite3.connect('homebot.db')
c = conn2.cursor()
#c.execute('''CREATE TABLE items
#		(id bigint, userid bigint, name text, qty real, qtycountable real, price real, checkid bigint, part real, categories text, PRIMARY KEY(id))''')
#c.execute('''CREATE TABLE users 
#		(userid bigint, name text, PRIMARY KEY(userid))''')
#c.execute('''CREATE TABLE payments 
#		(checkid bigint, finished bit, needtofinish bit, total real, time datetime, place text, PRIMARY KEY(checkid))''')
#c.execute('''ALTER TABLE payments ADD shop text''')
#c.execute('''ALTER TABLE payments DROP COLUMN shop;''')
#c.execute('''ALTER TABLE payments ADD filename varchar;''')
#c.execute('''INSERT INTO payments (checkid, total, place) VALUES (0, 0, 'LENTA')''')
#c.execute('''DELETE FROM payments WHERE checkid=0''')
#c.execute('''ALTER TABLE payments ADD shared bit''')
#c.execute('''ALTER TABLE payments ADD userid bigint''')

print(c.execute('SELECT name FROM users WHERE userid=?',[1]).fetchall())
conn2.commit()
 
#cursor = conn.cursor()

#cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

#print(cursor.fetchall())

#conn.close()
conn2.close()
