import { defineStore } from "pinia"
import axios from "axios"
import { computed, ref } from "vue"

export const useAuth = defineStore("auth", () => {
    const error = ref("")

    const get_error = computed(() => {
        return error.value
    })

    const empty_error = () => {
        error.value = ""
    }

    const login = async (login, password) => {
        await axios
            .post("/auth/login", {
                name: login,
                password: password
            })
            .then((response) => {
                if (response.data.access_token) {
                    localStorage.setItem("token", response.data.access_token)
                    error.value = ""
                    location.reload()
                } else {
                    localStorage.removeItem("token")
                    error.value = "Не верный логин или пароль"
                }
            })
    }

    return {
        login,
        get_error,
        empty_error
    }
})
