-- Sample Data for Skill-Based Micro-Task Marketplace
-- Insert data into tables in proper order to respect foreign key constraints

-- Insert SKILLS data first
INSERT INTO SKILL (skill_name, category, description) VALUES
('JavaScript', 'Programming', 'Web development programming language'),
('Python', 'Programming', 'General purpose programming language'),
('Graphic Design', 'Design', 'Visual communication and design'),
('Content Writing', 'Writing', 'Creating written content for various purposes'),
('Data Entry', 'Administrative', 'Inputting and managing data'),
('Social Media Marketing', 'Marketing', 'Managing social media platforms'),
('Video Editing', 'Media', 'Editing and producing video content'),
('Translation', 'Language', 'Translating content between languages'),
('Excel', 'Office', 'Spreadsheet and data analysis'),
('Photography', 'Media', 'Taking and editing photos');

-- Insert STUDENTS data
INSERT INTO STUDENT (first_name, last_name, email, phone, university, major, graduation_year, registration_date, profile_status) VALUES
('John', 'Smith', 'john.smith@university.edu', '555-0101', 'Stanford University', 'Computer Science', 2025, '2024-01-15', 'active'),
('Emily', 'Johnson', 'emily.johnson@university.edu', '555-0102', 'MIT', 'Graphic Design', 2024, '2024-01-20', 'active'),
('Michael', 'Brown', 'michael.brown@university.edu', '555-0103', 'Harvard', 'English Literature', 2025, '2024-02-01', 'active'),
('Sarah', 'Davis', 'sarah.davis@university.edu', '555-0104', 'Berkeley', 'Business Administration', 2026, '2024-02-10', 'active'),
('David', 'Wilson', 'david.wilson@university.edu', '555-0105', 'UCLA', 'Computer Science', 2025, '2024-02-15', 'active'),
('Lisa', 'Anderson', 'lisa.anderson@university.edu', '555-0106', 'NYU', 'Fine Arts', 2024, '2024-03-01', 'active'),
('James', 'Taylor', 'james.taylor@university.edu', '555-0107', 'Columbia', 'Journalism', 2025, '2024-03-05', 'active'),
('Maria', 'Garcia', 'maria.garcia@university.edu', '555-0108', 'University of Texas', 'Marketing', 2026, '2024-03-10', 'active');

-- Insert CLIENTS data
INSERT INTO CLIENT (company_name, contact_person, email, phone, business_type, registration_date, verification_status) VALUES
('TechStart Inc.', 'Robert Chen', 'robert.chen@techstart.com', '555-1001', 'Technology', '2024-01-01', 'verified'),
('Creative Agency', 'Jennifer Lee', 'jennifer.lee@creativeagency.com', '555-1002', 'Design', '2024-01-05', 'verified'),
('Marketing Solutions', 'David Martinez', 'david.martinez@marketingsolutions.com', '555-1003', 'Marketing', '2024-01-10', 'verified'),
('E-commerce Store', 'Amanda White', 'amanda.white@ecommerce.com', '555-1004', 'Retail', '2024-01-15', 'pending'),
('Publishing House', 'Thomas Harris', 'thomas.harris@publishing.com', '555-1005', 'Media', '2024-01-20', 'verified'),
('Startup Hub', 'Rachel Green', 'rachel.green@startuphub.com', '555-1006', 'Technology', '2024-01-25', 'verified'),
('Local Restaurant', 'Carlos Rodriguez', 'carlos.rodriguez@restaurant.com', '555-1007', 'Food Service', '2024-02-01', 'verified'),
('Educational Platform', 'Kevin Liu', 'kevin.liu@edutech.com', '555-1008', 'Education', '2024-02-05', 'pending');

-- Insert STUDENT_SKILL relationships
INSERT INTO STUDENT_SKILL (student_id, skill_id, proficiency_level, years_experience, certification) VALUES
(1, 1, 'advanced', 3.0, 'JavaScript Certification'),
(1, 2, 'intermediate', 2.0, 'Python Basics'),
(1, 9, 'advanced', 4.0, 'Excel Expert'),
(2, 3, 'expert', 5.0, 'Adobe Certified Designer'),
(2, 10, 'intermediate', 2.5, 'Photography Course'),
(3, 4, 'advanced', 3.5, 'Content Writing Certificate'),
(3, 8, 'intermediate', 2.0, 'Spanish-English Translation'),
(4, 5, 'expert', 4.0, 'Data Entry Specialist'),
(4, 6, 'advanced', 2.5, 'Social Media Marketing'),
(5, 1, 'expert', 4.0, 'Full Stack Developer'),
(5, 2, 'advanced', 3.0, 'Python Developer'),
(6, 3, 'advanced', 4.0, 'Graphic Design Degree'),
(6, 7, 'intermediate', 1.5, 'Video Editing Basics'),
(7, 4, 'expert', 3.0, 'Journalism Degree'),
(7, 8, 'beginner', 1.0, 'Basic Translation'),
(8, 6, 'expert', 3.5, 'Marketing Degree'),
(8, 5, 'advanced', 2.0, 'Administrative Skills');

