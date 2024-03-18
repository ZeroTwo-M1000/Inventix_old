<script setup>
import BlockBorder from "@/components/App/BlockBorder.vue"
</script>

<template>
    <BlockBorder class="main" color="grey" radius="19">
        <div class="main-content">
            <router-view />
        </div>
    </BlockBorder>
</template>

<style lang="scss" scoped>
.main {
    @apply basis-4/5 h-full w-full;

    @screen 2xl {
        border-radius: 35px !important;
    }

    &-content {
        @apply w-full h-full bg-dark-400 rounded-lg flex flex-col space-y-lg p-lg;

        @screen 2xl {
            @apply 2xl:space-y-xl 2xl:p-xl 2xl:rounded-xl;
        }
    }
}
</style>
