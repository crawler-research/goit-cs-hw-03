
import psycopg2

conn = psycopg2.connect(
    dbname="MaksymDB",
    user="max",
    password="deleted",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# 1.
user_id = 1  # replace with the actual user_id
cur.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
tasks = cur.fetchall()
print(f"Tasks for user {user_id}: {tasks}")

# 2.
cur.execute("SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = %s)", ('new',))
tasks = cur.fetchall()
print(tasks)

# 3.
task_id = 2
new_status = 'in progress'
cur.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = %s) WHERE id = %s", (new_status, task_id))

# 4.
cur.execute("SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)")
users = cur.fetchall()
print(f"Users without tasks: {users}")

# 5.
title = 'asdas' 
description = 'agsdasgasgsdgasd' 
status = 'new'
cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, (SELECT id FROM status WHERE name = %s), %s)", (title, description, status, user_id))

# 6.
cur.execute("SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')")
print(cur.fetchall())

# 7.
cur.execute("DELETE FROM tasks WHERE id = %s", (2,))

# 8
email = 'asdas@gmail.com'
cur.execute("SELECT * FROM users WHERE email LIKE %s", (email,))
print(cur.fetchall())

# 9.
cur.execute("UPDATE users SET fullname = %s WHERE id = %s", ('new asdas name', 2))

# 10.
cur.execute("SELECT s.name, COUNT(t.id) FROM status s LEFT JOIN tasks t ON s.id = t.status_id GROUP BY s.name")
status_counts = cur.fetchall()
print(f"Number of tasks for each status: {status_counts}")

#11
domain = '%@gmail.com'
cur.execute("SELECT t.* FROM tasks t JOIN users u ON t.user_id = u.id WHERE u.email LIKE %s", (domain,))
print(cur.fetchall())

# 12.
cur.execute("SELECT * FROM tasks WHERE description IS NULL OR description = ''")
print(cur.fetchall())

# 13.
cur.execute("SELECT u.*, t.* FROM users u JOIN tasks t ON u.id = t.user_id WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress')")
print(cur.fetchall())

# 14
cur.execute("SELECT u.*, COUNT(t.id) FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.id")
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()