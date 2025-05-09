<template>
  <div
    class="flex flex-row items-center justify-between max-w-2xl shadow-2xl px-10 py-6 mx-auto rounded-full bg-white"
  >
    <div class="text-2xl font-bold text-blue-500">Sortify</div>
    <!-- nav links -->
    <div class="flex flex-row items-center gap-2">
      <NuxtLink to="/" class="hover:text-blue-500 px-3 py-2.5">Home</NuxtLink>
      <NuxtLink to="/about" class="hover:text-blue-500 px-3 py-2.5"
        >About</NuxtLink
      >
    </div>
  </div>
</template>
