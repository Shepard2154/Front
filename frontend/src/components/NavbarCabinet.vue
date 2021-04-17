<template>
    <div class="main-container">
        <nav class="navigation">
            <router-link :to="{name: 'questionary'}" class="navigation__link">Анкета</router-link>
            <router-link :to="{name: 'statements'}" class="navigation__link">Заявления</router-link>
            <router-link :to="{name: 'documents'}" class="navigation__link">Подача документов</router-link>
            <router-link :to="{name: 'favorites'}" class="navigation__link">Избранное</router-link>
            <router-link :to="{name: 'ask'}" class="navigation__link">Задать вопрос</router-link>
        </nav>
    </div>
</template>

<style scoped>
    .main-container {
        display: flex;
        justify-content: center;
    }

    .navigation {
        display: flex;
        justify-content: space-around;
        width: 1000px;
        background-color: #4244A6;
        border: 1px solid #4244A6;
        border-radius: 50px;
    }

    .navigation__link {
        text-decoration: none;
        font-family: Manrope;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 25px;
        color: white;
        padding: 24px;
        border-radius: 50px;
    }

    .active {
        color: #4244A6;
        background-color: white;
    }
</style>

<script>
export default{
    name: "NavbarCabinet"
}
</script>
