import { defineStore } from "pinia"
import { ref } from "vue"

export const useNavigation = defineStore("navigation", () => {
    const ItemList = ref([
        {
            name: "home",
            span: "Главная",
            icon: new URL("@/assets/icon/home.svg", import.meta.url)
        },
        {
            name: "statistic",
            span: "Статистика",
            icon: new URL("@/assets/icon/activity.svg", import.meta.url)
        },
        {
            name: "bookmark",
            span: "Избранное",
            icon: new URL("@/assets/icon/bookmark.svg", import.meta.url)
        },
        {
            name: "reviews",
            span: "Отзывы",
            icon: new URL("@/assets/icon/message-square.svg", import.meta.url)
        },
        {
            name: "news",
            span: "Новости",
            icon: new URL("@/assets/icon/news.svg", import.meta.url)
        }
    ])

    return { ItemList }
})
