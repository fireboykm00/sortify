<script lang="ts" setup>
import { ref } from "vue";

// Developer information
const developer = {
  name: "Kwizera Mugisha Olivier",
  email: "kwizeramugishaolivier0@gmail.com",
  github: "github.com/fireboykm00",
  linkedin: "linkedin.com/in/fireboykm00",
};

// App information
const appInfo = {
  version: "1.0.0",
  releaseDate: "May 2025",
  license: "MIT",
};

// Features list
const features = [
  {
    title: "Smart Organization",
    description:
      "Automatically categorizes your files based on file types and extensions",
    icon: "i-mdi-brain",
  },
  {
    title: "Instant Processing",
    description:
      "Processes files quickly and efficiently for immediate organization",
    icon: "i-mdi-lightning-bolt",
  },
  {
    title: "Secure Storage",
    description:
      "Files are stored securely and automatically deleted after 1 hour",
    icon: "i-mdi-shield-check",
  },
  {
    title: "Easy Download",
    description: "Download your organized files as a convenient ZIP archive",
    icon: "i-mdi-download",
  },
];

// FAQ items
const faqs = ref([
  {
    question: "How long are my files stored?",
    answer:
      "Your files are automatically deleted after 1 hour to ensure privacy and security.",
    isOpen: false,
  },
  {
    question: "What file types are supported?",
    answer:
      "Sortify supports virtually all common file types including documents, images, videos, audio files, archives, and more.",
    isOpen: false,
  },
  {
    question: "Is there a file size limit?",
    answer:
      "The current version limits uploads to 100MB per session to ensure optimal performance.",
    isOpen: false,
  },
  {
    question: "Can I customize the organization categories?",
    answer:
      "Custom categories are coming in our next update. Currently, we use intelligent default categories based on file types.",
    isOpen: false,
  },
]);

// Toggle FAQ item
const toggleFaq = (index: number) => {
  faqs.value[index].isOpen = !faqs.value[index].isOpen;
};
</script>

