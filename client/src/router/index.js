import { createRouter, createWebHistory } from "vue-router"
import axios from "axios"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        // TODO: 404
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
        }
    ],
    scrollBehavior() {
        return { top: 0 }
    }
})

export default router
