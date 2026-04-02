# Database Design: Skill-Based Micro-Task Marketplace for Students

## A. Database Design

### 1. Entities and Attributes

#### STUDENT
- student_id (PK)
- first_name
- last_name
- email
- phone
- university
- major
- graduation_year
- registration_date
- profile_status

#### CLIENT
- client_id (PK)
- company_name
- contact_person
- email
- phone
- business_type
- registration_date
- verification_status

#### SKILL
- skill_id (PK)
- skill_name
- category
- description

#### STUDENT_SKILL
- student_skill_id (PK)
- student_id (FK)
- skill_id (FK)
- proficiency_level
- years_experience
- certification

#### TASK
- task_id (PK)
- client_id (FK)
- title
- description
- required_skill_id (FK)
- difficulty_level
- estimated_hours
- budget
- deadline
- posting_date
- status

#### TASK_APPLICATION
- application_id (PK)
- task_id (FK)
- student_id (FK)
- application_date
- proposed_rate
- cover_letter
- status

#### TASK_ASSIGNMENT
- assignment_id (PK)
- task_id (FK)
- student_id (FK)
- assigned_date
- start_date
- completion_date
- actual_hours
- final_payment

#### PAYMENT
- payment_id (PK)
- assignment_id (FK)
- amount
- payment_date
- payment_method
- status

#### RATING
- rating_id (PK)
- assignment_id (FK)
- client_rating
- student_rating
- client_feedback
- student_feedback
- rating_date

#### DISPUTE
- dispute_id (PK)
- assignment_id (FK)
- dispute_type
- description
- filed_date
- resolution_date
- resolution_status
- resolution_details

### 2. Primary Keys (PK)
- STUDENT: student_id
- CLIENT: client_id
- SKILL: skill_id
- STUDENT_SKILL: student_skill_id
- TASK: task_id
- TASK_APPLICATION: application_id
- TASK_ASSIGNMENT: assignment_id
- PAYMENT: payment_id
- RATING: rating_id
- DISPUTE: dispute_id

### 3. Foreign Keys (FK)
- STUDENT_SKILL.student_id → STUDENT.student_id
- STUDENT_SKILL.skill_id → SKILL.skill_id
- TASK.client_id → CLIENT.client_id
- TASK.required_skill_id → SKILL.skill_id
- TASK_APPLICATION.task_id → TASK.task_id
- TASK_APPLICATION.student_id → STUDENT.student_id
- TASK_ASSIGNMENT.task_id → TASK.task_id
- TASK_ASSIGNMENT.student_id → STUDENT.student_id
- PAYMENT.assignment_id → TASK_ASSIGNMENT.assignment_id
- RATING.assignment_id → TASK_ASSIGNMENT.assignment_id
- DISPUTE.assignment_id → TASK_ASSIGNMENT.assignment_id

### 4. Relationships

#### One-to-Many Relationships:
- CLIENT → TASK (1:N)
- STUDENT → STUDENT_SKILL (1:N)
- SKILL → STUDENT_SKILL (1:N)
- SKILL → TASK (1:N)
- TASK → TASK_APPLICATION (1:N)
- STUDENT → TASK_APPLICATION (1:N)
- TASK → TASK_ASSIGNMENT (1:N)
- STUDENT → TASK_ASSIGNMENT (1:N)
- TASK_ASSIGNMENT → PAYMENT (1:N)
- TASK_ASSIGNMENT → RATING (1:N)
- TASK_ASSIGNMENT → DISPUTE (1:N)

#### Many-to-Many Relationships (resolved through junction tables):
- STUDENT ↔ SKILL (through STUDENT_SKILL)

### 5. ER Diagram

