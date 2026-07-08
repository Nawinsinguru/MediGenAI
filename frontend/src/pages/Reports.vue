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
          Generate Medical Report
        </h2>
        <p class="text-gray-600 mt-2">
          Create a professional medical report with AI-generated insights
        </p>
      </div>

      <!-- Report Form -->
      <div class="card shadow-lg">
        <form @submit.prevent="generateReport" class="space-y-6">
          <!-- Patient Name -->
          <div>
            <label class="block text-sm font-semibold text-gray-900 mb-2"
              >Patient Name</label
            >
            <input
              v-model="form.patientName"
              type="text"
              placeholder="Enter patient name"
              class="input-field"
              required
            />
          </div>

          <!-- Age -->
          <div class="grid md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-900 mb-2"
                >Age</label
              >
              <input
                v-model.number="form.age"
                type="number"
                placeholder="Enter age"
                class="input-field"
                required
              />
            </div>

            <!-- Gender -->
            <div>
              <label class="block text-sm font-semibold text-gray-900 mb-2"
                >Gender</label
              >
              <select v-model="form.gender" class="input-field" required>
                <option value="">Select gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
              </select>
            </div>
          </div>

          <!-- Clinical Findings -->
          <div>
            <label class="block text-sm font-semibold text-gray-900 mb-2"
              >Clinical Findings</label
            >
            <textarea
              v-model="form.findings"
              placeholder="Enter clinical findings, symptoms, and observations..."
              class="input-field resize-none"
              rows="6"
              required
            ></textarea>
            <p class="text-xs text-gray-500 mt-2">
              Provide detailed clinical information for better report generation
            </p>
          </div>

          <!-- Error Message -->
          <div
            v-if="error"
            class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700"
          >
            {{ error }}
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="isLoading"
            class="btn-primary w-full flex items-center justify-center gap-2"
          >
            <svg
              v-if="!isLoading"
              class="w-5 h-5"
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
            <span v-if="!isLoading">Generate Report</span>
            <span v-else>Generating...</span>
          </button>
        </form>
      </div>

      <!-- Generated Report -->
      <div v-if="generatedReport" class="mt-12 animate-slide-up">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-2xl font-bold text-gray-900">Generated Report</h3>
          <button
            @click="copyToClipboard"
            class="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition"
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
                d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"
              />
            </svg>
            Copy
          </button>
        </div>

        <div
          class="card shadow-lg bg-gradient-to-br from-gray-50 to-white border-l-4 border-primary-500"
        >
          <div class="prose prose-sm max-w-none">
            <div
              class="whitespace-pre-wrap text-gray-700 leading-relaxed font-medium"
            >
              {{ generatedReport }}
            </div>
          </div>
        </div>

        <!-- Download Button -->
        <button
          @click="downloadReport"
          class="mt-6 btn-primary flex items-center gap-2 mx-auto"
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
              d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
            />
          </svg>
          Download as Text
        </button>
      </div>

      <!-- Success Message -->
      <div
        v-if="copySuccess"
        class="fixed bottom-6 right-6 p-4 bg-green-500 text-white rounded-lg shadow-lg animate-slide-up"
      >
        Report copied to clipboard!
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

const form = ref({
  patientName: "",
  age: null as number | null,
  gender: "",
  findings: "",
});

const isLoading = ref(false);
const error = ref<string | null>(null);
const generatedReport = ref<string | null>(null);
const copySuccess = ref(false);

const generateReport = async () => {
  if (
    !form.value.patientName ||
    !form.value.age ||
    !form.value.gender ||
    !form.value.findings
  ) {
    error.value = "Please fill in all fields";
    return;
  }

  error.value = null;
  isLoading.value = true;

  try {
    const response = await api.post("/reports/generate", {
      patient_name: form.value.patientName,
      age: form.value.age,
      gender: form.value.gender,
      findings: form.value.findings,
    });

    generatedReport.value = response.data.report;
  } catch (err: any) {
    error.value = err.response?.data?.detail || "Failed to generate report";
  } finally {
    isLoading.value = false;
  }
};

const copyToClipboard = async () => {
  if (generatedReport.value) {
    await navigator.clipboard.writeText(generatedReport.value);
    copySuccess.value = true;
    setTimeout(() => {
      copySuccess.value = false;
    }, 2000);
  }
};

const downloadReport = () => {
  if (!generatedReport.value) return;

  const element = document.createElement("a");
  element.setAttribute(
    "href",
    "data:text/plain;charset=utf-8," +
      encodeURIComponent(generatedReport.value),
  );
  element.setAttribute(
    "download",
    `medical_report_${new Date().toISOString().split("T")[0]}.txt`,
  );
  element.style.display = "none";
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
};

const handleLogout = () => {
  authStore.logout();
  router.push("/login");
};
</script>
