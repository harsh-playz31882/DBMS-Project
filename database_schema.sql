-- Skill-Based Micro-Task Marketplace Database Schema
-- SQLite Database Implementation


DROP TABLE IF EXISTS DISPUTE;
DROP TABLE IF EXISTS RATING;
DROP TABLE IF EXISTS PAYMENT;
DROP TABLE IF EXISTS TASK_ASSIGNMENT;
DROP TABLE IF EXISTS TASK_APPLICATION;
DROP TABLE IF EXISTS TASK;
DROP TABLE IF EXISTS STUDENT_SKILL;
DROP TABLE IF EXISTS SKILL;
DROP TABLE IF EXISTS STUDENT;
DROP TABLE IF EXISTS CLIENT;

-- Enhanced STUDENT table with authentication fields
CREATE TABLE STUDENT (
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
);

-- Enhanced CLIENT table with authentication fields
CREATE TABLE CLIENT (
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
);

-- User Sessions table for session management
CREATE TABLE USER_SESSIONS (
    session_id VARCHAR(255) PRIMARY KEY,
    user_id INTEGER NOT NULL,
    user_type VARCHAR(10) NOT NULL CHECK(user_type IN ('student', 'client')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Password Reset Tokens table
CREATE TABLE PASSWORD_RESET_TOKENS (
    token_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    user_type VARCHAR(10) NOT NULL CHECK(user_type IN ('student', 'client')),
    token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_used BOOLEAN DEFAULT FALSE
);

-- Login Attempts tracking for security
CREATE TABLE LOGIN_ATTEMPTS (
    attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(100) NOT NULL,
    user_type VARCHAR(10) NOT NULL CHECK(user_type IN ('student', 'client')),
    ip_address VARCHAR(45),
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    success BOOLEAN DEFAULT FALSE,
    failure_reason VARCHAR(50)
);

-- Create SKILL table
CREATE TABLE SKILL (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name VARCHAR(50) UNIQUE NOT NULL,
    category VARCHAR(30) NOT NULL,
    description TEXT
);

-- Create STUDENT_SKILL junction table
CREATE TABLE STUDENT_SKILL (
    student_skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    skill_id INTEGER NOT NULL,
    proficiency_level VARCHAR(20) NOT NULL CHECK(proficiency_level IN ('beginner', 'intermediate', 'advanced', 'expert')),
    years_experience DECIMAL(3,1) CHECK(years_experience >= 0 AND years_experience <= 10),
    certification VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES SKILL(skill_id) ON DELETE CASCADE,
    UNIQUE(student_id, skill_id)
);

-- Create TASK table
CREATE TABLE TASK (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    required_skill_id INTEGER NOT NULL,
    difficulty_level VARCHAR(20) NOT NULL CHECK(difficulty_level IN ('easy', 'medium', 'hard', 'expert')),
    estimated_hours DECIMAL(4,1) NOT NULL CHECK(estimated_hours > 0 AND estimated_hours <= 100),
    budget DECIMAL(10,2) NOT NULL CHECK(budget > 0),
    deadline DATE NOT NULL,
    posting_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'open' CHECK(status IN ('open', 'in_progress', 'completed', 'cancelled')),
    FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
    FOREIGN KEY (required_skill_id) REFERENCES SKILL(skill_id)
);

-- Create TASK_APPLICATION table
CREATE TABLE TASK_APPLICATION (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    application_date DATE NOT NULL DEFAULT CURRENT_DATE,
    proposed_rate DECIMAL(10,2) NOT NULL CHECK(proposed_rate > 0),
    cover_letter TEXT,
    status VARCHAR(20) DEFAULT 'pending' CHECK(status IN ('pending', 'accepted', 'rejected', 'withdrawn')),
    FOREIGN KEY (task_id) REFERENCES TASK(task_id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id) ON DELETE CASCADE,
    UNIQUE(task_id, student_id)
);

-- Create TASK_ASSIGNMENT table
CREATE TABLE TASK_ASSIGNMENT (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL UNIQUE,
    student_id INTEGER NOT NULL,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    start_date DATE,
    completion_date DATE,
    actual_hours DECIMAL(4,1) CHECK(actual_hours > 0 AND actual_hours <= 200),
    final_payment DECIMAL(10,2) CHECK(final_payment > 0),
    FOREIGN KEY (task_id) REFERENCES TASK(task_id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id) ON DELETE CASCADE
);

-- Create PAYMENT table
CREATE TABLE PAYMENT (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL UNIQUE,
    amount DECIMAL(10,2) NOT NULL CHECK(amount > 0),
    payment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    payment_method VARCHAR(20) NOT NULL CHECK(payment_method IN ('credit_card', 'debit_card', 'paypal', 'bank_transfer', 'cash')),
    status VARCHAR(20) DEFAULT 'pending' CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
    FOREIGN KEY (assignment_id) REFERENCES TASK_ASSIGNMENT(assignment_id) ON DELETE CASCADE
);

-- Create RATING table
CREATE TABLE RATING (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL UNIQUE,
    client_rating INTEGER CHECK(client_rating >= 1 AND client_rating <= 5),
    student_rating INTEGER CHECK(student_rating >= 1 AND student_rating <= 5),
    client_feedback TEXT,
    student_feedback TEXT,
    rating_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (assignment_id) REFERENCES TASK_ASSIGNMENT(assignment_id) ON DELETE CASCADE
);

-- Create DISPUTE table
CREATE TABLE DISPUTE (
    dispute_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL UNIQUE,
    dispute_type VARCHAR(30) NOT NULL CHECK(dispute_type IN ('payment', 'quality', 'deadline', 'communication', 'other')),
    description TEXT NOT NULL,
    filed_date DATE NOT NULL DEFAULT CURRENT_DATE,
    resolution_date DATE,
    resolution_status VARCHAR(20) DEFAULT 'pending' CHECK(resolution_status IN ('pending', 'resolved', 'escalated', 'dismissed')),
    resolution_details TEXT,
    FOREIGN KEY (assignment_id) REFERENCES TASK_ASSIGNMENT(assignment_id) ON DELETE CASCADE
);

-- Create additional indexes for performance optimization
CREATE INDEX idx_student_email ON STUDENT(email);
CREATE INDEX idx_client_email ON CLIENT(email);
CREATE INDEX idx_skill_name ON SKILL(skill_name);
CREATE INDEX idx_task_status ON TASK(status);
CREATE INDEX idx_task_deadline ON TASK(deadline);
CREATE INDEX idx_application_status ON TASK_APPLICATION(status);
CREATE INDEX idx_assignment_student ON TASK_ASSIGNMENT(student_id);
CREATE INDEX idx_payment_status ON PAYMENT(status);
CREATE INDEX idx_dispute_status ON DISPUTE(resolution_status);
