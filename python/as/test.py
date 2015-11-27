import psycopg2

# Connect to an existing database
conn = psycopg2.connect(database="test", user="vinyl", password="tibia1")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
