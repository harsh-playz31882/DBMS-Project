-- SQL Operations Demonstration

-- 1. SELECT QUERIES

SELECT * FROM STUDENT;
SELECT * FROM CLIENT;
SELECT * FROM SKILL;
SELECT * FROM TASK;


SELECT first_name, last_name, email, university 
FROM STUDENT 
WHERE university = 'Stanford University';

SELECT title, budget, deadline, status 
FROM TASK 
WHERE status = 'open' AND budget > 200;

-- SELECT with ORDER BY
SELECT first_name, last_name, graduation_year 
FROM STUDENT
ORDER BY graduation_year ASC, last_name ASC;

SELECT title, budget, posting_date 
FROM TASK 
ORDER BY budget DESC;


-- 2. AGGREGATE FUNCTIONS


-- COUNT operations
SELECT COUNT(*) AS total_students FROM STUDENT;
SELECT COUNT(*) AS total_tasks FROM TASK;
SELECT COUNT(*) AS open_tasks FROM TASK WHERE status = 'open';
SELECT university, COUNT(*) AS student_count 
FROM STUDENT 
GROUP BY university;

-- SUM operations
SELECT SUM(budget) AS total_budget FROM TASK;
SELECT SUM(final_payment) AS total_payments FROM TASK_ASSIGNMENT WHERE final_payment IS NOT NULL;
SELECT client_id, SUM(budget) AS total_spent 
FROM TASK 
GROUP BY client_id;

-- AVG operations
SELECT AVG(budget) AS average_task_budget FROM TASK;
SELECT AVG(graduation_year) AS avg_graduation_year FROM STUDENT;
SELECT AVG(client_rating) AS avg_client_rating 
FROM RATING 
WHERE client_rating IS NOT NULL;

-- MAX/MIN operations
SELECT MAX(budget) AS highest_budget, MIN(budget) AS lowest_budget FROM TASK;
SELECT MAX(graduation_year) AS latest_graduation FROM STUDENT;



-- 3. GROUP BY and HAVING A 
SELECT university, major, COUNT(*) AS student_count 
FROM STUDENT 
GROUP BY university, major 
ORDER BY student_count DESC;

SELECT university, COUNT(*) AS student_count 
FROM STUDENT 
GROUP BY university 
HAVING COUNT(*) > 1;

SELECT skill_id, proficiency_level, COUNT(*) AS student_count 
FROM STUDENT_SKILL 
GROUP BY skill_id, proficiency_level 
HAVING COUNT(*) >= 2;


-- INNER JOIN
SELECT s.first_name, s.last_name, ss.skill_id, sk.skill_name, ss.proficiency_level
FROM STUDENT s
INNER JOIN STUDENT_SKILL ss ON s.student_id = ss.student_id
INNER JOIN SKILL sk ON ss.skill_id = sk.skill_id;

-- LEFT JOIN
SELECT s.first_name, s.last_name, t.title, t.status
FROM STUDENT s
LEFT JOIN TASK_APPLICATION ta ON s.student_id = ta.student_id
LEFT JOIN TASK t ON ta.task_id = t.task_id
WHERE s.student_id = 1;


-- Subqueries
-- Subquery in WHERE clause
SELECT first_name, last_name, email
FROM STUDENT
WHERE student_id IN (
    SELECT student_id 
    FROM TASK_APPLICATION 
    WHERE status = 'accepted'
);

-- Subquery in FROM clause
SELECT * FROM (
    SELECT 
        s.student_id,
        s.first_name,
        s.last_name,
        COUNT(ta.application_id) as app_count
    FROM STUDENT s
    LEFT JOIN TASK_APPLICATION ta ON s.student_id = ta.student_id
    GROUP BY s.student_id, s.first_name, s.last_name
) AS student_stats
WHERE app_count > 1;



-- 6. NESTED QUERIES
-- Find students with above average ratings
SELECT DISTINCT s.first_name, s.last_name, s.email
FROM STUDENT s
INNER JOIN TASK_ASSIGNMENT ta ON s.student_id = ta.student_id
INNER JOIN RATING r ON ta.assignment_id = r.assignment_id
WHERE r.client_rating > (
    SELECT AVG(client_rating) 
    FROM RATING 
    WHERE client_rating IS NOT NULL
);

-- Find clients who posted high-budget tasks
SELECT client_id, company_name, contact_person
FROM CLIENT
WHERE client_id IN (
    SELECT client_id 
    FROM TASK 
    WHERE budget > (
        SELECT AVG(budget) * 1.5 
        FROM TASK
    )
);

-- Complex nested query for top performers
SELECT 
    s.first_name,
    s.last_name,
    COUNT(DISTINCT ta.assignment_id) as completed_tasks,
    AVG(r.client_rating) as avg_rating,
    SUM(p.amount) as total_earnings
