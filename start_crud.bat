@echo off
echo ========================================
echo    SKILLHUB CRUD INTERFACE
echo ========================================
echo.
echo 🚀 Starting Python CRUD Server...
echo.
echo 📡 This will start a local server
echo 🌐 No external dependencies required
echo 💾 Uses built-in SQLite database
echo.
echo 📱 Server will be available at:
echo    http://localhost:8000
echo.
echo 📋 Features Available:
echo    ✅ Complete CRUD Operations
echo    ✅ Students, Clients, Skills, Tasks
echo    ✅ Search and Filter
echo    ✅ Real-time Updates
echo    ✅ Responsive Design
echo.
echo ⏹️  Press Ctrl+C to stop server
echo.
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.6+
    echo 📥 Download from: https://www.python.org/downloads/
    pause
    exit /b
)

REM Start the server
echo 🔄 Starting server...
python server.py

echo.
echo 🛑 Server stopped
pause
