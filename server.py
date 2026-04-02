#!/usr/bin/env python3
"""
Simple Python CRUD Interface - Flask Backend
No external dependencies required - uses built-in sqlite3
"""

import sqlite3
import json
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import socket

# Database Setup
def init_database():
    conn = sqlite3.connect('skillhub_crud.db')
    cursor = conn.cursor()
    
    # Create tables matching your database_schema.sql
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS STUDENT (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            salt VARCHAR(32) NOT NULL,
            phone VARCHAR(20),
            university VARCHAR(100) NOT NULL,
            major VARCHAR(50) NOT NULL,
            graduation_year INTEGER NOT NULL CHECK(graduation_year >= 2020 AND graduation_year <= 2030),
            registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
            profile_status VARCHAR(20) DEFAULT 'active' CHECK(profile_status IN ('active', 'inactive', 'suspended')),
            last_login TIMESTAMP,
            login_attempts INTEGER DEFAULT 0,
            account_locked BOOLEAN DEFAULT FALSE,
            email_verified BOOLEAN DEFAULT FALSE
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CLIENT (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name VARCHAR(100) NOT NULL,
            contact_person VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            salt VARCHAR(32) NOT NULL,
            phone VARCHAR(20),
            business_type VARCHAR(50) NOT NULL,
            registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
            verification_status VARCHAR(20) DEFAULT 'pending' CHECK(verification_status IN ('pending', 'verified', 'rejected')),
            last_login TIMESTAMP,
            login_attempts INTEGER DEFAULT 0,
            account_locked BOOLEAN DEFAULT FALSE,
            email_verified BOOLEAN DEFAULT FALSE
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SKILL (
            skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name VARCHAR(50) UNIQUE NOT NULL,
            category VARCHAR(50) NOT NULL,
            students INTEGER DEFAULT 0,
            demand VARCHAR(20) DEFAULT 'Medium' CHECK(demand IN ('High', 'Medium', 'Low'))
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TASK (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200) NOT NULL,
            description TEXT NOT NULL,
            budget DECIMAL(10,2) NOT NULL,
            skill_required VARCHAR(50) NOT NULL,
            difficulty VARCHAR(20) NOT NULL CHECK(difficulty IN ('Beginner', 'Intermediate', 'Advanced')),
            deadline DATE NOT NULL,
            estimated_hours INTEGER NOT NULL,
            client_id INTEGER NOT NULL,
            posting_date DATE NOT NULL DEFAULT CURRENT_DATE,
            status VARCHAR(20) DEFAULT 'open' CHECK(status IN ('open', 'in_progress', 'completed', 'cancelled')),
            FOREIGN KEY (client_id) REFERENCES CLIENT(client_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TASK_APPLICATION (
            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            application_date DATE NOT NULL DEFAULT CURRENT_DATE,
            status VARCHAR(20) DEFAULT 'pending' CHECK(status IN ('pending', 'accepted', 'rejected')),
            cover_letter TEXT,
            FOREIGN KEY (task_id) REFERENCES TASK(task_id),
            FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TASK_ASSIGNMENT (
            assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
            completion_date DATE,
            status VARCHAR(20) DEFAULT 'in_progress' CHECK(status IN ('in_progress', 'completed', 'cancelled')),
            FOREIGN KEY (task_id) REFERENCES TASK(task_id),
            FOREIGN KEY (student_id) REFERENCES STUDENT(student_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PAYMENT (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            assignment_id INTEGER NOT NULL,
            amount DECIMAL(10,2) NOT NULL,
            payment_method VARCHAR(50) NOT NULL CHECK(payment_method IN ('credit_card', 'paypal', 'stripe', 'bank_transfer')),
            payment_date DATE NOT NULL DEFAULT CURRENT_DATE,
            status VARCHAR(20) DEFAULT 'pending' CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
            transaction_id VARCHAR(100),
            FOREIGN KEY (assignment_id) REFERENCES TASK_ASSIGNMENT(assignment_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RATING (
            rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
            assignment_id INTEGER NOT NULL,
            client_rating INTEGER CHECK(client_rating BETWEEN 1 AND 5),
            student_rating INTEGER CHECK(student_rating BETWEEN 1 AND 5),
            review TEXT,
            rating_date DATE NOT NULL DEFAULT CURRENT_DATE,
            FOREIGN KEY (assignment_id) REFERENCES TASK_ASSIGNMENT(assignment_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DISPUTE (
            dispute_id INTEGER PRIMARY KEY AUTOINCREMENT,
            assignment_id INTEGER NOT NULL,
            raised_by VARCHAR(20) NOT NULL CHECK(raised_by IN ('student', 'client')),
            reason TEXT NOT NULL,
            status VARCHAR(20) DEFAULT 'open' CHECK(status IN ('open', 'under_review', 'resolved', 'dismissed')),
            created_date DATE NOT NULL DEFAULT CURRENT_DATE,
            resolved_date DATE,
            resolution TEXT,
            FOREIGN KEY (assignment_id) REFERENCES TASK_ASSIGNMENT(assignment_id)
        )
    ''')
    
    # Insert sample data if empty
    cursor.execute("SELECT COUNT(*) FROM STUDENT")
    if cursor.fetchone()[0] == 0:
        insert_sample_data(cursor)
    
    conn.commit()
    conn.close()

def insert_sample_data(cursor):
    # Sample students with authentication fields
    import secrets
    import hashlib
    
    def hash_password(password, salt):
        return hashlib.sha256((password + salt).encode()).hexdigest()
    
    students = [
        ('John', 'Doe', 'john@example.com', '555-0101', 'Stanford University', 'Computer Science', 2025, 'johndoe123', 'active'),
        ('Jane', 'Smith', 'jane@example.com', '555-0102', 'MIT', 'Data Science', 2024, 'janesmith123', 'active'),
        ('Mike', 'Johnson', 'mike@example.com', '555-0103', 'Harvard', 'Business', 2026, 'mikejohnson123', 'active')
    ]
    
    for student in students:
        salt = secrets.token_hex(16)
        hashed_password = hash_password(student[7], salt)
        cursor.execute('''
            INSERT INTO STUDENT (first_name, last_name, email, phone, university, major, graduation_year, password_hash, salt, profile_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (student[0], student[1], student[2], student[3], student[4], student[5], student[6], hashed_password, salt, 'active'))
    
    # Sample clients with authentication fields
    clients = [
        ('TechStart Inc.', 'Alice Johnson', 'alice@techstart.com', '555-0201', 'Technology', 'alice123', 'pending'),
        ('Creative Agency', 'Bob Wilson', 'bob@creative.com', '555-0202', 'Design', 'bob123', 'pending')
    ]
    
    for client in clients:
        salt = secrets.token_hex(16)
        hashed_password = hash_password(client[5], salt)
        cursor.execute('''
            INSERT INTO CLIENT (company_name, contact_person, email, phone, business_type, password_hash, salt, verification_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (client[0], client[1], client[2], client[3], client[4], hashed_password, salt, client[6]))
    
    # Sample skills
    skills = [
        ('JavaScript', 'Programming', 'High', 15),
        ('Python', 'Programming', 'High', 12),
        ('C++', 'Programming', 'Medium', 8),
        ('Unreal Engine', 'Game Development', 'High', 6),
        ('Graphic Design', 'Design', 'Medium', 8),
        ('Content Writing', 'Writing', 'High', 10),
        ('Data Entry', 'Administrative', 'Low', 6),
        ('Social Media Marketing', 'Marketing', 'Medium', 7),
        ('Video Editing', 'Media', 'Medium', 5),
        ('Translation', 'Language', 'Low', 4),
        ('Excel', 'Office', 'Medium', 9),
        ('Photography', 'Media', 'Low', 3)
    ]
    
    cursor.executemany('''
        INSERT INTO SKILL (skill_name, category, demand, students)
        VALUES (?, ?, ?, ?)
    ''', skills)
    
    # Sample tasks
    tasks = [
        ('JavaScript Web App Development', 'Build a responsive web application using JavaScript and modern frameworks', 300.00, 'JavaScript', 'Intermediate', '2024-04-15', 20, 1, 'open'),
        ('Logo Design for Startup', 'Create a modern logo design for a new tech startup', 150.00, 'Graphic Design', 'Beginner', '2024-03-20', 8, 2, 'completed'),
        ('Python Data Analysis', 'Analyze dataset using Python and create visualizations', 250.00, 'Python', 'Advanced', '2024-04-10', 15, 3, 'in_progress'),
        ('Content Writing Campaign', 'Write 10 blog posts for digital marketing campaign', 180.00, 'Content Writing', 'Beginner', '2024-03-25', 12, 4, 'open'),
        ('Data Entry Project', 'Enter 500 product entries into database system', 100.00, 'Data Entry', 'Beginner', '2024-03-18', 10, 5, 'open'),
        ('Social Media Management', 'Manage Instagram and Twitter accounts for 1 month', 350.00, 'Social Media Marketing', 'Intermediate', '2024-04-20', 25, 6, 'open'),
        ('Video Editing Project', 'Edit 5 promotional videos for YouTube', 280.00, 'Video Editing', 'Advanced', '2024-04-12', 18, 7, 'in_progress'),
        ('Document Translation', 'Translate technical documents from English to Spanish', 200.00, 'Translation', 'Advanced', '2024-03-22', 14, 8, 'completed'),
        ('C++ Game Engine Development', 'Develop a basic 2D game engine using C++ with physics and rendering', 450.00, 'C++', 'Advanced', '2024-05-01', 30, 1, 'open'),
        ('Unreal Engine VR Experience', 'Create an immersive VR experience using Unreal Engine for training simulation', 600.00, 'Unreal Engine', 'Advanced', '2024-05-15', 40, 1, 'open')
    ]
    
    cursor.executemany('''
        INSERT INTO TASK (title, description, budget, skill_required, difficulty, deadline, estimated_hours, client_id, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tasks)

class CRUDHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        init_database()
    
    def do_GET(self):
        print("[DEBUG] do_GET method called!")
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        # Debug logging
        print(f"[DEBUG] GET request received: {self.path}")
        print(f"[DEBUG] Query params: {query_params}")
        
        # If it's the root path with no query parameters, serve the HTML file
        if (parsed_path.path == '/' or parsed_path.path == '') and not query_params:
            print("[DEBUG] Serving crud_interface.html for root path")
            self.serve_file('crud_interface.html')
            return
        
        # Serve test file if requested
        if parsed_path.path == '/test_skill.html':
            print("[DEBUG] Serving test_skill.html")
            self.serve_file('test_skill.html')
            return
        
        entity = query_params.get('entity', ['STUDENT'])[0]
        action = query_params.get('action', ['read'])[0]
        
        print(f"[DEBUG] Entity: {entity}, Action: {action}")
        
        if action == 'read':
            try:
                result = self.read_records(entity)
                print(f"[DEBUG] Read result: {result}")
                self.send_json_response(result)
            except Exception as e:
                print(f"[DEBUG] Error in read_records: {e}")
                self.send_json_response({'success': False, 'message': 'Error: ' + str(e)})
        else:
            self.serve_file('crud_interface.html')
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        query_params = parse_qs(post_data)
        
        # Add CORS headers
        self.send_response(200, 'text/plain', b'')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        entity = query_params.get('entity', ['STUDENT'])[0]
        action = query_params.get('action', ['read'])[0]
        
        if action == 'create':
            response = self.create_record(entity, query_params)
        elif action == 'update':
            response = self.update_record(entity, query_params)
        elif action == 'delete':
            response = self.delete_record(entity, query_params)
        else:
            response = {'success': False, 'message': 'Invalid action'}
        
        self.send_json_response(response)
    
    def read_records(self, entity):
        try:
            conn = sqlite3.connect('skillhub_crud.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if entity == 'TASK':
                cursor.execute('''
                    SELECT t.*, c.company_name as client_name 
                    FROM TASK t 
                    LEFT JOIN CLIENT c ON t.client_id = c.client_id 
                    ORDER BY t.posting_date DESC
                ''')
            elif entity == 'TASK_APPLICATION':
                cursor.execute('''
                    SELECT ta.*, s.first_name || ' ' || s.last_name as student_name, t.title as task_title
                    FROM TASK_APPLICATION ta
                    JOIN STUDENT s ON ta.student_id = s.student_id
                    JOIN TASK t ON ta.task_id = t.task_id
                    ORDER BY ta.application_date DESC
                ''')
            elif entity == 'TASK_ASSIGNMENT':
                cursor.execute('''
                    SELECT ta.*, s.first_name || ' ' || s.last_name as student_name, t.title as task_title
                    FROM TASK_ASSIGNMENT ta
                    JOIN STUDENT s ON ta.student_id = s.student_id
                    JOIN TASK t ON ta.task_id = t.task_id
                    ORDER BY ta.assigned_date DESC
                ''')
            elif entity == 'PAYMENT':
                cursor.execute('''
                    SELECT p.*, t.title as task_title
                    FROM PAYMENT p
                    JOIN TASK_ASSIGNMENT ta ON p.assignment_id = ta.assignment_id
                    JOIN TASK t ON ta.task_id = t.task_id
                    ORDER BY p.payment_date DESC
                ''')
            elif entity == 'RATING':
                cursor.execute('''
                    SELECT r.*, t.title as task_title
                    FROM RATING r
                    JOIN TASK_ASSIGNMENT ta ON r.assignment_id = ta.assignment_id
                    JOIN TASK t ON ta.task_id = t.task_id
                    ORDER BY r.rating_date DESC
                ''')
            elif entity == 'DISPUTE':
                cursor.execute('''
                    SELECT d.*, t.title as task_title
                    FROM DISPUTE d
                    JOIN TASK_ASSIGNMENT ta ON d.assignment_id = ta.assignment_id
                    JOIN TASK t ON ta.task_id = t.task_id
                    ORDER BY d.created_date DESC
                ''')
            else:
                # Handle specific entity column names (plural form)
                if entity == 'clients':
                    cursor.execute("SELECT * FROM CLIENT ORDER BY client_id ASC")
                elif entity == 'students':
                    cursor.execute("SELECT * FROM STUDENT ORDER BY student_id ASC")
                elif entity == 'skills':
                    cursor.execute("SELECT * FROM SKILL ORDER BY skill_id ASC")
                elif entity == 'tasks':
                    cursor.execute("SELECT * FROM TASK ORDER BY task_id ASC")
                else:
                    cursor.execute("SELECT * FROM " + entity + " ORDER BY " + entity.lower() + "_id ASC")
            
            records = [dict(row) for row in cursor.fetchall()]
            conn.close()
            
            return {'success': True, 'data': records}
        except Exception as e:
            return {'success': False, 'message': 'Error: ' + str(e)}
    
    def create_record(self, entity, data):
        try:
            print(f"[DEBUG] Creating record for entity: {entity}")
            print(f"[DEBUG] Data received: {data}")
            
            conn = sqlite3.connect('skillhub_crud.db')
            cursor = conn.cursor()
            
            if entity.upper() == 'STUDENT':
                import secrets
                import hashlib
                
                salt = secrets.token_hex(16)
                password_hash = hashlib.sha256((data.get('password', [''])[0] + salt).encode()).hexdigest()
                
                cursor.execute('''
                    INSERT INTO STUDENT (first_name, last_name, email, phone, university, major, graduation_year, password_hash, salt, profile_status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('first_name', [''])[0],
                    data.get('last_name', [''])[0],
                    data.get('email', [''])[0],
                    data.get('phone', [''])[0],
                    data.get('university', [''])[0],
                    data.get('major', [''])[0],
                    int(data.get('graduation_year', ['2024'])[0]),
                    password_hash,
                    salt,
                    data.get('profile_status', ['active'])
                ))
            elif entity.upper() == 'CLIENT':
                import secrets
                import hashlib
                
                salt = secrets.token_hex(16)
                password_hash = hashlib.sha256((data.get('password', [''])[0] + salt).encode()).hexdigest()
                
                cursor.execute('''
                    INSERT INTO CLIENT (company_name, contact_person, email, phone, business_type, password_hash, salt, verification_status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('company_name', [''])[0],
                    data.get('contact_person', [''])[0],
                    data.get('email', [''])[0],
                    data.get('phone', [''])[0],
                    data.get('business_type', [''])[0],
                    password_hash,
                    salt,
                    data.get('verification_status', ['active'])
                ))
            elif entity.upper() == 'SKILL':
                print(f"[DEBUG] Creating skill with data: skill_name={data.get('skill-name', [''])[0]}, category={data.get('skill-category', [''])[0]}, description={data.get('description', [''])[0]}")
                try:
                    cursor.execute('''
                        INSERT INTO SKILL (skill_name, category, description)
                        VALUES (?, ?, ?)
                    ''', (
                        data.get('skill-name', [''])[0],
                        data.get('skill-category', [''])[0],
                        data.get('description', [''])
                    ))
                    print("[DEBUG] Skill SQL executed successfully")
                except Exception as e:
                    print(f"[DEBUG] ERROR inserting skill: {e}")
                    raise e
            elif entity.upper() == 'TASK':
                cursor.execute('''
                    INSERT INTO TASK (title, description, budget, skill_required, difficulty, deadline, estimated_hours, client_id, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('title', [''])[0],
                    data.get('description', [''])[0],
                    float(data.get('budget', ['0'])[0]),
                    data.get('skill_required', [''])[0],
                    data.get('difficulty', [''])[0],
                    data.get('deadline', [''])[0],
                    int(data.get('estimated_hours', ['1'])[0]),
                    int(data.get('client_id', ['1'])[0]),
                    data.get('status', ['open'])
                ))
            elif entity.upper() == 'TASK_APPLICATION':
                cursor.execute('''
                    INSERT INTO TASK_APPLICATION (task_id, student_id, cover_letter, status)
                    VALUES (?, ?, ?, ?)
                ''', (
                    int(data.get('task_id', ['1'])[0]),
                    int(data.get('student_id', ['1'])[0]),
                    data.get('cover_letter', [''])[0],
                    data.get('status', ['pending'])
                ))
            elif entity.upper() == 'TASK_ASSIGNMENT':
                cursor.execute('''
                    INSERT INTO TASK_ASSIGNMENT (task_id, student_id, status)
                    VALUES (?, ?, ?)
                ''', (
                    int(data.get('task_id', ['1'])[0]),
                    int(data.get('student_id', ['1'])[0]),
                    data.get('status', ['in_progress'])
                ))
            elif entity.upper() == 'PAYMENT':
                cursor.execute('''
                    INSERT INTO PAYMENT (assignment_id, amount, payment_method, transaction_id, status)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    int(data.get('assignment_id', ['1'])[0]),
                    float(data.get('amount', ['0'])[0]),
                    data.get('payment_method', ['credit_card'])[0],
                    data.get('transaction_id', [''])[0],
                    data.get('status', ['completed'])
                ))
            elif entity.upper() == 'RATING':
                cursor.execute('''
                    INSERT INTO RATING (assignment_id, client_rating, student_rating, review)
                    VALUES (?, ?, ?, ?)
                ''', (
                    int(data.get('assignment_id', ['1'])[0]),
                    int(data.get('client_rating', ['5'])[0]),
                    int(data.get('student_rating', ['5'])[0]),
                    data.get('review', [''])[0])
                )
            elif entity.upper() == 'DISPUTE':
                cursor.execute('''
                    INSERT INTO DISPUTE (assignment_id, raised_by, reason, status)
                    VALUES (?, ?, ?, ?)
                ''', (
                    int(data.get('assignment_id', ['1'])[0]),
                    data.get('raised_by', ['student'])[0],
                    data.get('reason', [''])[0],
                    data.get('status', ['open'])
                ))
            
            conn.commit()
            conn.close()
            
            return {'success': True, 'message': entity + ' created successfully'}
        except Exception as e:
            return {'success': False, 'message': 'Error: ' + str(e)}
    
    def update_record(self, entity, data):
        try:
            conn = sqlite3.connect('skillhub_crud.db')
            cursor = conn.cursor()
            
            record_id = int(data.get('id', ['0'])[0])
            
            if entity.upper() == 'STUDENT':
                cursor.execute('''
                    UPDATE STUDENT 
                    SET first_name = ?, last_name = ?, email = ?, phone = ?, university = ?, major = ?, graduation_year = ?, profile_status = ?
                    WHERE student_id = ?
                ''', (
                    data.get('first_name', [''])[0],
                    data.get('last_name', [''])[0],
                    data.get('email', [''])[0],
                    data.get('phone', [''])[0],
                    data.get('university', [''])[0],
                    data.get('major', [''])[0],
                    int(data.get('graduation_year', ['2025'])[0]),
                    data.get('profile_status', ['active']),
                    record_id
                ))
            elif entity.upper() == 'CLIENT':
                cursor.execute('''
                    UPDATE CLIENT 
                    SET company_name = ?, contact_person = ?, email = ?, phone = ?, business_type = ?, verification_status = ?
                    WHERE client_id = ?
                ''', (
                    data.get('company_name', [''])[0],
                    data.get('contact_person', [''])[0],
                    data.get('email', [''])[0],
                    data.get('phone', [''])[0],
                    data.get('business_type', [''])[0],
                    data.get('verification_status', ['active']),
                    record_id
                ))
            elif entity.upper() == 'SKILL':
                cursor.execute('''
                    UPDATE SKILL 
                    SET skill_name = ?, category = ?, description = ?
                    WHERE skill_id = ?
                ''', (
                    data.get('skill_name', [''])[0],
                    data.get('category', [''])[0],
                    data.get('description', ['']),
                    record_id
                ))
            elif entity.upper() == 'TASK':
                cursor.execute('''
                    UPDATE TASK 
                    SET title = ?, description = ?, budget = ?, skill_required = ?, difficulty = ?, deadline = ?, estimated_hours = ?, client_id = ?, status = ?
                    WHERE task_id = ?
                ''', (
                    data.get('title', [''])[0],
                    data.get('description', [''])[0],
                    float(data.get('budget', ['0'])[0]),
                    data.get('skill_required', [''])[0],
                    data.get('difficulty', [''])[0],
                    data.get('deadline', [''])[0],
                    int(data.get('estimated_hours', ['1'])[0]),
                    int(data.get('client_id', ['1'])[0]),
                    data.get('status', ['open'])
                ))
            elif entity == 'TASK_APPLICATION':
                cursor.execute('''
                    UPDATE TASK_APPLICATION 
                    SET task_id = ?, student_id = ?, cover_letter = ?, status = ?
                    WHERE application_id = ?
                ''', (
                    int(data.get('task_id', ['1'])[0]),
                    int(data.get('student_id', ['1'])[0]),
                    data.get('cover_letter', [''])[0],
                    data.get('status', ['pending'])
                ))
            elif entity == 'TASK_ASSIGNMENT':
                cursor.execute('''
                    UPDATE TASK_ASSIGNMENT 
                    SET task_id = ?, student_id = ?, status = ?, completion_date = ?
                    WHERE assignment_id = ?
                ''', (
                    int(data.get('task_id', ['1'])[0]),
                    int(data.get('student_id', ['1'])[0]),
                    data.get('status', ['in_progress']),
                    data.get('completion_date', [''])[0]
                ))
            elif entity == 'PAYMENT':
                cursor.execute('''
                    UPDATE PAYMENT 
                    SET assignment_id = ?, amount = ?, payment_method = ?, transaction_id = ?, status = ?
                    WHERE payment_id = ?
                ''', (
                    int(data.get('assignment_id', ['1'])[0]),
                    float(data.get('amount', ['0'])[0]),
                    data.get('payment_method', ['credit_card'])[0],
                    data.get('transaction_id', [''])[0],
                    data.get('status', ['completed'])
                ))
            elif entity == 'RATING':
                cursor.execute('''
                    UPDATE RATING 
                    SET assignment_id = ?, client_rating = ?, student_rating = ?, review = ?
                    WHERE rating_id = ?
                ''', (
                    int(data.get('assignment_id', ['1'])[0]),
                    int(data.get('client_rating', ['5'])[0]),
                    int(data.get('student_rating', ['5'])[0]),
                    data.get('review', [''])[0]
                ))
            elif entity == 'DISPUTE':
                cursor.execute('''
                    UPDATE DISPUTE 
                    SET assignment_id = ?, raised_by = ?, reason = ?, status = ?, resolved_date = ?, resolution = ?
                    WHERE dispute_id = ?
                ''', (
                    int(data.get('assignment_id', ['1'])[0]),
                    data.get('raised_by', ['student'])[0],
                    data.get('reason', [''])[0],
                    data.get('status', ['under_review']),
                    data.get('resolved_date', [''])[0],
                    data.get('resolution', [''])[0]
                ))
            
            conn.commit()
            conn.close()
            
            return {'success': True, 'message': entity + ' updated successfully'}
        except Exception as e:
            return {'success': False, 'message': 'Error: ' + str(e)}
    
    def delete_record(self, entity, data):
        try:
            conn = sqlite3.connect('skillhub_crud.db')
            cursor = conn.cursor()
            
            record_id = int(data.get('id', ['0'])[0])
            
            if entity.upper() == 'TASK_APPLICATION':
                cursor.execute(f"DELETE FROM TASK_APPLICATION WHERE application_id = ?", (record_id,))
            elif entity.upper() == 'TASK_ASSIGNMENT':
                cursor.execute(f"DELETE FROM TASK_ASSIGNMENT WHERE assignment_id = ?", (record_id,))
            elif entity.upper() == 'PAYMENT':
                cursor.execute(f"DELETE FROM PAYMENT WHERE payment_id = ?", (record_id,))
            elif entity.upper() == 'RATING':
                cursor.execute(f"DELETE FROM RATING WHERE rating_id = ?", (record_id,))
            elif entity.upper() == 'DISPUTE':
                cursor.execute(f"DELETE FROM DISPUTE WHERE dispute_id = ?", (record_id,))
            else:
                # Handle specific entity column names for delete (plural form)
                if entity == 'clients':
                    cursor.execute("DELETE FROM CLIENT WHERE client_id = ?", (record_id,))
                elif entity == 'students':
                    cursor.execute("DELETE FROM STUDENT WHERE student_id = ?", (record_id,))
                elif entity == 'skills':
                    cursor.execute("DELETE FROM SKILL WHERE skill_id = ?", (record_id,))
                elif entity == 'tasks':
                    cursor.execute("DELETE FROM TASK WHERE task_id = ?", (record_id,))
                else:
                    cursor.execute("DELETE FROM " + entity + " WHERE " + entity.lower() + "_id = ?", (record_id,))
            
            conn.commit()
            conn.close()
            
            return {'success': True, 'message': entity + ' deleted successfully'}
        except Exception as e:
            return {'success': False, 'message': 'Error: ' + str(e)}
    
    def send_response_data(self, status, content_type, content):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))
    
    def send_json_response(self, data):
        self.send_response_data(200, 'application/json', json.dumps(data))
    
    def serve_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            self.send_response_data(200, 'text/html', content)
        except FileNotFoundError:
            self.send_response_data(404, 'text/plain', 'File not found')
    
    def do_POST(self):
        print("[DEBUG] do_POST method called!")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        query_params = parse_qs(post_data)
        
        print(f"[DEBUG] POST data received: {post_data}")
        print(f"[DEBUG] Parsed POST params: {query_params}")
        
        entity = query_params.get('entity', ['STUDENT'])[0]
        action = query_params.get('action', ['read'])[0]
        
        print(f"[DEBUG] POST Entity: {entity}, Action: {action}")
        
        if action == 'create':
            response = self.create_record(entity, query_params)
        elif action == 'update':
            response = self.update_record(entity, query_params)
        elif action == 'delete':
            response = self.delete_record(entity, query_params)
        else:
            response = {'success': False, 'message': 'Invalid action'}
        
        print(f"[DEBUG] POST response: {response}")
        self.send_json_response(response)
    
    def send_response_data(self, status, content_type, content):
        # Add CORS headers and CSP for development
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Length', str(len(content.encode('utf-8'))))
        
        # Remove CSP entirely for development to avoid browser conflicts
        # if content_type == 'text/html':
        #     self.send_header('Content-Security-Policy', ...)
        
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))
    
    def send_json_response(self, data):
        self.send_response_data(200, 'application/json', json.dumps(data))

def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == '__main__':
    # Initialize database
    init_database()
    
    # Get local IP
    local_ip = get_local_ip()
    port = 8000
    
    print(f"🚀 Starting Python CRUD Server...")
    print(f"📡 Local IP: {local_ip}")
    print(f"🌐 Server URL: http://{local_ip}:{port}")
    print(f"📱 Access from other devices: http://{local_ip}:{port}")
    print(f"💻 Local access: http://localhost:{port}")
    print(f"⏹️ Press Ctrl+C to stop server")
    
    # Start server
    server = HTTPServer(('0.0.0.0', port), CRUDHandler)
    print(f"✅ Server running on port {port}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        server.server_close()
