// Simple Demo Mode - No Authentication Required

// Global State
let currentUser = {
    id: 1,
    name: "Demo Student",
    email: "demo@skillhub.com",
    type: "student",
    university: "Stanford University",
    major: "Computer Science"
};

let isLoggedIn = true; // Always logged in demo mode

// Sample Data
let tasks = [
    { 
        id: 1, 
        title: "JavaScript Web App Development", 
        description: "Build a responsive web application using JavaScript and modern frameworks", 
        budget: 300, 
        skill: "JavaScript", 
        difficulty: "Intermediate", 
        deadline: "2024-04-15", 
        hours: 20, 
        postedBy: "TechStart Inc.", 
        postedDate: "2024-03-01", 
        status: "open",
        applications: 2
    },
    { 
        id: 2, 
        title: "Logo Design for Startup", 
        description: "Create a modern logo design for a new tech startup", 
        budget: 150, 
        skill: "Graphic Design", 
        difficulty: "Beginner", 
        deadline: "2024-03-20", 
        hours: 8, 
        postedBy: "Creative Agency", 
        postedDate: "2024-03-02", 
        status: "completed",
        applications: 5
    },
    { 
        id: 3, 
        title: "Python Data Analysis", 
        description: "Analyze dataset using Python and create visualizations", 
        budget: 250, 
        skill: "Python", 
        difficulty: "Advanced", 
        deadline: "2024-04-10", 
        hours: 15, 
        postedBy: "DataCorp", 
        postedDate: "2024-03-03", 
        status: "in_progress",
        applications: 3
    },
    { 
        id: 4, 
        title: "Content Writing Campaign", 
        description: "Write 10 blog posts for digital marketing campaign", 
        budget: 180, 
        skill: "Content Writing", 
        difficulty: "Beginner", 
        deadline: "2024-03-25", 
        hours: 12, 
        postedBy: "Marketing Pro", 
        postedDate: "2024-03-04", 
        status: "open",
        applications: 1
    },
    { 
        id: 5, 
        title: "Data Entry Project", 
        description: "Enter 500 product entries into database system", 
        budget: 100, 
        skill: "Data Entry", 
        difficulty: "Beginner", 
        deadline: "2024-03-18", 
        hours: 10, 
        postedBy: "Content Hub", 
        postedDate: "2024-03-05", 
        status: "open",
        applications: 4
    },
    { 
        id: 6, 
        title: "Social Media Management", 
        description: "Manage Instagram and Twitter accounts for 1 month", 
        budget: 350, 
        skill: "Social Media Marketing", 
        difficulty: "Intermediate", 
        deadline: "2024-04-20", 
        hours: 25, 
        postedBy: "Social Media Experts", 
        postedDate: "2024-03-06", 
        status: "open",
        applications: 2
    },
    { 
        id: 7, 
        title: "Video Editing Project", 
        description: "Edit 5 promotional videos for YouTube", 
        budget: 280, 
        skill: "Video Editing", 
        difficulty: "Advanced", 
        deadline: "2024-04-12", 
        hours: 18, 
        postedBy: "Video Productions", 
        postedDate: "2024-03-07", 
        status: "in_progress",
        applications: 3
    },
    { 
        id: 8, 
        title: "Document Translation", 
        description: "Translate technical documents from English to Spanish", 
        budget: 200, 
        skill: "Translation", 
        deadline: "2024-03-22", 
        hours: 14, 
        postedBy: "Translation Services", 
        postedDate: "2024-03-08", 
        status: "completed",
        applications: 6
    },
    { 
        id: 9, 
        title: "C++ Game Engine Development", 
        description: "Develop a basic 2D game engine using C++ with physics and rendering", 
        budget: 450, 
        skill: "C++", 
        difficulty: "Advanced", 
        deadline: "2024-05-01", 
        hours: 30, 
        postedBy: "Game Studio Pro", 
        postedDate: "2024-03-09", 
        status: "open",
        applications: 1
    },
    { 
        id: 10, 
        title: "Unreal Engine VR Experience", 
        description: "Create an immersive VR experience using Unreal Engine for training simulation", 
        budget: 600, 
        skill: "Unreal Engine", 
        difficulty: "Advanced", 
        deadline: "2024-05-15", 
        hours: 40, 
        postedBy: "VR Training Co", 
        postedDate: "2024-03-10", 
        status: "open",
        applications: 0
    }
];

