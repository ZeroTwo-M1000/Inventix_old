import { createRouter, createWebHistory } from "vue-router"
import axios from "axios"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/auth",
            name: "auth",
            components: {
                auth: () => import("@/views/AuthView.vue")
            },
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/auth/me")
                    .then((response) => {
                        next({ name: "home" })
                    })
                    .catch((e) => {
                        next()
                    })
            }
        },
        {
            path: "/",
            name: "home",
            component: () => import("@/views/HomeView.vue"),
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/auth/me")
                    .then((response) => {
                        if (response.data.success) {
                            next()
                        } else {
                            next({ name: "auth" })
                        }
                    })
                    .catch((e) => {
                        next({ name: "auth" })
                    })
            }
        },
        {
            path: "/statistic",
            name: "statistic",
            component: () => import("@/views/StatisticView.vue"),
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/auth/me")
                    .then((response) => {
                        if (response.data.success) {
                            next()
                        } else {
                            next({ name: "auth" })
                        }
                    })
                    .catch((e) => {
                        next({ name: "auth" })
                    })
            }
        },
        {
            path: "/news",
            name: "news",
            component: () => import("@/views/NewsView.vue"),
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/auth/me")
                    .then((response) => {
                        if (response.data.success) {
                            next()
                        } else {
                            next({ name: "auth" })
                        }
                    })
                    .catch((e) => {
                        next({ name: "auth" })
                    })
            }
        },
        {
            path: "/reviews",
            name: "reviews",
            component: () => import("@/views/ReviewsView.vue"),
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/auth/me")
                    .then((response) => {
                        if (response.data.success) {
                            next()
                        } else {
                            next({ name: "auth" })
                        }
                    })
                    .catch((e) => {
                        next({ name: "auth" })
                    })
            }
        },
        {
            path: "/bookmark",
            name: "bookmark",
            component: () => import("@/views/BookmarkView.vue"),
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/auth/me")
                    .then((response) => {
                        if (response.data.success) {
                            next()
                        } else {
                            next({ name: "auth" })
                        }
                    })
                    .catch((e) => {
                        next({ name: "auth" })
                    })
            }
        },
        {
            path: "/:pathMatch(.*)*",
            name: "404",
            component: () => import("@/views/404View.vue")
        }
    ],
    scrollBehavior() {
        return { top: 0 }
    }
})

export default router