```
                    ┌─────────────────┐
                    │     CLIENT      │
                    ├─────────────────┤
                    │ client_id (PK)  │
                    │ company_name    │
                    │ contact_person  │
                    │ email           │
                    │ phone           │
                    │ business_type   │
                    │ registration_date│
                    │ verification_status│
                    └─────────────────┘
                         │
                         │ 1
                         │
                         ◇ POSTS
                         │ N
                         │
                    ┌─────────────────┐
                    │      TASK        │
                    ├─────────────────┤
                    │ task_id (PK)     │
                    │ title            │
                    │ description      │
                    │ difficulty_level │
                    │ estimated_hours  │
                    │ budget           │
                    │ deadline         │
                    │ posting_date     │
                    │ status           │
                    └─────────────────┘
                         │
                         │ 1
                         │
                         ◇ REQUIRES
                         │ N
                         │
                    ┌─────────────────┐
                    │      SKILL       │
                    ├─────────────────┤
                    │ skill_id (PK)    │
                    │ skill_name       │
                    │ category         │
                    │ description      │
                    └─────────────────┘

    ┌─────────────────┐      ◇ APPLIES_FOR      ┌─────────────────┐
    │    STUDENT      │◀───── N ────── M ─────▶│ TASK_APPLICATION │
    ├─────────────────┤                      ├─────────────────┤
    │ student_id (PK) │                      │ application_id (PK)│
    │ first_name      │                      │ application_date │
    │ last_name       │                      │ proposed_rate    │
    │ email           │                      │ cover_letter     │
    │ phone           │                      │ status           │
    │ university      │                      └─────────────────┘
    │ major           │                              │
    │ graduation_year │                              │ 1
    │ registration_date│                             │
    │ profile_status  │                              │
    └─────────────────┘                              │
           │                                        │
           │ 1                                      │
           │                                        │
           ◇ HAS                                    ◇ PROCESSES
           │ N                                      │ 1
           │                                        │
           ▼                                        ▼
    ┌─────────────────┐                      ┌─────────────────┐
    │  STUDENT_SKILL   │                      │ TASK_ASSIGNMENT │
    ├─────────────────┤                      ├─────────────────┤
    │ student_skill_id (PK)│                  │ assignment_id (PK)│
    │ proficiency_level │                     │ assigned_date    │
    │ years_experience  │                     │ start_date       │
    │ certification    │                     │ completion_date  │
    └─────────────────┘                     │ actual_hours     │
           │                                 │ final_payment    │
           │ 1                               └─────────────────┘
           │                                        │
           │                                        │ 1
           │                                        │
           └────────────────────────────────────────┘
                                │
                                │ 1
                                │
                                ◇ GENERATES
                                │ 1
                                │
                                ▼
                    ┌─────────────────┐
                    │     PAYMENT      │
                    ├─────────────────┤
                    │ payment_id (PK)  │
                    │ amount           │
                    │ payment_date     │
                    │ payment_method   │
                    │ status           │
                    └─────────────────┘

                    ┌─────────────────┐
                    │     RATING      │
                    ├─────────────────┤
                    │ rating_id (PK)   │
                    │ client_rating    │
                    │ student_rating   │
                    │ client_feedback  │
                    │ student_feedback │
                    │ rating_date      │
                    └─────────────────┘

                    ┌─────────────────┐
                    │     DISPUTE     │
                    ├─────────────────┤
                    │ dispute_id (PK)  │
                    │ dispute_type     │
                    │ description      │
                    │ filed_date       │
                    │ resolution_date  │
                    │ resolution_status│
                    │ resolution_details│
                    └─────────────────┘
```

#### Relationship Details with Cardinality and Participation

**1. CLIENT - TASK Relationship**
- **Relationship Name**: POSTS
- **Cardinality**: 1:N (One-to-Many)
- **Participation**: 
  - CLIENT: Total participation (every client must post at least one task)
  - TASK: Total participation (every task must be posted by exactly one client)

**2. TASK - SKILL Relationship**
- **Relationship Name**: REQUIRES
- **Cardinality**: N:1 (Many-to-One)
- **Participation**:
  - TASK: Total participation (every task requires exactly one skill)
  - SKILL: Partial participation (a skill may not be required by any task)

**3. STUDENT - TASK_APPLICATION Relationship**
- **Relationship Name**: APPLIES_FOR
- **Cardinality**: M:N (Many-to-Many)
- **Participation**:
  - STUDENT: Partial participation (a student may not apply for any task)
  - TASK: Partial participation (a task may not receive any applications)

