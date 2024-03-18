<script setup>
import { useNavigation } from "@/stores/App/useNavigation.js"
import { toRefs } from "vue"
import BlockBorder from "@/components/App/BlockBorder.vue"

const { ItemList } = toRefs(useNavigation())
</script>

<template>
    <div class="navigation-menu">
        <router-link v-for="item in ItemList" :key="item.name" :to="{ name: item.name }" class="navigation-menu-item">
            <BlockBorder :color="item.name === $route.name ? 'blue' : 'none'" class="navigation-menu-item-border" padding="1.5" radius="15">
                <div class="navigation-menu-item-content">
                    <img :alt="item.name" :src="item.icon" />
                    <span>{{ item.span }}</span>
                </div>
            </BlockBorder>
        </router-link>
    </div>
</template>

<style lang="scss" scoped>
.navigation-menu {
    @apply w-full flex flex-col items-center space-y-2;

    &-item {
        @apply w-full;

        &.router-link-active {
            & .navigation-menu-item-content {
                @apply bg-blue;
            }
        }

        &-border {
            @apply w-full transition duration-300;

            @screen 2xl {
                border-radius: 20px !important;
            }

            &:hover {
                @apply scale-105;
            }
        }

        &-content {
            @apply w-full bg-bg flex items-center justify-start px-8 py-3 rounded-md;

            @screen 2xl {
                @apply py-4 rounded-lg;
            }

            span {
                @apply text-xl ml-lg;
            }
        }
    }
}
</style>
