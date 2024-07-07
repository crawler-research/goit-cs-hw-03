from faker import Faker
import psycopg2

fake = Faker()

conn = psycopg2.connect(
    dbname="MaksymDB",
    user="max",
    password="deleted",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

for i in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

    status = fake.random_element(elements=('new', 'in progress', 'completed'))

    cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))

    title = fake.sentence()
    description = fake.text()
    status_id = fake.random_int(min=1, max=100)
    user_id = fake.random_int(min=1, max=100)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))

conn.commit()
cur.close()
conn.close()