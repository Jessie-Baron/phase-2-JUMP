import mysql.connector

db = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'sakila'
)

cursor = db.cursor()

# query 1

query = "SELECT customer_id, count(inventory_id) FROM rental GROUP BY customer_id ORDER BY count(inventory_id) DESC LIMIT 5"

cursor.execute(query)
results = cursor.fetchall()
print(results)

# query 2
