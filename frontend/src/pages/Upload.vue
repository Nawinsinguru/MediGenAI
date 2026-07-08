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
        <h2 class="text-3xl font-bold text-gray-900">
          Upload Medical Documents
        </h2>
        <p class="text-gray-600 mt-2">
          Upload PDF files to enhance AI knowledge base
        </p>
      </div>

      <!-- Upload Area -->
      <div class="card shadow-lg">
        <div
          @dragover.prevent="isDragging = true"
          @dragleave.prevent="isDragging = false"
          @drop.prevent="handleDrop"
          class="border-2 border-dashed rounded-xl p-8 transition"
          :class="
            isDragging
              ? 'border-primary-500 bg-primary-50'
              : 'border-gray-200 bg-gray-50'
          "
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
                  d="M12 4v16m8-8H4"
                />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">
              Drop your PDF here
            </h3>
            <p class="text-gray-600 text-sm mb-4">or click to select files</p>
            <label class="btn-primary inline-block cursor-pointer">
              Select PDF
              <input
                type="file"
                accept=".pdf"
                class="hidden"
                @change="handleFileSelect"
              />
            </label>
            <p class="text-xs text-gray-500 mt-4">Maximum file size: 10MB</p>
          </div>
        </div>

        <!-- Upload Progress -->
        <div v-if="uploadProgress > 0 && uploadProgress < 100" class="mt-6">
          <div class="flex items-center justify-between mb-2">
            <p class="text-sm font-medium text-gray-700">Uploading...</p>
            <p class="text-sm font-medium text-gray-700">
              {{ uploadProgress }}%
            </p>
          </div>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div
              class="bg-gradient-to-r from-primary-500 to-primary-600 h-2 rounded-full transition-all"
              :style="{ width: uploadProgress + '%' }"
            ></div>
          </div>
        </div>

        <!-- Error Message -->
        <div
          v-if="error"
          class="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700"
        >
          {{ error }}
        </div>

        <!-- Success Message -->
        <div
          v-if="uploadSuccess"
          class="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg text-green-700"
        >
          File uploaded successfully!
        </div>
      </div>

      <!-- Recent Uploads -->
      <div v-if="recentUploads.length > 0" class="mt-12">
        <h3 class="text-xl font-bold text-gray-900 mb-6">Recent Uploads</h3>
        <div class="space-y-3">
          <div
            v-for="(file, idx) in recentUploads"
            :key="idx"
            class="flex items-center justify-between p-4 bg-white border border-gray-200 rounded-lg hover:shadow-md transition"
          >
            <div class="flex items-center gap-3">
              <div
                class="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center"
              >
                <svg
                  class="w-6 h-6 text-red-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
                  />
                </svg>
              </div>
              <div>
                <p class="font-medium text-gray-900">{{ file.name }}</p>
                <p class="text-xs text-gray-500">{{ file.date }}</p>
              </div>
            </div>
            <div class="flex items-center gap-2">
              <span
                class="text-xs font-semibold text-green-600 bg-green-100 px-3 py-1 rounded-full"
                >Processed</span
              >
              <button class="p-2 hover:bg-gray-100 rounded-lg transition">
                <svg
                  class="w-5 h-5 text-gray-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import api from "../utils/api";
import { RouterLink } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();

const isDragging = ref(false);
const uploadProgress = ref(0);
const error = ref<string | null>(null);
const uploadSuccess = ref(false);
const recentUploads = ref([
  {
    name: "Patient_Report_2024.pdf",
    date: "2 days ago",
  },
  {
    name: "Medical_History.pdf",
    date: "1 week ago",
  },
]);

const handleFileSelect = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;
  if (files && files.length > 0) {
    await uploadFile(files[0]);
  }
};

const handleDrop = async (event: DragEvent) => {
  isDragging.value = false;
  const files = event.dataTransfer?.files;
  if (files && files.length > 0) {
    await uploadFile(files[0]);
  }
};

const uploadFile = async (file: File) => {
  error.value = null;
  uploadSuccess.value = false;

  if (file.type !== "application/pdf") {
    error.value = "Please upload a PDF file";
    return;
  }

  if (file.size > 10 * 1024 * 1024) {
    error.value = "File size must be less than 10MB";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    uploadProgress.value = 0;
    const progressInterval = setInterval(() => {
      if (uploadProgress.value < 90) {
        uploadProgress.value += Math.random() * 30;
      }
    }, 300);

    await api.post("/upload/pdf", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    clearInterval(progressInterval);
    uploadProgress.value = 100;

    uploadSuccess.value = true;
    setTimeout(() => {
      uploadProgress.value = 0;
      uploadSuccess.value = false;
    }, 3000);

    // Add to recent uploads
    recentUploads.value.unshift({
      name: file.name,
      date: "Just now",
    });
  } catch (err: any) {
    error.value = err.response?.data?.detail || "Failed to upload file";
    uploadProgress.value = 0;
  }
};

const handleLogout = () => {
  authStore.logout();
  router.push("/login");
};
</script>
