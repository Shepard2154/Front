<template>
    <div>
        <div class="header">
            <v-row class="header__data">
                    <p class="header__data__text">Департамент профессионального образования Томской области</p>
                    <p class="header__data__text">+ 7 (777)-777-77-77</p>
                    <p class="header__data__text">email@tomsk.ru</p>
            </v-row>
        </div>

        <div class="navbar">
            <v-row class="navbar__data">
                <v-row>
                    <v-col>
                        <h2 class="navbar__data__text-1">Профессиональное образование</h2>
                        <h2 class="navbar__data__text-2">Томской области</h2>
                    </v-col>
                </v-row>
                
                <h2 class="navbar__data__text-3">Личный кабинет</h2>
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

</style>

<script>
    export default {
        name: "Header",
    }
</script>