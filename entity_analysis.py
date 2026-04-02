import sqlite3
import re

# Connect to the database
conn = sqlite3.connect('skillhub_crud.db')
cursor = conn.cursor()

print("=" * 80)
print("COMPREHENSIVE ENTITY SCHEMA ANALYSIS")
print("=" * 80)

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
all_tables = [row[0] for row in cursor.fetchall()]

print("\n📊 ALL DATABASE TABLES:")
for table in sorted(all_tables):
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"  {table}: {count} records")

# Focus on main CRUD tables
crud_tables = ['STUDENT', 'CLIENT', 'SKILL', 'TASK']
print(f"\n🎯 MAIN CRUD TABLES ANALYSIS:")

for table in crud_tables:
    if table in all_tables:
        print(f"\n{'='*50}")
        print(f"TABLE: {table}")
        print(f"{'='*50}")
        
        # Get schema
        cursor.execute(f"PRAGMA table_info({table})")
        columns = cursor.fetchall()
        
        print("DATABASE COLUMNS:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        # Get sample data
        cursor.execute(f"SELECT * FROM {table} LIMIT 1")
        sample = cursor.fetchone()
        if sample:
            print("SAMPLE DATA:")
            print(f"  {sample}")

print(f"\n{'='*80}")
print("FRONTEND-BACKEND ENTITY MAPPING ANALYSIS")
print(f"{'='*80}")

# Analyze frontend-backend mapping
frontend_entities = ['students', 'clients', 'skills', 'tasks']
backend_entities = ['STUDENT', 'CLIENT', 'SKILL', 'TASK']

print("\nENTITY MAPPING:")
for i, frontend in enumerate(frontend_entities):
    backend = backend_entities[i]
    table_exists = backend in all_tables
    print(f"  Frontend: '{frontend}' → Backend: '{backend}' → Table Exists: {table_exists}")

print(f"\n{'='*80}")
print("RECOMMENDED STANDARDIZATION")
print(f"{'='*80}")

print("\n🎯 RECOMMENDED APPROACH:")
print("1. Frontend: Use lowercase (students, clients, skills, tasks)")
print("2. Backend: Map lowercase to uppercase tables")
print("3. Database: Keep uppercase tables (STUDENT, CLIENT, SKILL, TASK)")
print("4. Consistent mapping in all CRUD operations")

conn.close()
