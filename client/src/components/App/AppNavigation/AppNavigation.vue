<script setup>
import NavigationTitle from "@/components/App/AppNavigation/fragments/NavigationTitle.vue"
import NavigationMenu from "@/components/App/AppNavigation/fragments/NavigationMenu.vue"
</script>

<template>
    <div class="navigation">
        <NavigationTitle />
        <NavigationMenu />
    </div>
</template>

<style lang="scss" scoped>
.navigation {
    @apply basis-1/5 h-full w-full flex flex-col items-center space-y-lg;

    @screen 2xl {
        @apply space-y-xl;
    }
}
</style>
