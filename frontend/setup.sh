#!/bin/bash
# Setup script for MediGenAI Frontend

echo "🚀 Setting up MediGenAI Frontend..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 Available commands:"
echo "  npm run dev     - Start development server"
echo "  npm run build   - Build for production"
echo "  npm run preview - Preview production build"
echo ""
echo "📝 Next steps:"
echo "  1. Make sure the backend is running on http://localhost:8000"
echo "  2. Run: npm run dev"
echo "  3. Open: http://localhost:5173"