<template>
  <div class="min-h-screen bg-white">
    <!-- Hero section -->
    <div class="w-full bg-blue-500 text-white py-16">
      <div class="container mx-auto px-4 max-w-4xl">
        <h1 class="text-4xl font-bold mb-4">About Sortify</h1>
        <p class="text-xl">
          The smart file organization tool that brings order to digital chaos.
        </p>
      </div>
    </div>

    <!-- App description -->
    <div class="container mx-auto px-4 py-12 max-w-4xl">
      <div class="mb-12">
        <h2 class="text-3xl font-bold mb-6">Our Mission</h2>
        <p class="text-lg text-gray-700">
          Sortify was born from a simple idea: managing files shouldn't be
          complicated. We believe that organizing digital content should be
          effortless and intuitive. Our application uses intelligent
          categorization to bring order to your files, saving you time and
          reducing the stress of managing digital clutter.
        </p>
      </div>

      <!-- Features section -->
      <div class="mb-16">
        <h2 class="text-3xl font-bold mb-8">Key Features</h2>
        <div class="grid md:grid-cols-2 gap-8">
          <div
            v-for="(feature, index) in features"
            :key="index"
            class="bg-gray-50 p-6 rounded-lg shadow-sm"
          >
            <div class="flex items-center mb-4">
              <Icon :name="feature.icon" class="text-blue-500 text-2xl mr-3" />
              <h3 class="text-xl font-semibold">{{ feature.title }}</h3>
            </div>
            <p class="text-gray-700">{{ feature.description }}</p>
          </div>
        </div>
      </div>

      <!-- How it works -->
      <div class="mb-16">
        <h2 class="text-3xl font-bold mb-6">How It Works</h2>
        <div class="bg-gray-50 p-8 rounded-lg">
          <ol class="relative border-l border-gray-300">
            <li class="mb-10 ml-6">
              <div
                class="absolute w-8 h-8 bg-blue-500 rounded-full -left-4 flex items-center justify-center"
              >
                <span class="text-white font-bold">1</span>
              </div>
              <h3 class="text-xl font-semibold mb-2">Upload Your Files</h3>
              <p class="text-gray-700">
                Drag and drop your files or use the file browser to select
                multiple files for organization.
              </p>
            </li>
            <li class="mb-10 ml-6">
              <div
                class="absolute w-8 h-8 bg-blue-500 rounded-full -left-4 flex items-center justify-center"
              >
                <span class="text-white font-bold">2</span>
              </div>
              <h3 class="text-xl font-semibold mb-2">Automatic Organization</h3>
              <p class="text-gray-700">
                Our intelligent system analyzes your files and organizes them
                into appropriate categories.
              </p>
            </li>
            <li class="mb-10 ml-6">
              <div
                class="absolute w-8 h-8 bg-blue-500 rounded-full -left-4 flex items-center justify-center"
              >
                <span class="text-white font-bold">3</span>
              </div>
              <h3 class="text-xl font-semibold mb-2">
                Preview Organized Structure
              </h3>
              <p class="text-gray-700">
                See exactly how your files have been organized before
                downloading.
              </p>
            </li>
            <li class="ml-6">
              <div
                class="absolute w-8 h-8 bg-blue-500 rounded-full -left-4 flex items-center justify-center"
              >
                <span class="text-white font-bold">4</span>
              </div>
              <h3 class="text-xl font-semibold mb-2">Download and Enjoy</h3>
              <p class="text-gray-700">
                Download your organized files as a ZIP archive and enjoy your
                newly organized files.
              </p>
            </li>
          </ol>
        </div>
      </div>

      <!-- FAQ section -->
      <div class="mb-16">
        <h2 class="text-3xl font-bold mb-6">Frequently Asked Questions</h2>
        <div class="space-y-4">
          <div
            v-for="(faq, index) in faqs"
            :key="index"
            class="border border-gray-200 rounded-lg"
          >
            <button
              @click="toggleFaq(index)"
              class="flex justify-between items-center w-full p-4 text-left font-semibold"
            >
              {{ faq.question }}
              <Icon
                :name="faq.isOpen ? 'i-mdi-chevron-up' : 'i-mdi-chevron-down'"
                class="text-blue-500"
              />
            </button>
            <div v-if="faq.isOpen" class="p-4 pt-0 text-gray-700">
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>

      <!-- Developer information -->
      <div class="mb-16">
        <h2 class="text-3xl font-bold mb-6">Developer Contact</h2>
        <div class="bg-gray-50 p-6 rounded-lg shadow-sm">
          <div class="flex items-center mb-4">
            <div
              class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mr-4"
            >
              <Icon name="i-mdi-account" class="text-blue-500 text-3xl" />
            </div>
            <div>
              <h3 class="text-xl font-semibold">{{ developer.name }}</h3>
              <p class="text-gray-700">Lead Developer</p>
            </div>
          </div>
          <div class="space-y-2 mt-4">
            <div class="flex items-center">
              <Icon name="i-mdi-email" class="text-blue-500 mr-2" />
              <a
                :href="`mailto:${developer.email}`"
                class="text-blue-600 hover:underline"
                >{{ developer.email }}</a
              >
            </div>
            <div class="flex items-center">
              <Icon name="i-mdi-github" class="text-blue-500 mr-2" />
              <a
                :href="`https://${developer.github}`"
                target="_blank"
                class="text-blue-600 hover:underline"
                >{{ developer.github }}</a
              >
            </div>
            <div class="flex items-center">
              <Icon name="i-mdi-linkedin" class="text-blue-500 mr-2" />
              <a
                :href="`https://${developer.linkedin}`"
                target="_blank"
                class="text-blue-600 hover:underline"
                >{{ developer.linkedin }}</a
              >
            </div>
          </div>
        </div>
      </div>

      <!-- App information -->
      <div class="mt-12 p-6 bg-gray-50 rounded-lg">
        <div class="text-center">
          <h3 class="text-xl font-semibold mb-2">Sortify</h3>
          <p class="text-gray-700 mb-1">Version {{ appInfo.version }}</p>
          <p class="text-gray-700 mb-1">Released {{ appInfo.releaseDate }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Any additional component-specific styles can go here */
</style>
