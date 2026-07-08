<template>
  <div class="min-h-screen">
    <!-- Header Navigation -->
    <header
      class="sticky top-0 z-50 bg-white/70 backdrop-blur-md border-b border-white/20"
    >
      <nav
        class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between"
      >
        <div class="flex items-center gap-3">
          <div
            class="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-600 rounded-xl flex items-center justify-center"
          >
            <svg
              class="w-6 h-6 text-white"
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
          <h1 class="text-xl font-bold text-gray-900">MediGenAI</h1>
        </div>

        <div class="hidden md:flex items-center gap-8">
          <RouterLink
            to="/chat"
            class="text-gray-600 hover:text-gray-900 font-medium transition"
            >Chat</RouterLink
          >
          <RouterLink
            to="/upload"
            class="text-gray-600 hover:text-gray-900 font-medium transition"
            >Upload</RouterLink
          >
          <RouterLink
            to="/reports"
            class="text-gray-600 hover:text-gray-900 font-medium transition"
            >Reports</RouterLink
          >
        </div>

        <button
          @click="handleLogout"
          class="px-4 py-2 text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 transition font-medium"
        >
          Logout
        </button>
      </nav>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid md:grid-cols-2 gap-8 mb-12">
        <!-- Welcome Section -->
        <div class="md:col-span-2">
          <div class="card shadow-lg">
            <div class="flex items-start justify-between">
              <div>
                <h2 class="text-3xl font-bold text-gray-900 mb-2">
                  Welcome, {{ authStore.user?.full_name || "User" }}
                </h2>
                <p class="text-gray-600">
                  Your personal medical AI assistant is ready to help
                </p>
              </div>
              <div class="hidden sm:flex items-center gap-3">
                <div class="text-right">
                  <p class="text-sm text-gray-600">Account Status</p>
                  <p class="font-semibold text-green-600">Active</p>
                </div>
                <div
                  class="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center"
                >
                  <svg
                    class="w-6 h-6 text-green-600"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M5 13l4 4L19 7"
                    />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Actions -->
        <RouterLink
          to="/chat"
          class="card shadow-lg hover:shadow-xl transition cursor-pointer group"
        >
          <div class="flex items-start justify-between mb-4">
            <div
              class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center group-hover:bg-blue-200 transition"
            >
              <svg
                class="w-6 h-6 text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
                />
              </svg>
            </div>
            <span
              class="text-xs font-semibold text-primary-600 bg-primary-50 px-3 py-1 rounded-full"
              >NEW</span
            >
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">AI Chat</h3>
          <p class="text-gray-600 text-sm">
            Ask medical questions and get AI-powered responses
          </p>
          <div class="mt-4 flex items-center text-primary-600 font-semibold">
            Get Started
            <svg
              class="w-4 h-4 ml-2 group-hover:translate-x-1 transition"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </div>
        </RouterLink>

        <RouterLink
          to="/upload"
          class="card shadow-lg hover:shadow-xl transition cursor-pointer group"
        >
          <div class="flex items-start justify-between mb-4">
            <div
              class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center group-hover:bg-purple-200 transition"
            >
              <svg
                class="w-6 h-6 text-purple-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 4v16m8-8H4"
                />
              </svg>
            </div>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Upload PDF</h3>
          <p class="text-gray-600 text-sm">
            Upload medical documents and PDFs to your library
          </p>
          <div class="mt-4 flex items-center text-primary-600 font-semibold">
            Upload Now
            <svg
              class="w-4 h-4 ml-2 group-hover:translate-x-1 transition"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </div>
        </RouterLink>

        <RouterLink
          to="/reports"
          class="card shadow-lg hover:shadow-xl transition cursor-pointer group"
        >
          <div class="flex items-start justify-between mb-4">
            <div
              class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center group-hover:bg-green-200 transition"
            >
              <svg
                class="w-6 h-6 text-green-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                />
              </svg>
            </div>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Generate Report</h3>
          <p class="text-gray-600 text-sm">
            Create professional medical reports instantly
          </p>
          <div class="mt-4 flex items-center text-primary-600 font-semibold">
            Generate
            <svg
              class="w-4 h-4 ml-2 group-hover:translate-x-1 transition"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </div>
        </RouterLink>

        <RouterLink
          to="/chat"
          class="card shadow-lg hover:shadow-xl transition cursor-pointer group"
        >
          <div class="flex items-start justify-between mb-4">
            <div
              class="w-12 h-12 bg-orange-100 rounded-xl flex items-center justify-center group-hover:bg-orange-200 transition"
            >
              <svg
                class="w-6 h-6 text-orange-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                />
              </svg>
            </div>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Quick Analysis</h3>
          <p class="text-gray-600 text-sm">
            Fast medical insights powered by AI
          </p>
          <div class="mt-4 flex items-center text-primary-600 font-semibold">
            Analyze
            <svg
              class="w-4 h-4 ml-2 group-hover:translate-x-1 transition"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </div>
        </RouterLink>
      </div>

      <!-- Features Grid -->
      <div class="grid md:grid-cols-3 gap-6">
        <div class="card text-center">
          <div
            class="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4"
          >
            <svg
              class="w-6 h-6 text-primary-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">Secure</h3>
          <p class="text-sm text-gray-600">
            Your medical data is encrypted and secure
          </p>
        </div>

        <div class="card text-center">
          <div
            class="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4"
          >
            <svg
              class="w-6 h-6 text-primary-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 10V3L4 14h7v7l9-11h-7z"
              />
            </svg>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">Fast</h3>
          <p class="text-sm text-gray-600">
            Get instant AI-powered medical insights
          </p>
        </div>

        <div class="card text-center">
          <div
            class="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4"
          >
            <svg
              class="w-6 h-6 text-primary-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
              />
            </svg>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">Intelligent</h3>
          <p class="text-sm text-gray-600">
            Advanced AI models for medical analysis
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import { RouterLink } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();

const handleLogout = () => {
  authStore.logout();
  router.push("/login");
};
</script>
