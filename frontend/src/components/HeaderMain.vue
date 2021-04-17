<template>
    <div>
        <div class="header">
            <v-row class="header__data">
                    <p class="header__data__text">Департамент профессионального образования Томской области</p>
                    <p class="header__data__text">+ 7 (777)-777-77-77</p>
                    <p class="header__data__text">email@tomsk.ru</p>
                    <v-btn class='login' plain>Личный кабинет</v-btn>
            </v-row>
        </div>
    </div>
</template>

<style scoped>
    .header {
        height: 59px;
        background: #F0F5FF;
        align-items: center;
        display: flex;
    }

    .header__data {
        justify-content: space-evenly;
    }

    .header__data__text {
        color: #6A6A6A;
    }

    .navbar {
        display: flex;
        padding: 60px;
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
    .login{
        border: 2px solid #4244A6;
        box-sizing: border-box;
        border-radius: 20px;
        font-family: Manrope;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 25px;

        /* identical to box height */

        color: #4244A6;
    }

</style>

<script>
    export default {
        name: "Header",
    }
</script>