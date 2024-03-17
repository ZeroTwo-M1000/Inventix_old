<script setup>
import { computed } from "vue"

const props = defineProps({
    color: {
        type: String,
        required: true
    },

    radius: {
        type: String,
        required: true
    },
    padding: {
        type: String
    }
})

const colors = {
    grey: "#69696950"
}

const style = computed(() => {
    return {
        background: "linear-gradient(to right bottom, " + colors[props.color] + " 0%, rgba(0, 0, 0, 0) 100%)",
        borderRadius: props.radius + "px",
        padding: "padding" in props ? props.padding : "1px"
    }
})
</script>

<template>
    <div :style="style" class="border">
        <slot />
    </div>
</template>

<style lang="scss" scoped>
.border {
    z-index: -1;
    padding: 1px;
    border: none;
}
</style>
