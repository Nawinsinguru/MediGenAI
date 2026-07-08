@echo off
REM MediGenAI Frontend Setup Script for Windows

echo.
echo ========================================
echo   MediGenAI Frontend Setup
echo ========================================
echo.

REM Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed or not in PATH
    echo Please install Node.js 18+ from https://nodejs.org/
    pause
    exit /b 1
)

echo [OK] Node.js installed: 
node --version
echo [OK] npm installed: 
npm --version
echo.

REM Install dependencies
echo [*] Installing dependencies...
echo.
call npm install

if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Available Commands:
echo   npm run dev     - Start development server
echo   npm run build   - Build for production
echo   npm run preview - Preview production build
echo.
echo Next Steps:
echo   1. Ensure backend is running: http://localhost:8000
echo   2. Run: npm run dev
echo   3. Open: http://localhost:5173
echo.
pause
