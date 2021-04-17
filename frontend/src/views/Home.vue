<template>
  <div class='back'>
      <HeaderMain />
       <div class="navbar">
            <v-row class="navbar__data">
                <v-row>
                    <v-col>
                        <v-btn class='btn' plain>Новости</v-btn>
                        <br>
                        <v-btn class='btn' plain>О поступлении</v-btn>
                        <br>
                        <v-btn class='btn' plain>Колледжи и техникумы</v-btn>
                    </v-col>
                </v-row>
            </v-row>
        </div>
        <div class='tool_line'>
            Расписание дней открых дверей
        <v-btn plain style="color:#fff">
            <v-icon dark style="font-size:50px">
              mdi-keyboard-tab
            </v-icon>
          </v-btn>
        </div>
      <v-container>
        <div>
          <h2 style="text-align:center;margin-top:30px" class='head2'>Новости</h2>
        </div>
        <v-container
          fill-height
          fluid
          grid-list-xl>
          <v-layout
            justify-center
            wrap
          >
            <v-flex
            md4>
              <v-card
                :loading="loading"
                class="mx-auto my-5"
                max-width="374"
              >
                <template slot="progress">
                  <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                  ></v-progress-linear>
                </template>

                <v-img
                  height="250"
                  src="../assets/img/3.jpg"
                ></v-img>

                <v-card-title>Проводится олимпиада по ИБ на платформе Томского колледжа</v-card-title>
              </v-card>
            </v-flex>
            <v-flex
            md4>
              <v-card
                :loading="loading"
                class="mx-auto my-5"
                max-width="374"
              >
                <template slot="progress">
                  <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                  ></v-progress-linear>
                </template>

                <v-img
                  height="250"
                  src="../assets/img/4.jpg"
                ></v-img>

                <v-card-title>Открытая лекция по экономике от ведущих специалистов</v-card-title>
              </v-card>
            </v-flex>
            <v-flex
            md4>
              <v-card
                :loading="loading"
                class="mx-auto my-6"
                max-width="374"
              >
                <template slot="progress">
                  <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                  ></v-progress-linear>
                </template>

                <v-img
                  height="250"
                  src="../assets/img/2.jpg"
                ></v-img>

                <v-card-title>Успей подать заявку в мобильном приложении до конца лета</v-card-title>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-container>
      <v-container>
        <div>
          <h2 style="text-align:center;margin-top:30px" class='head2'>О поступлении</h2>
        </div>
        <v-container
          fill-height
          fluid
          grid-list-xl>
          <v-layout
            justify-center
            wrap
          >
            <v-flex
            md5>
              <v-card
                :loading="loading"
                class="mx-auto my-5"
                max-width="374"
              >
                <template slot="progress">
                  <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                  ></v-progress-linear>
                </template>

                <v-img
                  height="250"
                  src="../assets/img/5.jpg"
                ></v-img>

                <v-card-title>Какие документы необходимо подготовить</v-card-title>
              </v-card>
            </v-flex>
            <v-flex
            md7>
              <v-card
                :loading="loading"
                class="mx-auto my-5"
              >
                <template slot="progress">
                  <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                  ></v-progress-linear>
                </template>

                <v-img
                  height="250"
                  src="../assets/img/6.jpg"
                ></v-img>

                <v-card-title>Список поступающих в 2021 годы. Средние проходные баллы</v-card-title>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-container>
      <v-footer
        color="primary lighten-1"
        padless
      >
        <v-row
          justify="center"
          no-gutters
        >
          <v-col
            class="primary lighten-2 py-4 text-center white--text"
            cols="12"
          >
            {{ new Date().getFullYear() }} — <strong>Департамент образования</strong>
          </v-col>
        </v-row>
      </v-footer>
  </div>
</template>

<style scoped>
.head2 {
  font-family: Manrope;
  font-style: normal;
  font-weight: 800;
  font-size: 24px;
  line-height: 33px;

  /* identical to box height */

  color: #52647B;


}
.back {
background-image: url('../assets/img/1.jpg');
bottom: 0;
right: 0;
height: 100%;
width: 100%;
background-position: center;
/* background-repeat: no-repeat;  */
background-size: cover;
position: absolute;
}
.btn {
  font-family: Manrope;
  font-style: normal;
  font-weight: 600;
  font-size: 26px;
  line-height: 26px;
  margin-top:30px;

  /* identical to box height */

  color: #1A0F91;
}
.navbar {
        display: flex;
        padding-top: 160px;
        padding-left: 100px;
        width: 1455px;
        margin: auto;
    }

.navbar__data {
    justify-content: space-evenly;
    display: flex;
}

.navbar__data__text-1, .navbar__data__text-2, .navbar__data__text-3 {
    width: 384px;
    height: 54px;
}

.navbar__data__text-1 {
    color: #4244A6;
}

.navbar__data__text-2 {
    color: #30D5C8;
}

.navbar__data__text-3 {
    color: #52647B;
}

.tool_line {
  margin-top:300px;
  background-color: #FA9746;
  text-align:center;
  font-family: Manrope;
  font-style: normal;
  font-weight: 800;
  font-size: 32px;
  line-height: 44px;
  color:#fff;
  padding: 30px;
}
</style>

<script>
import HeaderMain from "../components/HeaderMain.vue"
  export default {
    name: 'Home',
    components:{HeaderMain},
  }
</script>