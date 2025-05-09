<script lang="ts" setup>
import { ref, computed } from "vue";

type PreviewItem = {
  folder: string;
  files: string[];
};

const isOrganizing = ref(false);
const files = ref<FileList | null>(null);
const preview = ref<PreviewItem[]>([]);
const organizedFiles = ref<string[]>([]);
const sessionId = ref<string | null>(null);
const downloadUrl = ref<string | null>(null);
const apiBaseUrl = ref("http://localhost:8000"); // Update this to your API URL

const fileCount = computed(() => (files.value ? files.value.length : 0));
const hasFiles = computed(() => fileCount.value > 0);
const isDownloadReady = computed(() => sessionId.value && downloadUrl.value);

const handleFileInput = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files) {
    files.value = input.files;
  }
};

const handleDrop = (event: DragEvent) => {
  event.preventDefault();
  if (event.dataTransfer?.files) {
    files.value = event.dataTransfer.files;
  }
};

const handleDragOver = (event: DragEvent) => {
  event.preventDefault();
};

const resetForm = () => {
  files.value = null;
  preview.value = [];
  organizedFiles.value = [];
  sessionId.value = null;
  downloadUrl.value = null;

  // Reset the file input field
  const fileInput = document.getElementById("files") as HTMLInputElement;
  if (fileInput) {
    fileInput.value = "";
  }
};

const downloadZip = () => {
  if (sessionId.value) {
    window.open(`${apiBaseUrl.value}/download/${sessionId.value}`, "_blank");
  }
};

const organizeFiles = async () => {
  if (!files.value || files.value.length === 0) return;

  isOrganizing.value = true;

  const formData = new FormData();
  Array.from(files.value).forEach((file) => {
    formData.append("files", file);
  });

  try {
    const response = await fetch(`${apiBaseUrl.value}/files`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(
        `Upload failed: ${response.status} ${response.statusText}`
      );
    }

    const data = await response.json();

    // Store response data
    sessionId.value = data.session_id;
    downloadUrl.value = data.download_url;
    organizedFiles.value = data.organized_files || [];
    preview.value = data.preview || [];
  } catch (error) {
    console.error("Error uploading files:", error);
    alert(`Error uploading files: ${error}`);
  } finally {
    isOrganizing.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen w-full p-10 flex flex-col items-center bg-white">
    <!-- Hero Section -->
    <div class="w-full max-w-3xl text-center">
      <h2 class="text-4xl font-bold">Tired of messy files?</h2>
      <p class="text-lg text-gray-600 mt-2">
        Sortify is a simple, effective tool to help you organize your files in
        seconds.
      </p>
    </div>

    <!-- Upload Section -->
    <div class="w-full max-w-2xl mt-10 text-center">
      <h3 class="text-2xl font-semibold">Upload your files</h3>
      <p class="text-lg text-gray-600 mt-2">
        Let Sortify take care of the rest.
      </p>

      <!-- Drag-and-drop area -->
      <div
        class="flex flex-col items-center bg-gray-100 hover:bg-gray-200 transition p-6 w-full rounded-2xl border-2 border-dashed border-gray-300 text-center mt-6"
        @drop="handleDrop"
        @dragover="handleDragOver"
      >
        <input
          type="file"
          multiple
          hidden
          id="files"
          name="files"
          @change="handleFileInput"
        />
        <label for="files" class="cursor-pointer">
          <Icon name="i-mdi-file-upload" class="text-blue-500 text-6xl mb-2" />

          <!-- if files uploaded set text to files uploaded -->
          <p v-if="files" class="text-gray-700 font-medium">
            Files uploaded: {{ files.length }}
          </p>
          <!-- if files not uploaded show drag and drop -->
          <p v-else class="text-gray-700 font-medium">
            Drag and drop files here or click to select files
          </p>
        </label>
      </div>

      <!-- Organize button -->
      <button
        class="bg-blue-500 text-white px-6 py-3 text-lg rounded-2xl mt-6 hover:bg-blue-600 flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer"
        :disabled="!files || isOrganizing"
        @click="organizeFiles"
      >
        <span v-if="!isOrganizing">Organize Now</span>
        <span v-else>Organizing...</span>
        <Icon name="i-mdi-wand" class="text-white" />
      </button>
    </div>

    <!-- Preview Section -->
    <div class="w-full max-w-4xl mt-12">
      <div class="flex flex-row items-center justify-between">
        <div>
          <h3 class="text-2xl font-semibold">Preview</h3>
          <p class="text-gray-600 mt-1">
            Here’s how your files will be organized.
          </p>
        </div>
        <button
          class="bg-blue-500 text-white px-5 py-3 rounded-2xl hover:bg-blue-600 flex items-center gap-2 cursor-pointer"
          @click="downloadZip"
          :disabled="!isDownloadReady"
        >
          Download ZIP
          <Icon name="i-mdi-download" class="text-white" />
        </button>
      </div>

      <!-- Organized Structure -->
      <div
        class="bg-gray-100 mt-4 p-6 rounded-2xl h-64 overflow-auto text-gray-700 text-sm"
      >
        <ul v-if="preview.length" class="font-mono text-sm text-left">
          <li v-for="(item, index) in preview" :key="index" class="mb-2">
            <div class="flex items-center gap-2 text-blue-600 font-semibold">
              <Icon name="i-mdi-folder" class="text-lg" />
              {{ item.folder }}
            </div>
            <ul class="ml-6 mt-1">
              <li
                v-for="file in item.files"
                :key="file"
                class="flex items-center gap-2 text-gray-700 hover:text-black transition"
              >
                <Icon name="i-mdi-file" class="text-gray-500 text-base" />
                {{ file }}
              </li>
            </ul>
          </li>
        </ul>

        <p v-else class="text-gray-500 text-center">
          No preview available yet.
        </p>
      </div>
    </div>
  </div>
</template>

<style>
ul {
  list-style-type: none;
  padding-left: 0;
}
</style>
