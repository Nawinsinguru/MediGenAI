<template>
  <div class="min-h-screen flex items-center justify-center px-4 py-12">
    <div class="w-full max-w-md">
      <!-- Header -->
      <div class="text-center mb-8">
        <div class="flex items-center justify-center gap-2 mb-4">
          <div
            class="w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-600 rounded-2xl flex items-center justify-center"
          >
            <svg
              class="w-7 h-7 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 6v6m0 0v6m0-6h6m0 0h-6"
              />
            </svg>
          </div>
        </div>
        <h1 class="text-3xl font-bold text-gray-900">MediGenAI</h1>
        <p class="text-gray-600 mt-2">Create your account</p>
      </div>

      <!-- Register Form Card -->
      <div class="card shadow-lg">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Get Started</h2>

        <form @submit.prevent="handleRegister" class="space-y-4">
          <!-- Full Name Input -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2"
              >Full Name</label
            >
            <input
              v-model="fullName"
              type="text"
              class="input-field"
              placeholder="Enter your full name"
              required
            />
          </div>

          <!-- Email Input -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2"
              >Email</label
            >
            <input
              v-model="email"
              type="email"
              class="input-field"
              placeholder="Enter your email"
              required
            />
          </div>

          <!-- Password Input -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2"
              >Password</label
            >
            <input
              v-model="password"
              type="password"
              class="input-field"
              placeholder="Create a password"
              required
            />
          </div>

          <!-- Error Message -->
          <div
            v-if="error"
            class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm"
          >
            {{ error }}
          </div>

          <!-- Register Button -->
          <button
            type="submit"
            :disabled="isLoading"
            class="btn-primary w-full flex items-center justify-center gap-2"
          >
            <span v-if="!isLoading">Create Account</span>
            <span v-else>Creating...</span>
          </button>
        </form>

        <!-- Divider -->
        <div class="relative my-6">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-200"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-2 bg-white text-gray-500"
              >Already have an account?</span
            >
          </div>
        </div>

        <!-- Login Link -->
        <RouterLink to="/login" class="btn-secondary w-full text-center">
          Sign In
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import { RouterLink } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();

const fullName = ref("");
const email = ref("");
const password = ref("");
const isLoading = ref(false);
const error = ref<string | null>(null);

const handleRegister = async () => {
  isLoading.value = true;
  error.value = null;

  try {
    await authStore.register(fullName.value, email.value, password.value);
    await authStore.login(email.value, password.value);
    router.push("/");
  } catch (err: any) {
    error.value = authStore.error || "Registration failed. Please try again.";
  } finally {
    isLoading.value = false;
  }
};
</script>
