# Component Reference Guide

## Page Components

### Login.vue

**Path**: `src/pages/Login.vue`

**Purpose**: User authentication entry point

**Features**:

- Email and password fields
- Form validation
- Error message display
- Link to registration
- Loading state

**Usage**:

```
Route: /login
Accessible: Before authentication
```

---

### Register.vue

**Path**: `src/pages/Register.vue`

**Purpose**: New user account creation

**Features**:

- Full name input
- Email validation
- Password creation
- Account creation logic
- Link to login

**Usage**:

```
Route: /register
Accessible: Before authentication
```

---

### Dashboard.vue

**Path**: `src/pages/Dashboard.vue`

**Purpose**: Main hub with quick access to all features

**Features**:

- Welcome message
- User profile display
- Quick action cards
- Feature overview
- Navigation links

**Components**:

- Header navigation
- Welcome card
- Action cards (Chat, Upload, Reports, Analysis)
- Feature highlights grid

---

### Chat.vue

**Path**: `src/pages/Chat.vue`

**Purpose**: Real-time medical AI conversation

**Features**:

- Message display area
- Chat history
- User/AI message differentiation
- Input field with send button
- Auto-scroll functionality
- Loading indicators
- Error handling

**Data Structure**:

```typescript
interface Message {
  type: "user" | "ai";
  content: string;
}
```

---

### Upload.vue

**Path**: `src/pages/Upload.vue`

**Purpose**: PDF document management

**Features**:

- Drag-and-drop upload zone
- File input selector
- Progress bar
- File validation (PDF only)
- Size validation (max 10MB)
- Recent uploads list
- Success/error messages

**Upload Process**:

1. User selects or drags PDF
2. File validation
3. Progress tracking
4. Upload to backend
5. Success notification

---

### Reports.vue

**Path**: `src/pages/Reports.vue`

**Purpose**: Medical report generation

**Features**:

- Patient information form
- Clinical findings textarea
- Report preview
- Copy to clipboard
- Download functionality

**Form Fields**:

- Patient Name (text)
- Age (number)
- Gender (select)
- Clinical Findings (textarea)

**Report Actions**:

- Copy to clipboard
- Download as text file
- Generate new report

## Store

### auth.ts (Pinia Store)

**Path**: `src/stores/auth.ts`

**State**:

```typescript
token: string | null;
user: any;
isLoading: boolean;
error: string | null;
```

**Getters**:

```typescript
isAuthenticated: boolean;
```

**Actions**:

- `register(name, email, password)` - Create new account
- `login(email, password)` - Authenticate user
- `logout()` - Clear session
- `getCurrentUser()` - Fetch user info

**Usage**:

```typescript
const authStore = useAuthStore();
await authStore.login(email, password);
authStore.logout();
```

## Utils

### api.ts (Axios Instance)

**Path**: `src/utils/api.ts`

**Features**:

- Axios instance with base URL
- Request interceptors (add auth token)
- Response interceptors (handle 401)
- Automatic token attachment

**Usage**:

```typescript
import api from "@/utils/api";

api.get("/endpoint");
api.post("/endpoint", data);
api.put("/endpoint", data);
api.delete("/endpoint");
```

## Router

### index.ts

**Path**: `src/router/index.ts`

**Routes**:
| Route | Component | Auth Required |
|-------|-----------|---------------|
| /login | Login.vue | No |
| /register | Register.vue | No |
| / | Dashboard.vue | Yes |
| /chat | Chat.vue | Yes |
| /upload | Upload.vue | Yes |
| /reports | Reports.vue | Yes |

**Navigation Guards**:

- Redirects to login if auth required but not authenticated
- Redirects to dashboard if trying to access login/register while authenticated

## Reusable CSS Classes

### Buttons

```html
<!-- Primary Button -->
<button class="btn-primary">Action</button>

<!-- Secondary Button -->
<button class="btn-secondary">Action</button>

<!-- Disabled State -->
<button class="btn-primary" disabled>Disabled</button>
```

### Cards

```html
<!-- Standard Card -->
<div class="card">Content</div>

<!-- Card with Shadow -->
<div class="card shadow-lg">Content</div>

<!-- Clickable Card -->
<div class="card hover:shadow-xl cursor-pointer">Content</div>
```

### Input Fields

```html
<!-- Text Input -->
<input type="text" class="input-field" />

<!-- Email Input -->
<input type="email" class="input-field" />

<!-- Textarea -->
<textarea class="input-field resize-none"></textarea>
```

### Glass Effect

```html
<div class="glass-effect">
  <!-- Content with semi-transparent blur effect -->
</div>
```

## Animation Classes

### Fade In

```html
<div class="animate-fade-in">Fades in smoothly</div>
```

### Slide Up

```html
<div class="animate-slide-up">Slides up on appear</div>
```

## Color Variables

### Text Colors

```css
text-gray-900  /* Primary text */
text-gray-600  /* Secondary text */
text-gray-500  /* Tertiary text */
```

### Background Colors

```css
bg-white       /* Cards, inputs */
bg-gray-50     /* Page background */
bg-primary-50  /* Light purple highlights */
bg-primary-500 /* Primary action */
```

### Border Colors

```css
border-gray-200     /* Standard borders */
border-primary-500  /* Active state */
border-red-200      /* Error state */
border-green-200    /* Success state */
```

## Creating New Components

### Template

```vue
<template>
  <div class="card">
    <!-- Content here -->
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const state = ref<string>("");

const handleAction = () => {
  // Action logic
};
</script>

<style scoped>
/* Component-specific styles */
</style>
```

### Register in Page

```typescript
import MyComponent from "@/components/MyComponent.vue";

export default {
  components: {
    MyComponent,
  },
};
```

## State Management Pattern

### Using Store

```typescript
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

// Access state
authStore.token;
authStore.isAuthenticated;

// Call actions
await authStore.login(email, password);

// Watch state
watchEffect(() => {
  console.log(authStore.token);
});
```

## API Request Pattern

### Making Requests

```typescript
import api from "@/utils/api";

// GET request
const response = await api.get("/endpoint");

// POST request
const response = await api.post("/endpoint", {
  key: "value",
});

// Error handling
try {
  const data = await api.post("/endpoint", payload);
} catch (error) {
  console.error(error.response?.data?.detail);
}
```

## Form Handling Pattern

### Vue Form

```vue
<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="form.field" type="text" />
    <button type="submit">Submit</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from "vue";

const form = ref({
  field: "",
});

const handleSubmit = () => {
  // Form submission logic
};
</script>
```

## Best Practices

1. **Component Organization**
   - One component per file
   - Group related components in folders
   - Use descriptive names

2. **State Management**
   - Use stores for shared state
   - Keep component state local when possible
   - Avoid prop drilling

3. **Type Safety**
   - Use TypeScript for all scripts
   - Define interfaces for data
   - Use type annotations

4. **Performance**
   - Use lazy loading for routes
   - Memoize expensive computations
   - Optimize re-renders

5. **Accessibility**
   - Use semantic HTML
   - Add ARIA labels
   - Ensure keyboard navigation
   - Maintain color contrast

## Testing Components

```typescript
// Component test example
import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import Button from "@/components/Button.vue";

describe("Button Component", () => {
  it("renders properly", () => {
    const wrapper = mount(Button);
    expect(wrapper.exists()).toBe(true);
  });
});
```

---

**Last Updated**: 2024
**Vue Version**: 3.4+
**TypeScript**: 5.3+
