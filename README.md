# Skill-Based Micro-Task Marketplace for Students

A comprehensive DBMS project that demonstrates advanced database design, normalization, full-stack development, and practical problem-solving skills in building a freelance marketplace platform.

## 🎯 Project Overview

This system is a database-driven platform designed to connect university students with clients who require short-term, skill-based micro-tasks. In the modern gig economy, students often seek small projects to gain practical experience and earn income. However, existing freelance platforms are primarily built for professionals and large-scale projects, lacking structured support for student-level micro-tasks.

The platform provides a centralized database to manage student profiles, skills, client details, task postings, applications, task assignments, payments, ratings, and dispute records. It ensures transparency, accountability, and proper tracking of performance metrics.

## 🛠️ Technology Stack

- **Database**: SQLite 3.x (BCNF normalized, 10 tables)
- **Backend**: Python HTTP Server with RESTful API
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Authentication**: Password hashing with salt, session management
- **API**: RESTful endpoints for CRUD operations

## 📁 Project Structure

```
DBMS-Project/
├── database_design.md      # Complete ER diagram and database design
├── database_schema.sql      # SQL table creation with constraints
├── sample_data.sql         # Sample data insertion
├── sql_operations.sql       # Comprehensive SQL operations demo
├── crud_interface.html     # Main CRUD management interface
├── server.py               # Python HTTP server with API endpoints
├── emergency_test.html     # Debugging interface for testing
└── README.md               # This file
```

## 🏗️ Database Design

### Entities and Relationships

The database consists of **10 main entities** fully normalized to BCNF:

1. **STUDENT** - Student information, academic details, authentication
2. **CLIENT** - Client/company information and verification
3. **SKILL** - Available skills categories and descriptions
4. **STUDENT_SKILL** - Student-skill relationships with proficiency levels
5. **TASK** - Task postings by clients with budgets and deadlines
6. **TASK_APPLICATION** - Student applications for tasks
7. **TASK_ASSIGNMENT** - Task assignments to students
8. **PAYMENT** - Payment records and transaction tracking
9. **RATING** - Mutual rating system between students and clients
10. **DISPUTE** - Dispute resolution tracking

### Normalization Achieved

The database is normalized up to **BCNF (Boyce-Codd Normal Form)**:

- ✅ **1NF**: All attributes contain atomic values
- ✅ **2NF**: No partial dependencies on composite keys
- ✅ **3NF**: No transitive dependencies
- ✅ **BCNF**: All determinants are candidate keys

### Key Relationships

- **STUDENT ↔ SKILL** (M:N) through STUDENT_SKILL junction table
- **CLIENT ↔ TASK** (1:N) - One client posts many tasks
- **STUDENT ↔ TASK** (M:N) through APPLICATION → ASSIGNMENT workflow
- **TASK_ASSIGNMENT** → PAYMENT/RATING/DISPUTE (1:1) relationships

## 🚀 Features

### Database Features
- Complete ER diagram with all relationships
- Primary and foreign key constraints with referential integrity
- Data integrity checks (NOT NULL, UNIQUE, CHECK constraints)
- Comprehensive sample data for testing
- Advanced SQL operations demonstration
- BCNF normalization ensuring zero redundancy

### Frontend Features
- **Dashboard**: Real-time statistics and activity tracking
- **Student Management**: CRUD operations for student records
- **Client Management**: CRUD operations for client records
- **Task Management**: Task posting, filtering, and status tracking
- **Skills Management**: Skill categories and student skill mapping
- **Search & Filter**: Dynamic search and filtering capabilities
- **Responsive Design**: Mobile-friendly interface

### SQL Operations Demonstrated
- Basic SELECT queries with WHERE conditions and ORDER BY
- Aggregate functions (COUNT, SUM, AVG, MAX, MIN)
- GROUP BY and HAVING clauses
- INNER and LEFT JOIN operations across multiple tables
- Subqueries and nested queries
- INSERT, UPDATE, DELETE operations with constraints
- Advanced analytical queries for business intelligence
- Window functions and CASE statements

## ⚙️ Setup Instructions

### 1. Database Setup
1. The Python server automatically creates `skillhub_crud.db` on first run
2. Alternatively, open **DB Browser for SQLite**
3. Create a new database: `skillhub_crud.db`
4. Execute `database_schema.sql` to create tables
5. Execute `sample_data.sql` to populate with sample data
6. Use `sql_operations.sql` to test various SQL operations

### 2. Backend Setup
1. Make sure Python is installed on your system
2. Run the Python server: `python server.py`
3. The server will start on port 8000
4. Access the application at `http://localhost:8000`

### 3. Frontend Setup
1. Open `crud_interface.html` in a modern web browser
2. The application will connect to the Python server
3. Navigate through different sections using the navigation menu
4. Use `emergency_test.html` for debugging and testing