**4. STUDENT - STUDENT_SKILL Relationship**
- **Relationship Name**: HAS
- **Cardinality**: 1:N (One-to-Many)
- **Participation**:
  - STUDENT: Partial participation (a student may not have any skills listed)
  - STUDENT_SKILL: Total participation (every student-skill record must belong to a student)

**5. SKILL - STUDENT_SKILL Relationship**
- **Relationship Name**: POSSESSES
- **Cardinality**: 1:N (One-to-Many)
- **Participation**:
  - SKILL: Partial participation (a skill may not be possessed by any student)
  - STUDENT_SKILL: Total participation (every student-skill record must have a skill)

**6. TASK_APPLICATION - TASK_ASSIGNMENT Relationship**
- **Relationship Name**: PROCESSES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_APPLICATION: Partial participation (not all applications become assignments)
  - TASK_ASSIGNMENT: Total participation (every assignment comes from an application)

**7. TASK_ASSIGNMENT - PAYMENT Relationship**
- **Relationship Name**: GENERATES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_ASSIGNMENT: Partial participation (not all assignments have payments yet)
  - PAYMENT: Total participation (every payment belongs to exactly one assignment)

**8. TASK_ASSIGNMENT - RATING Relationship**
- **Relationship Name**: EVALUATES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_ASSIGNMENT: Partial participation (not all assignments have ratings)
  - RATING: Total participation (every rating belongs to exactly one assignment)

**9. TASK_ASSIGNMENT - DISPUTE Relationship**
- **Relationship Name**: DISPUTES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_ASSIGNMENT: Partial participation (not all assignments have disputes)
  - DISPUTE: Total participation (every dispute belongs to exactly one assignment)

#### ER Diagram Legend
- **PK**: Primary Key
- **FK**: Foreign Key
- **◇**: Relationship Diamond
- **1**: One side of relationship
- **N**: Many side of relationship
- **M**: Many side of relationship (for M:N)
- **Total Participation**: Entity must participate in the relationship
- **Partial Participation**: Entity may or may not participate in the relationship

### 6. Relational Schema

#### STUDENT(student_id, first_name, last_name, email, phone, university, major, graduation_year, registration_date, profile_status)

#### CLIENT(client_id, company_name, contact_person, email, phone, business_type, registration_date, verification_status)

#### SKILL(skill_id, skill_name, category, description)

#### STUDENT_SKILL(student_skill_id, student_id, skill_id, proficiency_level, years_experience, certification)

#### TASK(task_id, client_id, title, description, required_skill_id, difficulty_level, estimated_hours, budget, deadline, posting_date, status)

#### TASK_APPLICATION(application_id, task_id, student_id, application_date, proposed_rate, cover_letter, status)

#### TASK_ASSIGNMENT(assignment_id, task_id, student_id, assigned_date, start_date, completion_date, actual_hours, final_payment)

#### PAYMENT(payment_id, assignment_id, amount, payment_date, payment_method, status)

#### RATING(rating_id, assignment_id, client_rating, student_rating, client_feedback, student_feedback, rating_date)

#### DISPUTE(dispute_id, assignment_id, dispute_type, description, filed_date, resolution_date, resolution_status, resolution_details)

### 7. Normalization Analysis

#### First Normal Form (1NF):
- All tables have atomic values
- Each row is uniquely identifiable
- All attributes have single values

#### Second Normal Form (2NF):
- All tables are in 1NF
- All non-key attributes are fully dependent on the primary key
- No partial dependencies exist

#### Third Normal Form (3NF):
- All tables are in 2NF
- No transitive dependencies exist
- All non-key attributes depend only on the primary key

#### Boyce-Codd Normal Form (BCNF):
- All determinants are candidate keys
- No anomalies in insertion, deletion, or update
- All tables satisfy BCNF requirements

The database design is normalized up to BCNF, ensuring data integrity and eliminating redundancy.
