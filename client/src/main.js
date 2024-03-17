import { createApp } from "vue"
import { createPinia } from "pinia"
import "./style.css"

import App from "./App.vue"
import router from "./router"
import "boxicons"
import "boxicons/css/boxicons.min.css"
import axios from "axios"

export const BASE_URL = "http://0.0.0.0:8000"

axios.defaults.baseURL = `${BASE_URL}/api`

const token = localStorage.getItem("token")

if (token) {
    axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
}

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount("#app")
