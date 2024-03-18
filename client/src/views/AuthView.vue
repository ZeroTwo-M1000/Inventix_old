<script setup>
import BlockBorder from "@/components/App/BlockBorder.vue"
import { useAuth } from "@/stores/Auth/useAuth.js"
import { ref, toRefs } from "vue"

const auth = useAuth()

const { get_error } = toRefs(auth)

const login = ref("")
const password = ref("")
</script>

<template>
    <div class="auth">
        <div class="group auth-container">
            <img alt="auth" class="auth-container-bg" src="@/assets/auth-bg.svg" />
            <BlockBorder class="auth-container-border" color="grey" radius="35">
                <div class="auth-container-content">
                    <div class="auth-container-content-title">
                        <h1>Авторизация</h1>
                    </div>
                    <div class="auth-container-content-body">
                        <BlockBorder class="input-border" color="grey" radius="15">
                            <i class="bx bx-user"></i>
                            <input v-model="login" placeholder="Логин" type="text" @focus="auth.empty_error" />
                        </BlockBorder>
                        <BlockBorder class="input-border" color="grey" radius="15">
                            <i class="bx bx-lock-alt"></i>
                            <input v-model="password" placeholder="Пароль" type="password" @focus="auth.empty_error" />
                        </BlockBorder>
                        <div v-if="get_error" class="error">
                            <i class="bx bx-block"></i>
                            <p>{{ get_error }}</p>
                        </div>
                    </div>
                    <div class="auth-container-content-btn">
                        <button @click="auth.login(login, password)">Войти в аккаунт</button>
                    </div>
                </div>
            </BlockBorder>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.auth {
    @apply w-full h-screen flex items-center justify-center;

    &-container {
        @apply w-1/2 h-1/2 relative flex items-center justify-end rounded-xl overflow-hidden border border-dark-50;

        &-border {
            @apply w-1/2 h-full group-hover:w-full z-10 shadow-3xl transition-all duration-300;

            &:hover {
                padding: 0 !important;
            }
        }

        &-bg {
            @apply w-full h-full absolute;
        }

        &-content {
            @apply w-full z-10 h-full flex flex-col items-center justify-evenly bg-dark-500 rounded-xl;

            &-title {
                @apply text-3xl group-hover:scale-150 transition-all duration-300 font-medium text-white;

                @screen 2xl {
                    @apply text-4xl;
                }

                h1 {
                    @apply select-none;
                }
            }

            &-body {
                @apply w-4/6 group-hover:w-1/2 transition-all duration-300 relative;

                @screen 2xl {
                    @apply text-xl;
                }

                .error {
                    @apply w-full justify-center text-red flex items-center gap-3 mt-0;

                    animation: drop-down 0.5s forwards;

                    i {
                        @apply text-xl;
                        animation: scale 1s forwards;
                    }
                }

                .input-border {
                    @apply mt-4 flex items-center;

                    i {
                        @apply text-xl absolute text-dark-icon left-3;

                        @screen 2xl {
                            @apply text-2xl;
                        }
                    }
                }

                input {
                    @apply w-full py-2 px-10 rounded-md outline-none bg-dark-300 border-2 border-transparent transition-all duration-300;

                    &:focus {
                        @apply border-2 border-blue;
                    }
                }
            }

            &-btn {
                @apply w-1/2 group-hover:w-5/12 transition-all duration-300;

                @screen 2xl {
                    @apply text-xl;
                }

                button {
                    @apply w-full py-3 px-5 rounded-md outline-none bg-dark-300 hover:bg-blue transition-all duration-300;
                }
            }
        }
    }
}

@keyframes drop-down {
    0% {
        @apply mt-0;
    }

    100% {
        @apply mt-5;
    }
}

@keyframes scale {
    0% {
        @apply scale-100;
    }

    50% {
        @apply scale-150;
    }

    100% {
        @apply scale-100;
    }
}
</style>
