<template>
  <div class="min-h-screen">
    <!-- Header Navigation -->
    <header
      class="sticky top-0 z-50 bg-white/70 backdrop-blur-md border-b border-white/20"
    >
      <nav
        class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between"
      >
        <RouterLink to="/" class="flex items-center gap-3">
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
        </RouterLink>

        <button
          @click="handleLogout"
          class="px-4 py-2 text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 transition font-medium"
        >
          Logout
        </button>
      </nav>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="mb-8">
        <h2 class="text-3xl font-bold text-gray-900">Medical Chat Assistant</h2>
        <p class="text-gray-600 mt-2">
          Ask any medical question and get instant AI-powered responses
        </p>
      </div>

      <!-- Chat Container -->
      <div class="card shadow-lg flex flex-col h-[600px]">
        <!-- Messages Area -->
        <div
          ref="messagesContainer"
          class="flex-1 overflow-y-auto space-y-4 p-6 bg-gradient-to-b from-transparent to-gray-50/50"
        >
          <div
            v-if="messages.length === 0"
            class="flex items-center justify-center h-full"
          >
            <div class="text-center">
              <div
                class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4"
              >
                <svg
                  class="w-8 h-8 text-primary-600"
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
              <h3 class="text-lg font-semibold text-gray-900 mb-2">
                Start a Conversation
              </h3>
              <p class="text-gray-600 text-sm max-w-xs">
                Ask me anything about medical topics and I'll provide helpful
                information
              </p>
            </div>
          </div>

          <div
            v-for="(msg, idx) in messages"
            :key="idx"
            class="animate-slide-up"
          >
            <!-- User Message -->
            <div v-if="msg.type === 'user'" class="flex justify-end">
              <div
                class="max-w-xs bg-gradient-to-br from-primary-500 to-primary-600 text-white rounded-2xl rounded-tr-none px-4 py-3 shadow-md"
              >
                <p class="text-sm">{{ msg.content }}</p>
              </div>
            </div>

            <!-- AI Message -->
            <div v-else class="flex justify-start">
              <div
                class="max-w-xs bg-gray-100 text-gray-900 rounded-2xl rounded-tl-none px-4 py-3 shadow-md"
              >
                <p class="text-sm">{{ msg.content }}</p>
              </div>
            </div>
          </div>

          <!-- Loading Indicator -->
          <div v-if="isLoading" class="flex justify-start">
            <div
              class="bg-gray-100 rounded-2xl rounded-tl-none px-4 py-3 shadow-md"
            >
              <div class="flex items-center gap-2">
                <div
                  class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                  style="animation-delay: 0s"
                ></div>
                <div
                  class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                  style="animation-delay: 0.1s"
                ></div>
                <div
                  class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                  style="animation-delay: 0.2s"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Divider -->
        <div class="border-t border-gray-200"></div>

        <!-- Input Area -->
        <div class="p-4">
          <form @submit.prevent="sendMessage" class="flex gap-3">
            <input
              v-model="inputMessage"
              type="text"
              placeholder="Type your medical question..."
              class="flex-1 px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:border-primary-500 focus:ring-2 focus:ring-primary-200 transition-colors"
              :disabled="isLoading"
            />
            <button
              type="submit"
              :disabled="isLoading || !inputMessage.trim()"
              class="btn-primary flex items-center gap-2"
            >
              <svg
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                />
              </svg>
              Send
            </button>
          </form>

          <!-- Error Message -->
          <div
            v-if="error"
            class="mt-3 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm"
          >
            {{ error }}
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import api from "../utils/api";
import { RouterLink } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();

interface Message {
  type: "user" | "ai";
  content: string;
}

const messages = ref<Message[]>([]);
const inputMessage = ref("");
const isLoading = ref(false);
const error = ref<string | null>(null);
const messagesContainer = ref<HTMLElement | null>(null);

const scrollToBottom = async () => {
  await nextTick();
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
  }
};

const sendMessage = async () => {
  if (!inputMessage.value.trim()) return;

  error.value = null;
  const userMessage = inputMessage.value.trim();
  inputMessage.value = "";

  // Add user message
  messages.value.push({
    type: "user",
    content: userMessage,
  });

  scrollToBottom();

  isLoading.value = true;
  try {
    const response = await api.post("/chat", {
      question: userMessage,
    });

    // Add AI response
    messages.value.push({
      type: "ai",
      content: response.data.answer,
    });

    scrollToBottom();
  } catch (err: any) {
    error.value =
      err.response?.data?.detail || "Failed to get response. Please try again.";
  } finally {
    isLoading.value = false;
  }
};

const handleLogout = () => {
  authStore.logout();
  router.push("/login");
};
</script>
