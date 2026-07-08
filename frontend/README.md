# MediGenAI Frontend

A modern Vue 3 + TypeScript frontend for the MediGenAI medical AI assistant application.

## Features

- 🔐 **Authentication** - Secure login and registration system
- 💬 **AI Chat** - Medical Q&A with AI-powered responses
- 📄 **PDF Upload** - Upload and manage medical documents
- 📋 **Report Generation** - Generate professional medical reports
- 🎨 **Modern UI** - Clean, responsive design inspired by contemporary health apps
- ⚡ **Fast Performance** - Built with Vite for optimal development and build times

## Tech Stack

- **Framework**: Vue 3 with TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **State Management**: Pinia
- **HTTP Client**: Axios
- **Router**: Vue Router

## Prerequisites

- Node.js 18+ and npm

## Installation

```bash
# Install dependencies
npm install
```

## Development

```bash
# Start development server (runs on http://localhost:5173)
npm run dev
```

## Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
src/
├── components/          # Reusable Vue components
├── pages/              # Page components (views)
│   ├── Login.vue
│   ├── Register.vue
│   ├── Dashboard.vue
│   ├── Chat.vue
│   ├── Upload.vue
│   └── Reports.vue
├── router/             # Vue Router configuration
├── stores/             # Pinia state management
├── utils/              # Utility functions and API client
├── App.vue             # Root component
├── main.ts             # Application entry point
└── style.css           # Global styles with Tailwind
```

## Features Overview

### Authentication

- User registration with email and password
- Secure login system
- JWT-based token authentication
- Protected routes

### Dashboard

- Welcome screen with quick access to all features
- Feature overview cards
- User profile information

### Chat

- Real-time chat interface with AI
- Message history
- Automatic scrolling to latest messages
- Error handling

### PDF Upload

- Drag-and-drop file upload
- File size validation
- Upload progress tracking
- Recent uploads list

### Report Generation

- Patient information form
- Clinical findings input
- AI-generated medical reports
- Copy and download reports

## API Integration

The frontend connects to the backend API at `http://localhost:8000`:

- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user info
- `POST /chat` - Send chat message
- `POST /upload/pdf` - Upload PDF file
- `POST /reports/generate` - Generate medical report

## Styling

The application uses Tailwind CSS with custom color schemes:

- **Primary Colors**: Purple/Violet gradients
- **Cream Colors**: Warm, soft backgrounds
- **Modern Effects**: Glass morphism, smooth animations

## Deployment

Build the application and deploy the `dist` folder to any static hosting service:

```bash
npm run build
# Deploy dist/ folder to your hosting provider
```

## Environment Configuration

The API base URL can be configured in `src/utils/api.ts`:

```typescript
const API_BASE_URL = "http://localhost:8000";
```

Update this for production deployments.

## License

MIT
