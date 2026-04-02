import sqlite3

# Connect to the database
conn = sqlite3.connect('skillhub_crud.db')
cursor = conn.cursor()

# Read the SQL file
with open('sql_operations.sql', 'r') as file:
    sql_content = file.read()

# Extract only SELECT queries (skip INSERT, UPDATE, DELETE that might fail)
lines = sql_content.split('\n')
current_query = ""
in_select = False

print("=" * 80)
print("EXECUTING SELECT QUERIES FROM sql_operations.sql")
print("=" * 80)

query_num = 1
for line in lines:
    line = line.strip()
    
    # Start of a SELECT query
    if line.upper().startswith('SELECT'):
        in_select = True
        current_query = line
    # Continue building the query
    elif in_select and line:
        current_query += " " + line
    # End of query (semicolon or empty line)
    elif in_select and (line.endswith(';') or not line):
        if current_query.endswith(';'):
            current_query = current_query[:-1]  # Remove semicolon
        
        try:
            print(f"\n{'='*60}")
            print(f"SELECT QUERY {query_num}:")
            print(f"{'='*60}")
            print(f"SQL:\n{current_query}\n")
            
            cursor.execute(current_query)
            results = cursor.fetchall()
            
            print("OUTPUT:")
            if results:
                if cursor.description:
                    columns = [desc[0] for desc in cursor.description]
                    print(f"Columns: {', '.join(columns)}")
                for i, row in enumerate(results):
                    if i < 5:  # Limit output for readability
                        print(f"  {row}")
                    elif i == 5:
                        print(f"  ... and {len(results)-5} more rows")
                        break
            else:
                print("  No results returned")
            
            query_num += 1
        except Exception as e:
            print(f"ERROR: {e}")
        
        current_query = ""
        in_select = False

print(f"\n{'='*80}")
print("SELECT QUERIES COMPLETED")
print(f"{'='*80}")

conn.close()
