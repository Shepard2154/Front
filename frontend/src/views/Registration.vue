<template>
    <div>
      <Header />
      <v-container class="container">
        <h2 class="container__header">Регистрация</h2>
        <div class="registration-form">
          <h4 class="registration-form__header">Личные данные</h4>
          <h4 class="registration-form__header">Данные для входа в систему</h4>
        </div>

        <div class="registration">
          <div class="registration__personal-data">
            <v-text-field 
            class="registration-field"
            label="Фамилия"
            hide-details="auto"
            v-model="surname"
            outlined>
            </v-text-field>

            <v-text-field 
            class="registration-field"
            label="Имя"
            hide-details="auto"
            v-model="name"
            outlined>
            </v-text-field>

            <v-text-field 
            class="registration-field"
            label="Отчество"
            hide-details="auto"
            v-model="patronymic"
            outlined>
            </v-text-field>

            <v-text-field 
            class="registration-field"
            label="Регион"
            hide-details="auto"
            v-model="region"
            outlined>
            </v-text-field>
          </div>

          <div class="registration__enter-data">
            <v-text-field 
            class="registration-field"
            label="E-mail"
            hide-details="auto"
            v-model="email"
            outlined>
            </v-text-field>

            <v-text-field 
            class="registration-field"
            label="Пароль"
            hide-details="auto"
            v-model="password"
            outlined>
            </v-text-field>

            <v-text-field 
            class="registration-field"
            label="Повторите пароль"
            hide-details="auto"
            v-model="passwordRepeted"
            outlined>
            </v-text-field>

            <v-text-field 
            class="registration-field"
            label="Мобильный телефон"
            hide-details="auto"
            v-model="phone"
            outlined>
            </v-text-field>
          </div>
        </div>

        <v-checkbox
        v-model="isForeign"
        label="Иностранный гражданин">
        </v-checkbox>

        <v-btn 
        class="registration__button-register"
        elevation="8"
        color="#4244A6"
        style="color: white;"
        @click="toRegistrate">
          Зарегистрироваться
      </v-btn>

        <v-checkbox
        v-model="isAgreed"
        label="Согласие на обработку персональных данных">
        </v-checkbox>
      </v-container>
    </div>
</template>

<style scoped>
  .container {
    position: relative;
    max-width: 800px;
  }

  .container__header {
    color: #4244A6;
  }

  .registration-form {
    display: flex;
    justify-content: space-between;
    padding-top: 35px;
  }

  .registration-form__header {
    font-family: Manrope;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 25px;
    color: #52647B;
  }

  .registration {
    width: 488px;
    height: 324px;
    padding: 15px;
    text-align: center;
    display: flex;
    top: 50%;
    justify-content: space-between;
    width: auto;
  }

  .registration__button-register {
    border-radius: 20px;
    font-family: Manrope;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 25px;
    float: right;
  }

  .registration__personal-data {
    display: flex;
    flex-direction: column;
  }

  .registration__enter-data {
    display: flex;
    flex-direction: column;
  }

  .registration-field {
    min-width: 325px;
  }
</style>

<script>
  import Header from "../components/Header.vue" 

  export default {
    name: "Registration",
    components: {
      Header
    },
    data: () => ({
      surname: "",
      name: "",
      patronymic: "",
      region: "",
      email: "",
      password: "",
      passwordRepeted: "",
      phone: "",

      isForeign: false,
      isAgreed: false,
    }),

    methods: {
      toRegistrate() {
        this.$router.push("/login")
        console.log(this.loginData, this.passwordData, this.emailData)
        console.log(this.isForeign, this.isAgreed)
      }
    } 
  }
</script>