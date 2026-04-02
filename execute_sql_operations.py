import sqlite3
import sys

# Connect to the database
conn = sqlite3.connect('skillhub_crud.db')
cursor = conn.cursor()

print("=" * 80)
print("SQL OPERATIONS - PROJECT REPORT OUTPUTS")
print("=" * 80)

# Read and execute SQL operations from file
with open('sql_operations.sql', 'r') as file:
    sql_content = file.read()

# Split by semicolons and execute each query
queries = sql_content.split(';')
query_num = 1

for query in queries:
    query = query.strip()
    if query and not query.startswith('--'):
        try:
            print(f"\n{'='*60}")
            print(f"QUERY {query_num}:")
            print(f"{'='*60}")
            print(f"SQL:\n{query}\n")
            
            cursor.execute(query)
            
            # Check if it's a SELECT query
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                print("OUTPUT:")
                if results:
                    # Get column names for better formatting
                    if cursor.description:
                        columns = [desc[0] for desc in cursor.description]
                        print(f"Columns: {', '.join(columns)}")
                    for row in results:
                        print(f"  {row}")
                else:
                    print("  No results returned")
            else:
                # For INSERT, UPDATE, DELETE operations
                print(f"OUTPUT: Operation completed successfully")
                conn.commit()
            
            query_num += 1
            
        except Exception as e:
            print(f"ERROR: {e}")
            print("This query could not be executed due to missing tables or invalid syntax")

print(f"\n{'='*80}")
print("END OF SQL OPERATIONS")
print(f"{'='*80}")

conn.close()
