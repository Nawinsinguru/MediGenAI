#!/usr/bin/env node

/**
 * MediGenAI Quick Start Script
 * Helps set up and run both backend and frontend
 */

const { spawn } = require('child_process');
const path = require('path');
const os = require('os');

const isWindows = os.platform() === 'win32';

const commands = {
  checkNode: () => spawn(process.execPath, ['-v']),
  installFrontend: () => spawn(isWindows ? 'npm.cmd' : 'npm', ['install'], {
    cwd: path.join(__dirname),
    stdio: 'inherit'
  }),
  runFrontend: () => spawn(isWindows ? 'npm.cmd' : 'npm', ['run', 'dev'], {
    cwd: path.join(__dirname),
    stdio: 'inherit'
  })
};

console.log(`
╔════════════════════════════════════════╗
║     MediGenAI - Quick Start Helper    ║
╚════════════════════════════════════════╝

📋 Setup Instructions:

1. BACKEND SETUP (First Terminal)
   • Navigate to: cd backend
   • Create venv: python -m venv venv
   • Activate:
     - Windows: .\\venv\\Scripts\\Activate.ps1
     - Mac/Linux: source venv/bin/activate
   • Install: pip install -r requirements.txt
   • Run: uvicorn app.main:app --reload

2. FRONTEND SETUP (Second Terminal)
   • Navigate to: cd frontend
   • Run this command: npm run setup
   • Then run: npm run dev

3. ACCESS THE APP
   • Frontend: http://localhost:5173
   • Backend API: http://localhost:8000
   • API Docs: http://localhost:8000/docs

✨ Features Available:
   ✓ User Authentication (Login/Register)
   ✓ AI Medical Chat
   ✓ PDF Document Upload
   ✓ Medical Report Generation

📚 Documentation:
   • Setup Guide: ../SETUP_GUIDE.md
   • Design System: ./DESIGN_SYSTEM.md
   • README: ./README.md

💡 Tips:
   • Keep both terminal windows open
   • Backend must run on port 8000
   • Frontend will run on port 5173
   • Press Ctrl+C to stop either service

Happy coding! 🚀
`);
