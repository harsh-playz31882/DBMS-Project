# Database Schema Documentation
## Skill-Based Micro-Task Marketplace for Students

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Entity Relationship Diagram](#entity-relationship-diagram)
3. [Table Structures](#table-structures)
4. [Relationship Definitions](#relationship-definitions)
5. [Normalization Analysis](#normalization-analysis)
6. [Business Rules](#business-rules)

---

## 🎯 Overview

This database implements a comprehensive skill-based micro-task marketplace system that connects students with clients for freelance work. The system manages student profiles, client information, skills, tasks, applications, assignments, payments, ratings, and disputes.

**Key Features:**
- Student skill management and proficiency tracking
- Client task posting and management
- Task application and assignment workflow
- Payment processing and rating system
- Dispute resolution mechanism

---

## 🔗 Entity Relationship Diagram

```
┌─────────────┐     ┌──────────┐     ┌──────────┐
│   STUDENT   │─────│STUDENT_SKILL│─────│  SKILL    │
└─────────────┘     └──────────┘     └──────────┘
       │                │                   │
       │                │                   │
       │                │                   │
       │                ▼                   ▼
       │          ┌─────────────┐     ┌──────────┐
       └──────────│TASK_APPLICATION│─────│   TASK    │
                  └─────────────┘     └──────────┘
                       │                   │
                       │                   │
                       ▼                   ▼
                  ┌─────────────┐     ┌──────────┐
                  │TASK_ASSIGNMENT│─────│  CLIENT   │
                  └─────────────┘     └──────────┘
                       │
                       │
                       ▼
                  ┌─────────────┐
                  │   PAYMENT   │
                  └─────────────┘
                       │
                       ▼
                  ┌─────────────┐
                  │   RATING    │
                  └─────────────┘
                       │
                       ▼
                  ┌─────────────┐
                  │  DISPUTE    │
                  └─────────────┘
```

---

## 📊 Table Structures

### 1. STUDENT Table
**Purpose**: Stores student personal information and academic details

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| student_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique student identifier |
| first_name | VARCHAR(50) | NOT NULL | Student's first name |
| last_name | VARCHAR(50) | NOT NULL | Student's last name |
| email | VARCHAR(100) UNIQUE NOT NULL | Student's email address (unique login) |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password for authentication |
| salt | VARCHAR(32) | NOT NULL | Password salt for security |
| phone | VARCHAR(20) | NULL | Contact phone number |
| university | VARCHAR(100) | NOT NULL | Educational institution |
| major | VARCHAR(50) | NOT NULL | Field of study |
| graduation_year | INTEGER | NOT NULL CHECK(2020-2030) | Expected graduation year |
| registration_date | DATE | NOT NULL DEFAULT CURRENT_DATE | Account creation date |
| profile_status | VARCHAR(20) | DEFAULT 'active' CHECK(active,inactive,suspended) | Account status |
| last_login | TIMESTAMP | NULL | Last successful login timestamp |
| login_attempts | INTEGER | DEFAULT 0 | Failed login attempts |
| account_locked | BOOLEAN | DEFAULT FALSE | Account security lock status |
| email_verified | BOOLEAN | DEFAULT FALSE | Email verification status |

---

### 2. CLIENT Table
**Purpose**: Stores client company information and contact details

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| client_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique client identifier |
| company_name | VARCHAR(100) | NOT NULL | Company or organization name |
| contact_person | VARCHAR(100) | NOT NULL | Primary contact person |
| email | VARCHAR(100) UNIQUE NOT NULL | Client email address (unique login) |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password for authentication |
| salt | VARCHAR(32) | NOT NULL | Password salt for security |
| phone | VARCHAR(20) | NULL | Contact phone number |
| business_type | VARCHAR(50) | NOT NULL | Industry or business sector |
| registration_date | DATE | NOT NULL DEFAULT CURRENT_DATE | Account creation date |
| verification_status | VARCHAR(20) | DEFAULT 'pending' CHECK(pending,active,suspended) | Account verification status |
| last_login | TIMESTAMP | NULL | Last successful login timestamp |
| login_attempts | INTEGER | DEFAULT 0 | Failed login attempts |
| account_locked | BOOLEAN | DEFAULT FALSE | Account security lock status |
| email_verified | BOOLEAN | DEFAULT FALSE | Email verification status |

---

### 3. SKILL Table
**Purpose**: Stores available skills and categories

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| skill_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique skill identifier |
| skill_name | VARCHAR(50) UNIQUE NOT NULL | Skill name (e.g., "JavaScript", "Python") |
| category | VARCHAR(50) | NOT NULL | Skill category (e.g., "Programming", "Design") |
| description | TEXT | NULL | Detailed skill description or requirements |

---

### 4. STUDENT_SKILL Table (Junction Table)
**Purpose**: Many-to-many relationship between students and skills

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| student_skill_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique relationship identifier |
| student_id | INTEGER | NOT NULL FOREIGN KEY → STUDENT.student_id | Student reference |
| skill_id | INTEGER | NOT NULL FOREIGN KEY → SKILL.skill_id | Skill reference |
| proficiency_level | VARCHAR(20) | NOT NULL CHECK(beginner,intermediate,advanced,expert) | Skill proficiency level |
| years_experience | DECIMAL(3,1) | CHECK(0-10) | Years of experience |
| certification | VARCHAR(100) | NULL | Professional certifications |

---

### 5. TASK Table
**Purpose**: Stores freelance tasks posted by clients

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| task_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique task identifier |
| client_id | INTEGER | NOT NULL FOREIGN KEY → CLIENT.client_id | Client who posted task |
| title | VARCHAR(200) | NOT NULL | Task title and description |
| description | TEXT | NOT NULL | Detailed task requirements |
| required_skill_id | INTEGER | FOREIGN KEY → SKILL.skill_id | Primary skill required |
| difficulty_level | VARCHAR(20) | NOT NULL | Task difficulty assessment |
| estimated_hours | INTEGER | NOT NULL | Expected completion time |
| budget | DECIMAL(10,2) | NOT NULL | Task payment amount |
| deadline | DATE | NOT NULL | Task completion deadline |
| posting_date | DATE | NOT NULL DEFAULT CURRENT_DATE | When task was posted |
| status | VARCHAR(20) | DEFAULT 'open' CHECK(open,in_progress,completed,cancelled) | Current task status |

---

### 6. TASK_APPLICATION Table
**Purpose**: Manages student applications for tasks

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| application_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique application identifier |
| task_id | INTEGER | NOT NULL FOREIGN KEY → TASK.task_id | Task being applied for |
| student_id | INTEGER | NOT NULL FOREIGN KEY → STUDENT.student_id | Student applying |
| application_date | DATE | NOT NULL DEFAULT CURRENT_DATE | When application was submitted |
| proposed_rate | DECIMAL(8,2) | NULL | Student's proposed hourly rate |
| cover_letter | TEXT | NULL | Application cover letter |
| status | VARCHAR(20) | DEFAULT 'pending' CHECK(pending,accepted,rejected) | Application status |

---

### 7. TASK_ASSIGNMENT Table
**Purpose**: Links accepted applications to actual work assignments

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| assignment_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique assignment identifier |
| task_id | INTEGER | NOT NULL FOREIGN KEY → TASK.task_id | Task being assigned |
| student_id | INTEGER | NOT NULL FOREIGN KEY → STUDENT.student_id | Student assigned to task |
| assigned_date | DATE | NOT NULL DEFAULT CURRENT_DATE | When assignment was made |
| start_date | DATE | NULL | When work actually began |
| completion_date | DATE | NULL | When work was completed |
| actual_hours | DECIMAL(5,1) | NULL | Actual hours worked |
| final_payment | DECIMAL(10,2) | NULL | Final payment amount |

---

### 8. PAYMENT Table
**Purpose**: Records payments for completed assignments

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| payment_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique payment identifier |
| assignment_id | INTEGER | NOT NULL FOREIGN KEY → TASK_ASSIGNMENT.assignment_id | Assignment being paid for |
| amount | DECIMAL(10,2) | NOT NULL | Payment amount |
| payment_date | DATE | NOT NULL DEFAULT CURRENT_DATE | When payment was made |
| payment_method | VARCHAR(20) | DEFAULT 'credit_card' | Payment method used |
| status | VARCHAR(20) | DEFAULT 'completed' CHECK(pending,completed,failed) | Payment status |

---

### 9. RATING Table
**Purpose**: Stores mutual ratings between clients and students

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| rating_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique rating identifier |
| assignment_id | INTEGER | NOT NULL FOREIGN KEY → TASK_ASSIGNMENT.assignment_id | Assignment being rated |
| client_rating | INTEGER | CHECK(1-5) | Client's rating of student (1-5 stars) |
| student_rating | INTEGER | CHECK(1-5) | Student's rating of client (1-5 stars) |
| client_feedback | TEXT | NULL | Client's feedback comments |
| student_feedback | TEXT | NULL | Student's feedback comments |
| rating_date | DATE | NOT NULL DEFAULT CURRENT_DATE | When rating was submitted |

---

### 10. DISPUTE Table
**Purpose**: Manages disputes for task assignments

| Column Name | Data Type | Constraints | Description |
|-------------|-------------|-------------|-------------|
| dispute_id | INTEGER PRIMARY KEY AUTOINCREMENT | NOT NULL | Unique dispute identifier |
| assignment_id | INTEGER | NOT NULL FOREIGN KEY → TASK_ASSIGNMENT.assignment_id | Assignment being disputed |
| dispute_type | VARCHAR(20) | NOT NULL | Type of dispute (payment,quality,deadline,etc.) |
| description | TEXT | NOT NULL | Detailed dispute description |
| filed_date | DATE | NOT NULL DEFAULT CURRENT_DATE | When dispute was filed |
| resolution_date | DATE | NULL | When dispute was resolved |
| resolution_status | VARCHAR(20) | DEFAULT 'open' CHECK(open,resolved,dismissed) | Current dispute status |
| resolution_details | TEXT | NULL | Resolution explanation |

---

## 🔗 Relationship Definitions

### Primary Relationships

#### 1. CLIENT ↔ TASK (1:N)
- **Name**: POSTS
- **Description**: One client can post many tasks
- **Business Rule**: Every task must be posted by exactly one client
- **Cardinality**: 1 client → N tasks
- **Participation**: 
  - CLIENT: Total (must post at least one task to be active)
  - TASK: Total (every task belongs to exactly one client)

#### 2. STUDENT ↔ SKILL (M:N through STUDENT_SKILL)
- **Name**: POSSESSES/HAS
- **Description**: Students can have many skills, skills can be possessed by many students
- **Business Rule**: Proficiency levels and experience tracked per student-skill combination
- **Cardinality**: M students ↔ N skills
- **Participation**: 
  - STUDENT: Partial (may have zero or many skills)
  - SKILL: Partial (may be possessed by zero or many students)
  - STUDENT_SKILL: Total (every record links specific student to specific skill)

#### 3. TASK ↔ SKILL (N:1)
- **Name**: REQUIRES
- **Description**: Each task requires exactly one primary skill
- **Business Rule**: Tasks can be filtered by required skill
- **Cardinality**: N tasks → 1 skill
- **Participation**: 
  - TASK: Total (every task requires exactly one skill)
  - SKILL: Partial (may not be required by any task)

#### 4. STUDENT ↔ TASK (M:N through TASK_APPLICATION → TASK_ASSIGNMENT)
- **Name**: APPLIES_FOR → PROCESSES
- **Description**: Students apply for tasks, accepted applications become assignments
- **Business Rule**: Application must be accepted before work can begin
- **Cardinality**: M students ↔ N tasks
- **Participation**: 
  - STUDENT: Partial (may apply for zero or many tasks)
  - TASK: Partial (may receive zero or many applications)
  - TASK_APPLICATION: Partial (not all applications become assignments)
  - TASK_ASSIGNMENT: Total (every assignment comes from an accepted application)

#### 5. TASK_ASSIGNMENT ↔ PAYMENT (1:1)
- **Name**: GENERATES
- **Description**: Each completed assignment generates one payment
- **Business Rule**: Payment recorded only after assignment completion
- **Cardinality**: 1 assignment → 1 payment
- **Participation**: 
  - TASK_ASSIGNMENT: Partial (not all assignments have payments yet)
  - PAYMENT: Total (every payment belongs to exactly one assignment)

#### 6. TASK_ASSIGNMENT ↔ RATING (1:1)
- **Name**: EVALUATES
- **Description**: Completed assignments can be rated by both parties
- **Business Rule**: Mutual rating system for quality assurance
- **Cardinality**: 1 assignment → 1 rating
- **Participation**: 
  - TASK_ASSIGNMENT: Partial (not all assignments have ratings)
  - RATING: Total (every rating belongs to exactly one assignment)

#### 7. TASK_ASSIGNMENT ↔ DISPUTE (1:1)
- **Name**: DISPUTES
- **Description**: Disputes can be filed for assignments
- **Business Rule**: Dispute resolution process with status tracking
- **Cardinality**: 1 assignment → 1 dispute
- **Participation**: 
  - TASK_ASSIGNMENT: Partial (not all assignments have disputes)
  - DISPUTE: Total (every dispute belongs to exactly one assignment)

---

## 📐 Normalization Analysis

### First Normal Form (1NF) ✅
- **Atomic Values**: All attributes contain single, indivisible values
- **Primary Keys**: Each table has a unique identifier
- **No Repeating Groups**: No multi-valued attributes in single columns

### Second Normal Form (2NF) ✅
- **1NF Compliance**: All tables satisfy 1NF requirements
- **Full Functional Dependency**: All non-key attributes fully dependent on primary key
- **No Partial Dependencies**: No attribute depends on only part of composite key

### Third Normal Form (3NF) ✅
- **2NF Compliance**: All tables satisfy 2NF requirements  
- **No Transitive Dependencies**: No non-key attributes depend on other non-key attributes
- **Key-Only Dependencies**: All attributes depend directly on primary key

### Boyce-Codd Normal Form (BCNF) ✅
- **3NF Compliance**: All tables satisfy 3NF requirements
- **Determinant Analysis**: All determinants are candidate keys
- **No Anomalies**: No insertion, deletion, or update anomalies

**Result**: Database is fully normalized to BCNF, ensuring data integrity and eliminating redundancy.

---

## 📋 Business Rules

### Data Integrity Rules
1. **Unique Emails**: No two users (students/clients) can share the same email
2. **Skill Uniqueness**: No duplicate skill names in the SKILL table
3. **Application Workflow**: Task → Application → Assignment → Payment → Rating
4. **Status Transitions**: 
   - Tasks: open → in_progress → completed/cancelled
   - Applications: pending → accepted/rejected
   - Assignments: assigned → in_progress → completed
5. **Rating Constraints**: Ratings must be between 1-5 stars
6. **Payment Validation**: Final payments cannot exceed task budget

### Access Control Rules
1. **Account Locking**: 3 failed login attempts triggers account lock
2. **Email Verification**: New accounts require email verification
3. **Profile Status**: Inactive accounts cannot apply for tasks
4. **Client Verification**: New clients require admin verification

### Workflow Rules
1. **Task Posting**: Only verified clients can post tasks
2. **Skill Requirements**: Every task must specify at least one required skill
3. **Application Process**: Students can only apply for open tasks
4. **Assignment Creation**: Only accepted applications become assignments
5. **Payment Processing**: Payments recorded only for completed assignments
6. **Dispute Resolution**: All disputes must have resolution status and details

---

## 🔍 Query Examples

### Basic Operations
```sql
-- Get all students with their skills
SELECT s.first_name, s.last_name, sk.skill_name, ss.proficiency_level
FROM STUDENT s
JOIN STUDENT_SKILL ss ON s.student_id = ss.student_id
JOIN SKILL sk ON ss.skill_id = sk.skill_id;

-- Find high-budget tasks
SELECT title, budget, deadline 
FROM TASK 
WHERE status = 'open' AND budget > 500;

-- Client activity analysis
SELECT c.company_name, COUNT(t.task_id) as total_tasks, SUM(t.budget) as total_spent
FROM CLIENT c
LEFT JOIN TASK t ON c.client_id = t.client_id
GROUP BY c.client_id, c.company_name;
```

### Advanced Analytics
```sql
-- Student performance metrics
SELECT 
    s.first_name,
    s.last_name,
    COUNT(DISTINCT ta.assignment_id) as completed_tasks,
    AVG(r.client_rating) as avg_rating,
    SUM(p.amount) as total_earnings
FROM STUDENT s
JOIN TASK_ASSIGNMENT ta ON s.student_id = ta.student_id
JOIN PAYMENT p ON ta.assignment_id = p.assignment_id
JOIN RATING r ON ta.assignment_id = r.assignment_id
WHERE ta.completion_date IS NOT NULL
GROUP BY s.student_id, s.first_name, s.last_name;

-- Monthly task trends
SELECT 
    strftime('%Y-%m', posting_date) as month,
    COUNT(*) as tasks_posted,
    SUM(budget) as total_budget,
    AVG(budget) as avg_budget
FROM TASK
GROUP BY strftime('%Y-%m', posting_date)
ORDER BY month;
```

---

## 📊 Database Statistics

### Current Data Distribution
- **Students**: 2 active profiles
- **Clients**: 2 registered companies  
- **Skills**: 11 available skills
- **Tasks**: 10 posted tasks
- **Applications**: Managed through application workflow
- **Assignments**: Tracked through assignment system
- **Payments**: Recorded for completed work
- **Ratings**: Mutual evaluation system
- **Disputes**: Resolution tracking system

### Performance Considerations
- **Indexing Strategy**: Primary keys and foreign keys indexed
- **Query Optimization**: JOIN operations use indexed columns
- **Data Growth**: Designed to scale with user base
- **Backup Strategy**: Regular database dumps recommended

---

## 🛠️ Technical Implementation

### Database Engine: SQLite 3.x
### Character Set: UTF-8
### Collation: Binary (default)
### Transaction Support: ACID compliant
### Concurrency: File-based locking (single writer)

---

*This schema documentation provides a comprehensive overview of the relational database structure, relationships, and business rules for the Skill-Based Micro-Task Marketplace system.*