### 4. Testing the System
- Start the Python server first (`python server.py`)
- Test CRUD operations on students, clients, and tasks
- Try search and filter functionality
- Explore the dashboard statistics
- View task details and status changes

## 📊 Database Schema Summary

### Key Tables and Relationships

```sql
STUDENT (student_id PK, first_name, last_name, email, university, major, graduation_year, ...)
CLIENT (client_id PK, company_name, contact_person, email, business_type, ...)
SKILL (skill_id PK, skill_name, category, description)
TASK (task_id PK, client_id FK, required_skill_id FK, title, budget, deadline, ...)
STUDENT_SKILL (student_skill_id PK, student_id FK, skill_id FK, proficiency_level, ...)
TASK_APPLICATION (application_id PK, task_id FK, student_id FK, status, ...)
TASK_ASSIGNMENT (assignment_id PK, task_id FK, student_id FK, completion_date, ...)
PAYMENT (payment_id PK, assignment_id FK, amount, payment_date, ...)
RATING (rating_id PK, assignment_id FK, client_rating, student_rating, ...)
DISPUTE (dispute_id PK, assignment_id FK, dispute_type, resolution_status, ...)
```

## 🔍 Sample SQL Queries

### Find Top Performing Students
```sql
SELECT 
    s.first_name, s.last_name,
    COUNT(ta.assignment_id) as completed_tasks,
    AVG(r.client_rating) as avg_rating,
    SUM(p.amount) as total_earnings
FROM STUDENT s
INNER JOIN TASK_ASSIGNMENT ta ON s.student_id = ta.student_id
INNER JOIN PAYMENT p ON ta.assignment_id = p.assignment_id
INNER JOIN RATING r ON ta.assignment_id = r.assignment_id
WHERE ta.completion_date IS NOT NULL
GROUP BY s.student_id
ORDER BY total_earnings DESC;
```

### Skill Demand Analysis
```sql
SELECT 
    sk.skill_name, sk.category,
    COUNT(t.task_id) as task_count,
    AVG(t.budget) as avg_budget
FROM SKILL sk
LEFT JOIN TASK t ON sk.skill_id = t.required_skill_id
GROUP BY sk.skill_id
ORDER BY task_count DESC;
```

### Monthly Task Trends
```sql
SELECT 
    strftime('%Y-%m', posting_date) as month,
    COUNT(*) as tasks_posted,
    SUM(budget) as total_budget,
    AVG(budget) as avg_budget
FROM TASK
GROUP BY strftime('%Y-%m', posting_date)
ORDER BY month;
```

## 🎓 Academic Requirements Met

✅ **Database Design**
- Entity identification and attributes analysis
- Primary and foreign key definitions
- Relationship mapping with cardinality
- ER diagram creation and visualization
- Relational schema conversion
- Normalization up to 3NF/BCNF

✅ **Database Implementation**
- SQL table creation with comprehensive constraints
- Sample data insertion and validation
- Data integrity enforcement
- Proper relationship handling and referential integrity

✅ **SQL Operations**
- Comprehensive SELECT queries with complex conditions
- INSERT, UPDATE, DELETE operations with validation
- Complex JOIN operations across multiple tables
- Subqueries and nested queries
- Aggregate functions and analytical queries
- GROUP BY and HAVING clauses
- Window functions and CASE statements

✅ **Full-Stack Development**
- HTML/CSS interface with responsive design
- JavaScript CRUD operations with async/await
- RESTful API design and implementation
- User authentication and security
- Real-time data updates and validation
- Error handling and debugging

## 🧩 Challenges Faced & Solutions

- **Database Design Complexity**: Solved through systematic ER diagram approach
- **Frontend-Backend Integration**: Resolved entity mapping and data serialization issues
- **Security Implementation**: Implemented password hashing, input validation, and SQL injection prevention
- **Performance Optimization**: Applied database indexing and query optimization
- **Cross-Platform Compatibility**: Ensured compatibility across different operating systems

## 🚀 Future Enhancements

- User authentication system with role-based access
- Real-time notifications for task updates
- Advanced search with multiple filters
- File upload for task attachments
- Payment gateway integration
- Mobile application development
- API endpoints for external integration
- Machine learning for task matching

## 📈 Project Statistics

- **Database Tables**: 10 fully normalized tables
- **SQL Queries**: 50+ complex queries implemented
- **API Endpoints**: Complete CRUD for all entities
- **Frontend Components**: 15+ interactive components
- **Security Features**: Authentication, authorization, input validation
- **Normalization**: BCNF compliant database design

## 🤝 Contributing

This project serves as a comprehensive demonstration of database management skills and can be extended based on specific requirements or academic needs. Contributions for improvements and enhancements are welcome.

## 📄 License

This project is created for educational purposes and is open for academic use and modification.

---

**This project represents a comprehensive learning journey in database systems, full-stack web development, and practical problem-solving, demonstrating both theoretical knowledge and practical implementation skills.**
