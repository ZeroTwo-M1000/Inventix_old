<script setup>
import AppNavigation from "@/components/App/AppNavigation/AppNavigation.vue"
import AppMain from "@/components/App/AppMain/AppMain.vue"
</script>

<template>
    <router-view name="auth" />
    <div v-if="$route.name !== 'auth'" class="app">
        <AppNavigation />
        <AppMain />
    </div>
</template>

<style lang="scss">
.app {
    @apply w-screen h-screen flex space-x-lg p-lg;

    @screen 2xl {
        @apply space-x-xl p-xl;
    }
}
</style>