-- Insert TASKS data
INSERT INTO TASK (client_id, title, description, required_skill_id, difficulty_level, estimated_hours, budget, deadline, posting_date, status) VALUES
(1, 'JavaScript Web App Development', 'Need a simple web application for inventory management using JavaScript and HTML', 1, 'medium', 15.0, 300.00, '2024-04-15', '2024-03-01', 'open'),
(2, 'Logo Design for Startup', 'Create a modern logo for our new tech startup', 3, 'medium', 8.0, 150.00, '2024-03-20', '2024-03-02', 'open'),
(3, 'Social Media Content Creation', 'Create 10 social media posts for our product launch', 6, 'easy', 5.0, 100.00, '2024-03-15', '2024-03-03', 'in_progress'),
(4, 'Data Entry for Product Catalog', 'Enter 500 products into our e-commerce system', 5, 'easy', 10.0, 80.00, '2024-03-10', '2024-03-04', 'completed'),
(5, 'Blog Content Writing', 'Write 5 blog posts about digital marketing trends', 4, 'medium', 12.0, 200.00, '2024-03-25', '2024-03-05', 'open'),
(1, 'Python Data Analysis Script', 'Create a Python script to analyze sales data', 2, 'hard', 20.0, 400.00, '2024-04-20', '2024-03-06', 'open'),
(6, 'Video Editing for Marketing', 'Edit a 5-minute promotional video', 7, 'medium', 6.0, 120.00, '2024-03-18', '2024-03-07', 'open'),
(7, 'Translation of Technical Documents', 'Translate technical manual from English to Spanish', 8, 'hard', 15.0, 250.00, '2024-03-30', '2024-03-08', 'open'),
(8, 'Excel Dashboard Creation', 'Create sales dashboard in Excel with charts', 9, 'medium', 8.0, 160.00, '2024-03-22', '2024-03-09', 'open'),
(2, 'Product Photography', 'Take photos of 20 products for our catalog', 10, 'easy', 4.0, 90.00, '2024-03-12', '2024-03-10', 'completed');

-- Insert TASK_APPLICATIONS data
INSERT INTO TASK_APPLICATION (task_id, student_id, application_date, proposed_rate, cover_letter, status) VALUES
(1, 1, '2024-03-02', 280.00, 'I have 3 years of JavaScript experience and can deliver a high-quality web app.', 'pending'),
(1, 5, '2024-03-03', 320.00, 'Expert JavaScript developer with full-stack experience. Can deliver quickly.', 'accepted'),
(2, 2, '2024-03-03', 140.00, 'Professional graphic designer with certification and portfolio.', 'accepted'),
(3, 8, '2024-03-04', 95.00, 'Marketing student with social media experience.', 'accepted'),
(4, 4, '2024-03-05', 75.00, 'Fast and accurate data entry specialist.', 'accepted'),
(5, 3, '2024-03-06', 180.00, 'Experienced content writer with journalism background.', 'pending'),
(5, 7, '2024-03-07', 220.00, 'Professional writer with published articles.', 'pending'),
(6, 5, '2024-03-08', 380.00, 'Python expert with data analysis experience.', 'accepted'),
(7, 6, '2024-03-09', 110.00, 'Video editing student with portfolio of projects.', 'pending'),
(8, 7, '2024-03-10', 240.00, 'Bilingual journalism student with translation experience.', 'accepted'),
(9, 1, '2024-03-11', 150.00, 'Excel expert with data visualization skills.', 'accepted'),
(10, 2, '2024-03-12', 85.00, 'Photography student with equipment and experience.', 'accepted');

-- Insert TASK_ASSIGNMENTS data
INSERT INTO TASK_ASSIGNMENT (task_id, student_id, assigned_date, start_date, completion_date, actual_hours, final_payment) VALUES
(2, 2, '2024-03-05', '2024-03-06', '2024-03-14', 7.5, 140.00),
(3, 8, '2024-03-05', '2024-03-06', NULL, NULL, NULL),
(4, 4, '2024-03-06', '2024-03-07', '2024-03-09', 9.0, 75.00),
(6, 5, '2024-03-09', '2024-03-10', NULL, NULL, NULL),
(8, 7, '2024-03-11', '2024-03-12', NULL, NULL, NULL),
(9, 1, '2024-03-12', '2024-03-13', NULL, NULL, NULL),
(10, 2, '2024-03-13', '2024-03-14', '2024-03-16', 4.5, 85.00),
(1, 5, '2024-03-04', '2024-03-05', NULL, NULL, NULL);

-- Insert PAYMENTS data
INSERT INTO PAYMENT (assignment_id, amount, payment_date, payment_method, status) VALUES
(1, 140.00, '2024-03-15', 'paypal', 'completed'),
(3, 75.00, '2024-03-10', 'credit_card', 'completed'),
(7, 85.00, '2024-03-17', 'bank_transfer', 'completed');

-- Insert RATINGS data
INSERT INTO RATING (assignment_id, client_rating, student_rating, client_feedback, student_feedback, rating_date) VALUES
(1, 5, 4, 'Excellent logo design! Very professional and creative.', 'Great client, clear requirements and prompt payment.', '2024-03-16'),
(3, 4, 5, 'Fast and accurate work. Delivered on time.', 'Good communication, fair payment terms.', '2024-03-11'),
(7, 5, 5, 'Beautiful photos! Exactly what we needed.', 'Wonderful client, very cooperative.', '2024-03-18');

-- Insert DISPUTES data
INSERT INTO DISPUTE (assignment_id, dispute_type, description, filed_date, resolution_date, resolution_status, resolution_details) VALUES
(2, 'deadline', 'Student missed the initial deadline by 2 days', '2024-03-15', '2024-03-16', 'resolved', 'Extended deadline with 10% discount applied');