let skills = [
    { name: "JavaScript", category: "Programming", students: 15, demand: "High" },
    { name: "Python", category: "Programming", students: 12, demand: "High" },
    { name: "C++", category: "Programming", students: 8, demand: "Medium" },
    { name: "Unreal Engine", category: "Game Development", students: 6, demand: "High" },
    { name: "Graphic Design", category: "Design", students: 8, demand: "Medium" },
    { name: "Content Writing", category: "Writing", students: 10, demand: "High" },
    { name: "Data Entry", category: "Administrative", students: 6, demand: "Low" },
    { name: "Social Media Marketing", category: "Marketing", students: 7, demand: "Medium" },
    { name: "Video Editing", category: "Media", students: 5, demand: "Medium" },
    { name: "Translation", category: "Language", students: 4, demand: "Low" },
    { name: "Excel", category: "Office", students: 9, demand: "Medium" },
    { name: "Photography", category: "Media", students: 3, demand: "Low" }
];

let userProfile = {
    skills: ["JavaScript", "Python", "React", "Node.js"],
    applications: [
        { id: 1, taskTitle: "JavaScript Web App", status: "pending", appliedDate: "2024-03-10" },
        { id: 2, taskTitle: "Python Data Analysis", status: "accepted", appliedDate: "2024-03-08" }
    ],
    reviews: [
        { id: 1, taskTitle: "Logo Design", rating: 5, comment: "Excellent work!", date: "2024-03-01" },
        { id: 2, taskTitle: "Content Writing", rating: 4, comment: "Great quality", date: "2024-02-28" }
    ],
    stats: {
        completed: 12,
        rating: 4.8,
        earned: 750
    }
};

