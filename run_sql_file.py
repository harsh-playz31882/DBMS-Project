import sqlite3

# Connect to the database
conn = sqlite3.connect('skillhub_crud.db')
cursor = conn.cursor()

# Read and execute the SQL file directly
with open('sql_operations.sql', 'r') as file:
    sql_content = file.read()

# Execute all SQL statements
cursor.executescript(sql_content)

# For SELECT queries, fetch and display results
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = cursor.fetchall()

print("Available tables after running SQL operations:")
for table in tables:
    print(f"- {table[0]}")

# Show some sample data
print("\nSample data from key tables:")
for table_name in ['STUDENT', 'CLIENT', 'SKILL', 'TASK']:
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"{table_name}: {count} records")
    except:
        print(f"{table_name}: Table not found")

conn.commit()
conn.close()
print("\nSQL operations completed successfully!")
