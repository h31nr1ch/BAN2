#CRUD python
#uhulll
#!/usr/bin/env python
 
import MySQLdb
 
# Instantiate connection object and connect to MySQL database
db = MySQLdb.connect(&quot;localhost&quot;, &quot;username&quot;, &quot;password&quot;, &quot;irent&quot;)
 
# Instantiate cursor object
cursor = db.cursor()
 
# Prepare a dml statement
sql = &quot;insert into property (address_line_1, user_id, type_id) \
        values ('%s', '%d', '%d')&quot; % ('234 Sathorn Rd', 1, 1)
 
try:
    # Execute dml and commit changes
    cursor.execute(sql)
    db.commit()
     
except:
    # Rollback changes
    db.rollback()
 
# Close database connection
db.close()

# Prepare a dml statement
sql = &quot;delete from property where id &gt; '%d'&quot; % (10)

# Prepare a dml statement
sql = &quot;update property set address_line_2 = '%s' \
        where id = '%d'&quot; % ('Apt B', 1)
 