// Notification System
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 2000;
        animation: slideInRight 0.3s ease-out;
    `;
    
    switch(type) {
        case 'success':
            notification.style.backgroundColor = '#27ae60';
            break;
        case 'error':
            notification.style.backgroundColor = '#e74c3c';
            break;
        case 'warning':
            notification.style.backgroundColor = '#f39c12';
            break;
        default:
            notification.style.backgroundColor = '#3498db';
    }
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Navigation
function showSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('active');
    });
    
    // Show target section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
    }
    
    // Update nav links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
        }
    });
    
    // Load section-specific content
    switch(sectionId) {
        case 'home':
            loadHomePage();
            break;
        case 'tasks':
            loadTasksPage();
            break;
        case 'post-task':
            // Post task page loads automatically
            break;
        case 'profile':
            loadProfilePage();
            break;
        case 'payment':
            // Payment page loads automatically
            break;
    }
}

// Load Home Page
function loadHomePage() {
    // Load featured tasks
    const featuredTasksGrid = document.getElementById('featured-tasks-grid');
    if (featuredTasksGrid) {
        const featuredTasks = tasks.filter(t => t.status === 'open').slice(0, 3);
        featuredTasksGrid.innerHTML = featuredTasks.map(task => `
            <div class="task-card">
                <div class="task-header">
                    <h3>${task.title}</h3>
                    <span class="task-skill">${task.skill}</span>
                </div>
                <div class="task-body">
                    <p>${task.description}</p>
                    <div class="task-meta">
                        <span class="task-budget">$${task.budget}</span>
                        <span class="task-difficulty">${task.difficulty}</span>
                        <span class="task-hours">${task.hours}h</span>
                    </div>
                </div>
                <div class="task-footer">
                    <button class="btn btn-primary" onclick="applyForTask(${task.id})">Apply Now</button>
                </div>
            </div>
        `).join('');
    }
    
    // Load popular skills
    const popularSkillsShowcase = document.getElementById('popular-skills-showcase');
    if (popularSkillsShowcase) {
        const popularSkills = skills.filter(s => s.demand === 'High').slice(0, 6);
        popularSkillsShowcase.innerHTML = popularSkills.map(skill => `
            <div class="skill-card">
                <div class="skill-icon">🎯</div>
                <div class="skill-info">
                    <h4>${skill.name}</h4>
                    <p>${skill.category}</p>
                    <span class="skill-demand">${skill.demand} Demand</span>
                </div>
            </div>
        `).join('');
    }
    
    // Update statistics
    document.getElementById('total-tasks').textContent = tasks.filter(t => t.status === 'open').length;
    document.getElementById('total-students').textContent = skills.reduce((sum, skill) => sum + skill.students, 0);
    document.getElementById('total-clients').textContent = 8; // Mock data
}

// Load Tasks Page
function loadTasksPage() {
    loadTasksFilters();
    renderTasks();
}

function loadTasksFilters() {
    const skillFilter = document.getElementById('skill-filter');
    if (skillFilter) {
        const skillOptions = skills.map(skill => `<option value="${skill.name}">${skill.name}</option>`).join('');
        skillFilter.innerHTML = '<option value="">All Skills</option>' + skillOptions;
    }
}

function renderTasks(filteredTasks = null) {
    const tasksToRender = filteredTasks || tasks.filter(t => t.status === 'open');
    const container = document.getElementById('tasks-grid');
    
    if (!container) return;
    
    if (tasksToRender.length === 0) {
        container.innerHTML = '<div class="no-tasks">No tasks found. Try adjusting your filters.</div>';
        return;
    }
    
    container.innerHTML = tasksToRender.map(task => `
        <div class="task-card">
            <div class="task-header">
                <h3>${task.title}</h3>
                <span class="task-skill">${task.skill}</span>
            </div>
            <div class="task-body">
                <p>${task.description}</p>
                <div class="task-meta">
                    <span class="task-budget">$${task.budget}</span>
                    <span class="task-difficulty">${task.difficulty}</span>
                    <span class="task-hours">${task.hours}h</span>
                </div>
            </div>
            <div class="task-footer">
                <button class="btn btn-primary" onclick="applyForTask(${task.id})">Apply Now</button>
            </div>
        </div>
    `).join('');
}

function filterTasks() {
    const searchTerm = document.getElementById('search-tasks').value.toLowerCase();
    const skillFilter = document.getElementById('skill-filter').value;
    const difficultyFilter = document.getElementById('difficulty-filter').value;
    const budgetFilter = document.getElementById('budget-filter').value;
    
    let filteredTasks = tasks.filter(t => t.status === 'open');
    
    if (searchTerm) {
        filteredTasks = filteredTasks.filter(t => 
            t.title.toLowerCase().includes(searchTerm) ||
            t.description.toLowerCase().includes(searchTerm) ||
            t.skill.toLowerCase().includes(searchTerm)
        );
    }
    
    if (skillFilter) {
        filteredTasks = filteredTasks.filter(t => t.skill === skillFilter);
    }
    
    if (difficultyFilter) {
        filteredTasks = filteredTasks.filter(t => t.difficulty === difficultyFilter);
    }
    
    if (budgetFilter) {
        filteredTasks = filteredTasks.filter(t => {
            switch(budgetFilter) {
                case '0-100': return t.budget <= 100;
                case '100-300': return t.budget > 100 && t.budget <= 300;
                case '300-500': return t.budget > 300 && t.budget <= 500;
                case '500+': return t.budget > 500;
                default: return true;
            }
        });
    }
    
    renderTasks(filteredTasks);
}

// Load Profile Page
function loadProfilePage() {
    loadProfileSkills();
    loadProfileApplications();
    loadProfileReviews();
    updateProfileStats();
    
    // Update profile display with current user data
    const profileSidebar = document.querySelector('.profile-sidebar');
    if (profileSidebar) {
        profileSidebar.innerHTML = `
            <div class="profile-avatar">
                <div class="avatar-placeholder">👤</div>
                <h3>${currentUser.name}</h3>
                <p>${currentUser.university} - ${currentUser.major}</p>
                <div class="profile-stats">
                    <div class="profile-stat">
                        <span>${userProfile.stats.completed}</span>
                        <span>Tasks Completed</span>
                    </div>
                    <div class="profile-stat">
                        <span>${userProfile.stats.rating}</span>
                        <span>Avg Rating</span>
                    </div>
                    <div class="profile-stat">
                        <span>$${userProfile.stats.earned}</span>
                        <span>Total Earned</span>
                    </div>
                </div>
            </div>
        `;
    }
}

function updateProfileStats() {
    const statElements = document.querySelectorAll('.profile-stat span:first-child');
    if (statElements.length >= 3) {
        statElements[0].textContent = userProfile.stats.completed;
        statElements[1].textContent = userProfile.stats.rating;
        statElements[2].textContent = `$${userProfile.stats.earned}`;
    }
}

function loadProfileSkills() {
    const container = document.getElementById('profile-skills');
    if (container) {
        container.innerHTML = userProfile.skills.map(skill => `
            <div class="skill-tag">
                ${skill}
                <button class="skill-remove" onclick="removeSkill('${skill}')">×</button>
            </div>
        `).join('');
    }
}

function loadProfileApplications() {
    const container = document.getElementById('my-applications');
    if (container) {
        container.innerHTML = userProfile.applications.map(app => `
            <div class="application-item">
                <h4>${app.taskTitle}</h4>
                <div class="application-meta">
                    <span class="status ${app.status}">${app.status}</span>
                    <span class="date">Applied: ${app.appliedDate}</span>
                </div>
            </div>
        `).join('');
    }
}

function loadProfileReviews() {
    const container = document.getElementById('my-reviews');
    if (container) {
        container.innerHTML = userProfile.reviews.map(review => `
            <div class="review-item">
                <h4>${review.taskTitle}</h4>
                <div class="rating">
                    ${'⭐'.repeat(review.rating)}
                </div>
                <p>${review.comment}</p>
                <span class="date">${review.date}</span>
            </div>
        `).join('');
    }
}

function addSkill() {
    const skillInput = document.getElementById('new-skill');
    const skillName = skillInput.value.trim();
    
    if (skillName && !userProfile.skills.includes(skillName)) {
        userProfile.skills.push(skillName);
        loadProfileSkills();
        skillInput.value = '';
        showNotification('Skill added successfully!', 'success');
    }
}

function removeSkill(skillName) {
    userProfile.skills = userProfile.skills.filter(s => s !== skillName);
    loadProfileSkills();
    showNotification('Skill removed', 'info');
}

// Task Functions
function applyForTask(taskId) {
    const task = tasks.find(t => t.id === taskId);
    if (task) {
        showNotification(`Applied for "${task.title}"!`, 'success');
        task.applications++;
        
        // Add to user's applications
        userProfile.applications.unshift({
            id: userProfile.applications.length + 1,
            taskTitle: task.title,
            status: 'pending',
            appliedDate: new Date().toISOString().split('T')[0]
        });
        
        if (document.getElementById('profile').classList.contains('active')) {
            loadProfileApplications();
        }
    }
}

function postTask() {
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-description').value;
    const budget = document.getElementById('task-budget').value;
    const skill = document.getElementById('task-skill').value;
    const deadline = document.getElementById('task-deadline').value;
    const difficulty = document.getElementById('task-difficulty').value;
    
    if (title && description && budget && skill && deadline) {
        const newTask = {
            id: tasks.length + 1,
            title,
            description,
            budget: parseInt(budget),
            skill,
            deadline,
            difficulty,
            hours: 20, // Default
            postedBy: currentUser.name,
            postedDate: new Date().toISOString().split('T')[0],
            status: 'open',
            applications: 0
        };
        
        tasks.unshift(newTask);
        showNotification('Task posted successfully!', 'success');
        
        // Clear form
        document.getElementById('post-task-form').reset();
        
        // Go to tasks page to see the new task
        showSection('tasks');
    } else {
        showNotification('Please fill all required fields', 'warning');
    }
}

function showPaymentSummary(taskId) {
    const task = tasks.find(t => t.id === taskId);
    if (!task) return;
    
    const serviceFee = task.budget * 0.05; // 5% service fee
    const total = task.budget + serviceFee;
    
    document.getElementById('payment-task-title').textContent = task.title;
    document.getElementById('payment-amount').textContent = `$${task.budget.toFixed(2)}`;
    document.getElementById('payment-fee').textContent = `$${serviceFee.toFixed(2)} (5%)`;
    document.getElementById('payment-total').textContent = `$${total.toFixed(2)}`;
    
    showSection('payment');
}

function processPayment(paymentData) {
    showNotification('Processing payment...', 'info');
    
    setTimeout(() => {
        showNotification('Payment successful! Task assigned.', 'success');
        showSection('tasks');
    }, 2000);
}

function cancelPayment() {
    showSection('tasks');
}

// Initialize App
document.addEventListener('DOMContentLoaded', function() {
    // Load initial page
    loadHomePage();
    
    // Set up navigation
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            showSection(targetId);
        });
    });
    
    // Set up form handlers
    const postTaskForm = document.getElementById('post-task-form');
    if (postTaskForm) {
        postTaskForm.addEventListener('submit', function(e) {
            e.preventDefault();
            postTask();
        });
    }
    
    const paymentForm = document.getElementById('payment-form');
    if (paymentForm) {
        paymentForm.addEventListener('submit', function(e) {
            e.preventDefault();
            processPayment();
        });
    }
    
    // Set up filter handlers
    const filterInputs = ['search-tasks', 'skill-filter', 'difficulty-filter', 'budget-filter'];
    filterInputs.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.addEventListener('change', filterTasks);
            element.addEventListener('input', filterTasks);
        }
    });
    
    // Payment method change
    const paymentMethod = document.getElementById('payment-method');
    if (paymentMethod) {
        paymentMethod.addEventListener('change', function() {
            const creditCardFields = document.getElementById('credit-card-fields');
            const paypalFields = document.getElementById('paypal-fields');
            
            if (this.value === 'paypal') {
                creditCardFields.style.display = 'none';
                paypalFields.style.display = 'block';
            } else {
                creditCardFields.style.display = 'block';
                paypalFields.style.display = 'none';
            }
        });
    }
});

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