FROM STUDENT s
INNER JOIN TASK_ASSIGNMENT ta ON s.student_id = ta.student_id
INNER JOIN PAYMENT p ON ta.assignment_id = p.assignment_id
INNER JOIN RATING r ON ta.assignment_id = r.assignment_id
WHERE s.student_id IN (
    SELECT student_id 
    FROM TASK_ASSIGNMENT 
    WHERE completion_date IS NOT NULL
    GROUP BY student_id 
    HAVING COUNT(*) >= 2
)
GROUP BY s.student_id, s.first_name, s.last_name
ORDER BY total_earnings DESC;

-- ========================================
-- 7. INSERT, UPDATE, DELETE OPERATIONS
-- ========================================

-- INSERT operations
INSERT INTO SKILL (skill_name, category, description) 
VALUES ('React', 'Programming', 'JavaScript library for building user interfaces');

INSERT INTO STUDENT (first_name, last_name, email, phone, university, major, graduation_year, registration_date, profile_status)
VALUES ('Alice', 'Johnson', 'alice.johnson@university.edu', '555-0109', 'Stanford University', 'Computer Science', 2025, '2024-03-20', 'active');

-- UPDATE operations
UPDATE STUDENT 
SET phone = '555-9999', profile_status = 'active' 
WHERE student_id = 8;

UPDATE TASK 
SET status = 'in_progress' 
WHERE task_id = 5 AND deadline > CURRENT_DATE;

UPDATE TASK_ASSIGNMENT 
SET completion_date = CURRENT_DATE, actual_hours = 12.5 
WHERE assignment_id = 2;

-- DELETE operations
DELETE FROM TASK_APPLICATION 
WHERE application_date < '2024-01-01' AND status = 'pending';

DELETE FROM DISPUTE 
WHERE resolution_status = 'dismissed' AND resolution_date < '2024-01-01';

-- ========================================
-- 8. ADVANCED QUERIES
-- ========================================

-- Window functions (if supported by SQLite version)
SELECT 
    student_id,
    first_name,
    last_name,
    graduation_year,
    RANK() OVER (ORDER BY graduation_year DESC) as graduation_rank
FROM STUDENT;

-- CASE statements
SELECT 
    title,
    budget,
    CASE 
        WHEN budget < 100 THEN 'Low Budget'
        WHEN budget BETWEEN 100 AND 300 THEN 'Medium Budget'
        WHEN budget > 300 THEN 'High Budget'
    END as budget_category,
    CASE 
        WHEN deadline < CURRENT_DATE THEN 'Overdue'
        WHEN deadline = CURRENT_DATE THEN 'Due Today'
        WHEN deadline > CURRENT_DATE THEN 'Upcoming'
    END as deadline_status
FROM TASK;

-- UNION operations
SELECT first_name, last_name, email, 'Student' as user_type
FROM STUDENT
UNION
SELECT contact_person as first_name, '' as last_name, email, 'Client' as user_type
FROM CLIENT;

-- ========================================
-- 9. ANALYTICAL QUERIES
-- ========================================

-- Skill demand analysis
SELECT 
    sk.skill_name,
    sk.category,
    COUNT(t.task_id) as task_count,
    AVG(t.budget) as avg_budget,
    MAX(t.budget) as max_budget
FROM SKILL sk
LEFT JOIN TASK t ON sk.skill_id = t.required_skill_id
GROUP BY sk.skill_id, sk.skill_name, sk.category
ORDER BY task_count DESC, avg_budget DESC;

-- Student performance metrics
SELECT 
    s.first_name,
    s.last_name,
    s.university,
    COUNT(DISTINCT ta.assignment_id) as total_assignments,
    SUM(p.amount) as total_earnings,
    AVG(r.client_rating) as avg_rating,
    COUNT(DISTINCT ss.skill_id) as skill_count
FROM STUDENT s
LEFT JOIN TASK_ASSIGNMENT ta ON s.student_id = ta.student_id
LEFT JOIN PAYMENT p ON ta.assignment_id = p.assignment_id
LEFT JOIN RATING r ON ta.assignment_id = r.assignment_id
LEFT JOIN STUDENT_SKILL ss ON s.student_id = ss.student_id
GROUP BY s.student_id, s.first_name, s.last_name, s.university
ORDER BY total_earnings DESC;

-- Monthly task trends
SELECT 
    strftime('%Y-%m', posting_date) as month,
    COUNT(*) as tasks_posted,
    SUM(budget) as total_budget,
    AVG(budget) as avg_budget
FROM TASK
GROUP BY strftime('%Y-%m', posting_date)
ORDER BY month;

-- Client activity analysis
SELECT 
    c.company_name,
    c.business_type,
    COUNT(t.task_id) as total_tasks,
    SUM(t.budget) as total_spent,
    AVG(t.budget) as avg_task_budget,
    COUNT(DISTINCT CASE WHEN t.status = 'completed' THEN t.task_id END) as completed_tasks
FROM CLIENT c
LEFT JOIN TASK t ON c.client_id = t.client_id
GROUP BY c.client_id, c.company_name, c.business_type
ORDER BY total_spent DESC;
