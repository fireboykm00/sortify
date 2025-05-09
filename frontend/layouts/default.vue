<template>
  <div class="flex flex-col min-h-screen">
    <!-- Mobile menu button -->
    <div class="fixed top-4 left-4 md:hidden">
      <button
        @click="isSidebarOpen = !isSidebarOpen"
        class="p-2 rounded-lg text-blue-500 bg-blue-100 hover:bg-blue-50 flex justify-center items-center"
      >
        <Icon
          :name="isSidebarOpen ? 'i-mdi-close' : 'i-mdi-menu'"
          class="text-2xl"
        />
      </button>
    </div>

    <!-- Sidebar -->
    <div
      class="fixed inset-y-0 left-0 z-40 w-full md:w-[200px] bg-white border-r border-gray-300 transform transition-transform duration-300 ease-in-out md:translate-x-0"
      :class="{
        'translate-x-0': isSidebarOpen,
        '-translate-x-full': !isSidebarOpen,
      }"
    >
      <Sidebar @close="isSidebarOpen = false" />
    </div>

    <!-- Main content -->
    <div class="flex-1 min-h-screen md:pl-[200px]">
      <slot />
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRoute } from "#app";

const isSidebarOpen = ref(false);
const route = useRoute();

// Watch for route changes and close sidebar on mobile
watch(() => route.path, () => {
  if (isSidebarOpen.value) {
    isSidebarOpen.value = false;
  }
});
</script>
