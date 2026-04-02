# Proper ER Diagram with Relationships, Cardinality, and Participation

## ER Diagram with Standard Notation

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

## Relationship Details with Cardinality and Participation

### 1. CLIENT - TASK Relationship
- **Relationship Name**: POSTS
- **Cardinality**: 1:N (One-to-Many)
- **Participation**: 
  - CLIENT: Total participation (every client must post at least one task)
  - TASK: Total participation (every task must be posted by exactly one client)
- **Description**: One client can post many tasks, but each task is posted by exactly one client

### 2. TASK - SKILL Relationship
- **Relationship Name**: REQUIRES
- **Cardinality**: N:1 (Many-to-One)
- **Participation**:
  - TASK: Total participation (every task requires exactly one skill)
  - SKILL: Partial participation (a skill may not be required by any task)
- **Description**: Many tasks can require the same skill, but each task requires exactly one skill

### 3. STUDENT - TASK_APPLICATION Relationship
- **Relationship Name**: APPLIES_FOR
- **Cardinality**: M:N (Many-to-Many)
- **Participation**:
  - STUDENT: Partial participation (a student may not apply for any task)
  - TASK: Partial participation (a task may not receive any applications)
- **Description**: A student can apply for many tasks, and a task can receive many applications

### 4. STUDENT - STUDENT_SKILL Relationship
- **Relationship Name**: HAS
- **Cardinality**: 1:N (One-to-Many)
- **Participation**:
  - STUDENT: Partial participation (a student may not have any skills listed)
  - STUDENT_SKILL: Total participation (every student-skill record must belong to a student)
- **Description**: One student can have many skills, but each student-skill record belongs to exactly one student

### 5. SKILL - STUDENT_SKILL Relationship
- **Relationship Name**: POSSESSES
- **Cardinality**: 1:N (One-to-Many)
- **Participation**:
  - SKILL: Partial participation (a skill may not be possessed by any student)
  - STUDENT_SKILL: Total participation (every student-skill record must have a skill)
- **Description**: One skill can be possessed by many students, but each student-skill record has exactly one skill

### 6. TASK_APPLICATION - TASK_ASSIGNMENT Relationship
- **Relationship Name**: PROCESSES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_APPLICATION: Partial participation (not all applications become assignments)
  - TASK_ASSIGNMENT: Total participation (every assignment comes from an application)
- **Description**: An accepted application becomes exactly one assignment

### 7. TASK_ASSIGNMENT - PAYMENT Relationship
- **Relationship Name**: GENERATES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_ASSIGNMENT: Partial participation (not all assignments have payments yet)
  - PAYMENT: Total participation (every payment belongs to exactly one assignment)
- **Description**: One assignment generates at most one payment, and each payment belongs to exactly one assignment

### 8. TASK_ASSIGNMENT - RATING Relationship
- **Relationship Name**: EVALUATES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_ASSIGNMENT: Partial participation (not all assignments have ratings)
  - RATING: Total participation (every rating belongs to exactly one assignment)
- **Description**: One assignment can have at most one rating, and each rating belongs to exactly one assignment

### 9. TASK_ASSIGNMENT - DISPUTE Relationship
- **Relationship Name**: DISPUTES
- **Cardinality**: 1:1 (One-to-One)
- **Participation**:
  - TASK_ASSIGNMENT: Partial participation (not all assignments have disputes)
  - DISPUTE: Total participation (every dispute belongs to exactly one assignment)
- **Description**: One assignment can have at most one dispute, and each dispute belongs to exactly one assignment

## ER Diagram Legend
- **PK**: Primary Key
- **FK**: Foreign Key
- **◇**: Relationship Diamond
- **1**: One side of relationship
- **N**: Many side of relationship
- **M**: Many side of relationship (for M:N)
- **Total Participation**: Entity must participate in the relationship
- **Partial Participation**: Entity may or may not participate in the relationship

## Summary of All Relationships

| Relationship | Cardinality | Participation (Entity 1) | Participation (Entity 2) |
|-------------|-------------|-------------------------|-------------------------|
| CLIENT - TASK | 1:N | Total | Total |
| TASK - SKILL | N:1 | Total | Partial |
| STUDENT - TASK_APPLICATION | M:N | Partial | Partial |
| STUDENT - STUDENT_SKILL | 1:N | Partial | Total |
| SKILL - STUDENT_SKILL | 1:N | Partial | Total |
| TASK_APPLICATION - TASK_ASSIGNMENT | 1:1 | Partial | Total |
| TASK_ASSIGNMENT - PAYMENT | 1:1 | Partial | Total |
| TASK_ASSIGNMENT - RATING | 1:1 | Partial | Total |
| TASK_ASSIGNMENT - DISPUTE | 1:1 | Partial | Total |
