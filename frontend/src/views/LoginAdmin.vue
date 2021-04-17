<template>
    <div>
        <HeaderAdmin />
        <v-card class="login" 
        elevation="2">
            <h2 class="login__header">Вход в личный кабинет</h2>
            <v-text-field
            outlined
            label="Логин">
            </v-text-field>

            <v-text-field
            outlined
            label="Пароль">
            </v-text-field>

            <v-btn class="enter-button"
            color="#4244A6"
            style="color: white"
            @click="toEnter"
            >Войти</v-btn>
        </v-card>
    </div>
</template>

<style scoped>
    .login {
        width: 555px;
        height: 367px;
        margin: 0 auto;
        padding: 60px;
        display: grid;
    }

    .login__header {
        font-family: Manrope;
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 27px;
        color: #4244A6;
    }

    .enter-button {
        border: 2px solid #4244A6;
        box-sizing: border-box;
        border-radius: 20px
    }
</style>

<script>
    import HeaderAdmin from "../components/HeaderAdmin.vue"

    export default {
        name: "LoginAdmin",
        components: {
            HeaderAdmin
        },

        methods: {
            toEnter() {
                console.log("Entered")
                this.$router.push("profile")
            }
        }
    }
</script>