import sqlite3

# Connect to the database
conn = sqlite3.connect('skillhub_crud.db')
cursor = conn.cursor()

print("=" * 80)
print("STANDARDIZING ENTITY MAPPINGS")
print("=" * 80)

# Define the standardization mapping
entity_mapping = {
    'students': 'STUDENT',
    'clients': 'CLIENT', 
    'skills': 'SKILL',
    'tasks': 'TASK'
}

print("\n🎯 ENTITY MAPPING STANDARDIZATION:")
for frontend, backend in entity_mapping.items():
    print(f"  Frontend: '{frontend}' → Backend Table: '{backend}'")

# Check if we need to clean up duplicate tables
print(f"\n📊 CURRENT TABLE STATUS:")

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
all_tables = [row[0] for row in cursor.fetchall()]

main_tables = ['STUDENT', 'CLIENT', 'SKILL', 'TASK']
duplicate_tables = ['students', 'clients', 'skills', 'tasks']

print("MAIN TABLES (Keep):")
for table in main_tables:
    if table in all_tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table}: {count} records")

print("\nDUPLICATE TABLES (Consider removing):")
for table in duplicate_tables:
    if table in all_tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table}: {count} records")

print(f"\n✅ RECOMMENDED BACKEND ENTITY HANDLING:")
print("1. Frontend sends: 'students', 'clients', 'skills', 'tasks'")
print("2. Backend maps to: 'STUDENT', 'CLIENT', 'SKILL', 'TASK'")
print("3. Use entity.upper() for consistent mapping")
print("4. Remove duplicate lowercase tables to avoid confusion")

conn.close()
