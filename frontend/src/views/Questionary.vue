<template>
    <v-container class="container">
      <div class="wrapper">
        <div class="navigation">
          <a href="#" class="navigation__link">Личные и персональные данные</a>
          <a href="#" class="navigation__link">Адрес постоянной регистрации</a>
          <a href="#" class="navigation__link">Документ об образовании</a>
          <a href="#" class="navigation__link">Личные достижения</a>
          <a href="#" class="navigation__link">Родственники</a>
          <a href="#" class="navigation__link">Льготы</a>
          <a href="#" class="navigation__link">Загруженные документы</a>
          <a href="#" class="navigation__link">Доп.информация</a>
        </div>

        <div class="questionary">
          <img src="../assets/img/photo.png" class="questionary__photo">
          <a href="#" class="questionary__photo-download">Загрузите ваше фото</a>
          <h2 class="questionary__header">Личные данные</h2>
          <v-text-field class="questionary__name"
          label="Фамилия"
          v-model="name"
          outlined
          >
          </v-text-field>

          <v-text-field class="questionary__birthday-date"
          label="Имя"
          v-model="birthdayDate"
          outlined>
          </v-text-field>

          <v-text-field class="questionary__birthday-place"
          label="Отчество"
          v-model="birthdayPlace"
          outlined>
          </v-text-field>

          <v-text-field class="questionary__passport"
          label="E-mail"
          v-model="passport"
          outlined>
          </v-text-field>

          <v-text-field class="questionary__passport-address"
          label="Мобильный телефон"
          v-model="passportAddress"
          outlined>
          </v-text-field>

          <h2 class="questionary__header">Персональные данные</h2>
          <v-text-field 
          class="questionary__real-address"
          label="Дата рождения"
          v-model="realAddress"
          outlined>
          </v-text-field>

          <v-text-field 
          class="questionary__name"
          label="Место рождения"
          v-model="phone"
          outlined>
          </v-text-field>

          <v-text-field 
          class="questionary__birthday-date"
          label="Гражданство"
          v-model="email"
          outlined>
          </v-text-field>

          <v-text-field 
          class="questionary__birthday-place"
          label="Документ, удостоверяющий личность"
          v-model="birthdayPlace"
          outlined>
          </v-text-field>

          <v-text-field 
          class="questionary__nationality"
          label="Серия"
          v-model="nationality"
          outlined>
          </v-text-field>

          <v-text-field 
          class="questionary__military-registration"
          label="Номер"
          v-model="militaryRegistration"
          outlined>
          </v-text-field>

          <v-text-field 
          class="questionary__education"
          label="Кем выдан"
          v-model="education"
          outlined>
          </v-text-field>

          <v-btn 
          class="questionary__button-save"
          elevation="8"
          color="#4244A6"
          style="color: white;"
          @click="toSave">
            Сохранить данные профиля
          </v-btn>
        </div>
      </div>
    </v-container>
</template>

<style scoped>
  .container {
    position: relative;
    margin: 0 auto;
  }

  .navigation {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    height: 435px;
  }

  .navigation__link {
    text-decoration: none;
    color: #5ECACE;
    width: 323px;
  }

  .questionary {
    padding: 15px;
    text-align: center;
    margin: 0 auto;
    width: -webkit-fill-available;
  }

  .questionary__button-save {
    color: white;
  }

  .questionary__header {
    text-align: left;
  }

  .questionary__photo {
    text-align: left;
    display: block;
  }

  .questionary__photo-download {
    text-decoration: none;
    text-align: left;
    display: block;
  }

  .wrapper {
    display: flex;
  }
</style>

<script>
export default {
    name: "Questionary",
    data: () => ({
      name: "",
      birthdayDate: "",
      birthdayPlace: "",
      passport: "",
      passportAddress: "",
      realAddress: "",
      phone: "",
      email: "",
      birthdayPlace: "",
      nationality: "",
      militaryRegistration: "",
      education: "",
    }),

    methods: {
      toSave() {
        console.log("Данные успешно сохранены")
      }
    } 

}
</script>
