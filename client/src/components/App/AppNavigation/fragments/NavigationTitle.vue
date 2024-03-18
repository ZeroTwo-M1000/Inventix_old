<script setup></script>

<template>
    <div class="title">
        <img alt="logo" src="../../../../assets/logo.svg" />
        <h1 class="title-text">Inventix</h1>
    </div>
</template>

<style lang="scss" scoped>
.title {
    @apply flex items-center;

    &-text {
        @apply text-4xl font-semibold ml-md select-none cursor-default;
    }
}
</style>
