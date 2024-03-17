import { createRouter, createWebHistory } from "vue-router"
import axios from "axios"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/auth",
            name: "auth",
            component: () => import("@/views/AuthView.vue"),
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
                        if (response.data) {
                            next()
                        } else {
                            next({ name: "auth" })
                        }
                    })
                    .catch((e) => {
                        next({ name: "auth" })
                    })
            }
        }
    ]
})

export default router
