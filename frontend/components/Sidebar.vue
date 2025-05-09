<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const currentRoute = computed(() => route.path);

// Define emit for close event
const emit = defineEmits(["close"]);
</script>
<template>
  <div class="h-full z-100">
    <!-- Mobile close button -->
    <button
      @click="$emit('close')"
      class="absolute top-4 right-4 md:hidden p-2 rounded-lg text-blue-500 bg-blue-100 hover:bg-blue-50 flex justify-center items-center"
    >
      <Icon name="i-mdi-close" class="text-xl" />
    </button>

    <div class="h-full overflow-y-auto">
      <!-- Gradient Logo -->
      <div
        class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-indigo-600 p-6"
      >
        Sortify
      </div>

      <!-- Navigation -->
      <nav class="space-y-2 p-6">
        <NuxtLink
          to="/"
          :class="[
            'rounded-2xl px-3 py-2.5 transition-colors flex flex-row gap-2 items-center',
            currentRoute === '/'
              ? 'bg-blue-500 text-white'
              : 'hover:bg-blue-100 text-gray-800',
          ]"
        >
          <Icon name="i-mdi-home" class="text-2xl" />
          Home
        </NuxtLink>

        <NuxtLink
          to="/about"
          :class="[
            'rounded-2xl px-3 py-2.5 transition-colors flex flex-row gap-2 items-center',
            currentRoute === '/about'
              ? 'bg-blue-500 text-white'
              : 'hover:bg-blue-100 text-gray-800',
          ]"
        >
          <Icon name="i-mdi-information-outline" class="text-2xl" />
          About Us
        </NuxtLink>
      </nav>
    </div>
  </div>
</template>
