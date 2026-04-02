# Skill-Based Micro-Task Marketplace for Students

A comprehensive DBMS project that demonstrates database design, normalization, and full-stack development skills.

## Project Overview

The proposed system is a database-driven platform designed to connect students with clients who require short-term, skill-based micro-tasks. In the modern gig economy, students often seek small projects to gain practical experience and earn income. However, existing freelance platforms are primarily built for professionals and large-scale projects, lacking structured support for student-level micro-tasks.

This system provides a centralized database to manage student profiles, skills, client details, task postings, applications, task assignments, payments, ratings, and dispute records. It ensures transparency, accountability, and proper tracking of performance metrics.

## Technology Stack

- **Database**: SQLite (compatible with DB Browser)
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: JavaScript (client-side simulation)

## Project Structure

```
DBMS-Project/
├── database_design.md      # Complete ER diagram and database design
├── database_schema.sql      # SQL table creation with constraints
├── sample_data.sql         # Sample data insertion
├── sql_operations.sql       # Comprehensive SQL operations demo
├── index.html              # Main frontend application
├── styles.css              # Styling and responsive design
├── script.js               # JavaScript CRUD operations
└── README.md               # This file
```

## Database Design

### Entities and Relationships

The database consists of 10 main entities:

1. **STUDENT** - Student information and profiles
2. **CLIENT** - Client/company information
3. **SKILL** - Available skills categories
4. **STUDENT_SKILL** - Student-skill relationships (junction table)
5. **TASK** - Task postings by clients
6. **TASK_APPLICATION** - Student applications for tasks
7. **TASK_ASSIGNMENT** - Task assignments to students
8. **PAYMENT** - Payment records
9. **RATING** - Mutual rating system
10. **DISPUTE** - Dispute resolution tracking

### Normalization

The database is normalized up to **BCNF (Boyce-Codd Normal Form)**:

- **1NF**: All attributes contain atomic values
- **2NF**: No partial dependencies on composite keys
- **3NF**: No transitive dependencies
- **BCNF**: All determinants are candidate keys

## Features

### Database Features
- Complete ER diagram with all relationships
- Primary and foreign key constraints
- Data integrity checks (NOT NULL, UNIQUE, CHECK constraints)
- Comprehensive sample data
- Advanced SQL operations demonstration

### Frontend Features
- **Dashboard**: Real-time statistics and activity tracking
- **Student Management**: CRUD operations for student records
- **Client Management**: CRUD operations for client records
- **Task Management**: Task posting, filtering, and status tracking
- **Skills Management**: Skill categories and student skill mapping
- **Search & Filter**: Dynamic search and filtering capabilities
- **Responsive Design**: Mobile-friendly interface

### SQL Operations Demonstrated
- Basic SELECT queries with WHERE conditions
- Aggregate functions (COUNT, SUM, AVG, MAX, MIN)
- GROUP BY and HAVING clauses
- INNER and LEFT JOIN operations
- Subqueries and nested queries
- INSERT, UPDATE, DELETE operations
- Advanced analytical queries
- Window functions and CASE statements

## Setup Instructions

### 1. Database Setup
1. Open **DB Browser for SQLite**
2. Create a new database: `skill_marketplace.db`
3. Execute `database_schema.sql` to create tables
4. Execute `sample_data.sql` to populate with sample data
5. Use `sql_operations.sql` to test various SQL operations

### 2. Frontend Setup
1. Open `index.html` in a modern web browser
2. The application will load with sample data
3. Navigate through different sections using the navigation menu

### 3. Testing the System
- Test CRUD operations on students, clients, and tasks
- Try search and filter functionality
- Explore the dashboard statistics
- View task details and status changes

## Database Schema Summary

### Key Tables and Relationships

```sql
STUDENT (student_id PK, first_name, last_name, email, university, major, ...)
CLIENT (client_id PK, company_name, contact_person, email, business_type, ...)
SKILL (skill_id PK, skill_name, category, description)
TASK (task_id PK, client_id FK, required_skill_id FK, title, budget, ...)
STUDENT_SKILL (student_skill_id PK, student_id FK, skill_id FK, proficiency, ...)
TASK_APPLICATION (application_id PK, task_id FK, student_id FK, status, ...)
TASK_ASSIGNMENT (assignment_id PK, task_id FK, student_id FK, ...)
PAYMENT (payment_id PK, assignment_id FK, amount, status, ...)
RATING (rating_id PK, assignment_id FK, client_rating, student_rating, ...)
DISPUTE (dispute_id PK, assignment_id FK, dispute_type, resolution_status, ...)
```

## Sample SQL Queries

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

## Academic Requirements Met

✅ **Database Design**
- Entity identification and attributes
- Primary and foreign key definitions
- Relationship mapping
- ER diagram creation
- Relational schema conversion
- Normalization up to 3NF/BCNF

✅ **Database Implementation**
- SQL table creation with constraints
- Sample data insertion
- Data integrity enforcement
- Proper relationship handling

✅ **SQL Operations**
- Comprehensive SELECT queries
- INSERT, UPDATE, DELETE operations
- Complex JOIN operations
- Subqueries and nested queries
- Aggregate functions
- GROUP BY and HAVING clauses

✅ **Frontend Development**
- HTML/CSS interface
- CRUD operations
- Data visualization
- Responsive design
- User-friendly navigation

## Future Enhancements

- User authentication system
- Real-time notifications
- Advanced search with filters
- File upload for task attachments
- Payment gateway integration
- Mobile application development
- API endpoints for external integration

## Contributing

This project serves as a comprehensive demonstration of database management skills and can be extended based on specific requirements or academic needs.

## License

This project is created for educational purposes and is open for academic use and modification.
