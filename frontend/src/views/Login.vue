<template>
    <div>
      <Header />

      <div class="spacer"></div> 

      <v-container class="container">
        <v-row>
          <v-card class="registration"
          style="border-radius: 20px;"
          elevation="3">
            <h2 class="registration__header">Регистрация</h2>
            <p class="registration__main-text">Если у Вас еще нет личного кабинета абитуриента, зарегистрируйтесь в системе.  Регистрация не займет много времени</p>
            <v-btn 
            class="registration__button-register"
            elevation="8"
            color="#4244A6"
            style="color: white"
            @click="toRegistrate">
              Зарегистрироваться
            </v-btn>
          </v-card>

          <v-card class="login"
          style="border-radius: 20px;"
          elevation="3">
            <h2 class="login__header">Вход в систему</h2>
            <v-text-field 
            class="login__login"
            label="E-mail"
            :rules="rules"
            hide-details="auto"
            v-model="loginData"
            outlined>
            </v-text-field>

            <v-text-field 
            class="login__password"
            label="Пароль"
            :rules="rules"
            hide-details="auto"
            v-model="passwordData"
            outlined>
            </v-text-field>

            <v-btn 
            class="login__button-login"
            elevation="8"
            color="#4244A6"
            style="color: white"
            @click="toLogin">
              Войти
            </v-btn>

            <a href="#" class="login__button-forger-pswd">Забыли пароль?</a>
          </v-card>
        </v-row>
      </v-container>
    </div>
</template>

<style scoped>
  .container {
    position: relative;
  }

  .login {
    width: 555px;
    height: 367px;
    padding: 67px;
    text-align: left;
    margin: 0 auto;
    top: 50%;
    display: flex;
    flex-direction: column;
  }

  .login__header {
    color: #4244A6;
  }

  .login__button-login {
    border-radius: 20px;
    width: 154px;
    height: 44px;
  }

  .login__button-forger-pswd {
    text-decoration: none;
    font-family: Manrope;
    font-style: normal;
    font-weight: 300;
    font-size: 17px;
    line-height: 16px;
    color: #6A6A6A;
    padding-top: 15px;
  }

  .registration {
    width: 555px;
    height: 367px;
    padding: 67px;
    text-align: left;
    margin: 0 auto;
    top: 50%;
    display: grid;
  }

  .registration__button-register {
    border-radius: 20px;
    width: 261px;
    height: 44px;
  }

  .registration__header {
    color: #4244A6;
  }

  .registration__main-text {
    font-family: Manrope;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 25px;
    color: #6A6A6A;
  }

  .spacer {
    margin-bottom: 40px;
  }
</style>

<script>
  import Header from "../components/Header.vue"

  export default {
    name: "Login",
    components: {
      Header,
    },
    data: () => ({
    loginData: "",
    passwordData: "",

    rules: [
      value => !!value || 'Это поле обязательно.',
      value => (value && value.length >= 7) || 'Должно быть не меньше 7 символов',
    ],
  }),

  methods: {
    toLogin() {
      this.$router.push("/cabinet/questionary")
      console.log(this.loginData, this.passwordData)
    },

    toRegistrate(){
      this.$router.push("/register")
    }
  } 
  }
</script>