<template>
    <div>
        <div class="wrap">
            <div class="navbar">
                <v-row class="navbar__data">
                    <v-row>
                        <v-col>
                            <h2 class="navbar__data__text-1">Мониторинг профессионального образования</h2>
                            <h2 class="navbar__data__text-2">Томской области</h2>
                        </v-col>
                    </v-row>
                    
                    <h2 class="navbar__data__text-3"></h2>
                </v-row>
            </div>

            <v-card class="navigation"
            style="border-radius: 20px;"
            elevation="8"
            raised>
                <router-link :to="{name: 'contingentAdmin'}" class="navigation__link">Контингент</router-link>  
                <router-link :to="{name: 'staffAdmin'}" class="navigation__link">Кадры</router-link>  
                <router-link :to="{name: 'commissionAdmin'}" class="navigation__link">Приемная комиссия</router-link>  
                <router-link :to="{name: 'reportsAdmin'}" class="navigation__link">Формирование отчетов</router-link>  
                <router-link :to="{name: 'propertyAdmin'}" class="navigation__link">Имущественный комплекс</router-link>  
            </v-card>
        </div>
        <v-container>
            <v-row class="content">
                <v-card class="filter
                raised"
                style="border-radius: 20px;">
                    <h2 class="filter__header">Фильтры поиска</h2>
                    <div>
                    <a class="filter__item" @click="pressed1 = !pressed1">Учебное заведение</a>
                        <transition name="fade">
                            <v-autocomplete v-if="pressed1" class="filter__select" :items="university"></v-autocomplete>           
                        </transition>
                    </div>
                    <br>
                    <br>
                    <div>
                        <a class="filter__item" @click="pressed2 = !pressed2">Специальность</a>
                        <transition name="fade">
                            <v-autocomplete v-if="pressed2" class="filter__select" :items="prof"></v-autocomplete>           
                        </transition>
                    </div>
                    <br>
                    <br>
                    <div>
                        <a class="filter__item" @click="pressed3 = !pressed3">Направление</a>
                        <transition name="fade">
                            <v-autocomplete v-if="pressed3" class="filter__select" :items="spec"></v-autocomplete>           
                        </transition>
                    </div>
                    <br>
                    <br>
                    <div>
                        <a class="filter__item" @click="pressed4 = !pressed4">Возраст</a>
                        <transition name="fade">
                            <v-text-field v-if="pressed4" class="filter__select" v-model="age" style="margin-left: 10px;"></v-text-field>           
                        </transition>
                    </div>
                    <br>
                    <br>
                    <div>
                        <a class="filter__item" @click="pressed5 = !pressed5">Регион</a>
                        <transition name="fade">
                            <v-autocomplete v-if="pressed5" class="filter__select" :items="regions"></v-autocomplete>           
                        </transition>
                    </div>
                    <br>
                    <br>
                    <div>
                        <a class="filter__item" @click="pressed6 = !pressed6">Военнообязанные</a>
                        <transition name="fade">
                            <v-checkbox v-if="pressed6" class="filter__select" label="Да"></v-checkbox>                      
                        </transition>
                        <transition name="fade">
                            <v-checkbox v-if="pressed6" class="filter__select" label="нет"></v-checkbox> 
                        </transition>
                    </div>
                   <br>
                    <br>
                    <div>
                        <a class="filter__item" @click="pressed7 = !pressed7">Особые категории</a>
                        <transition name="fade">
                            <v-checkbox v-if="pressed7" class="filter__select" label="Да"></v-checkbox>                      
                        </transition>
                        <transition name="fade">
                            <v-checkbox v-if="pressed7" class="filter__select" label="нет"></v-checkbox> 
                        </transition>
                    </div>
                    <br>
                    <br>
                    <div>
                        <a class="filter__item" @click="pressed8 = !pressed8">Трудоустройство</a>
                        <transition name="fade">
                            <v-checkbox v-if="pressed8" class="filter__select" label="Да"></v-checkbox>                      
                        </transition>
                        <transition name="fade">
                            <v-checkbox v-if="pressed8" class="filter__select" label="нет"></v-checkbox> 
                        </transition>
                    </div>
                    <br>
                    <br>
                    <v-btn color="#4244A6"
                    style="color: white"
                    @click="getData"
                    >Поиск</v-btn>
                </v-card>

                <v-card class="main-content"
                style="border-radius: 20px; height: 100%">
                <v-data-table
                    class="data-table"
                    item-key="name"
                    hide-default-footer
                    v-if="loaded"
                    :headers="headers"
                    :items="tableItems"
                    :page.sync="page"
                    :items-per-page="10"
                    :search="search"
                >
                </v-data-table>

                <v-pagination
                    class="pagination"
                    color="#EDAC48"
                    v-model="page"
                    :length="pageCount"
                ></v-pagination>
                </v-card>
            </v-row>
        </v-container>
    </div>
</template>

<style scoped>
    .wrap {
        display: flex;
        align-items: center;
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
        width: 525px;
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

    .navigation {
        display: flex;
        justify-content: space-evenly;
        width: 900px;
        height: 65px;
        padding: 21px;
        box-shadow: 2px 0px 30px rgba(128, 128, 128, 0.2), 0px 2px 30px rgba(128, 128, 128, 0.05);
        border-radius: 20px;
        margin-right: 100px;
    }

    .navigation__link {
        text-decoration: none;
        font-family: Nunito;
        font-style: normal;
        font-weight: 600;
        font-size: 14px;
        line-height: 19px;
        color: #6A6A6A;
    }

    .filter {
        width: 323px;
        height: 820px;
        padding: 20px;
        align-items: baseline;
        border-radius: 30px;
        box-shadow: 2px 0px 30px rgba(128, 128, 128, 0.2), 0px 2px 30px rgba(128, 128, 128, 0.05);
    }

    .filter__header {
        font-family: Nunito;
        color: #4244A6;
        text-align: center;
    }

    .filter__item {
        text-decoration: none;
        font-family: Nunito;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 25px;
        color: #8B8B8B;
    }

    .filter__select {
        max-height: 5px;
        top: -10px;
    }

    .main-content {
        width: 1327px;
        height: 624px;
        box-shadow: 2px 0px 30px rgba(128, 128, 128, 0.2), 0px 2px 30px rgba(128, 128, 128, 0.05);
    }

    .content {
        display: flex;
        justify-content: space-between;
    }

    .active {
        color: #4244A6;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }

    .fade-enter, .fade-leave-to {
        opacity: 0;
    }
</style>

<script>
    export default {
        name: "CabinetAdmin",
        data: () => ({
            loaded: false,
            search: "",
            page: 1,
            pageCount: 0,

            pressed1: false,
            pressed2: false,
            pressed3: false,
            pressed4: false,
            pressed5: false,
            pressed6: false,
            pressed7: false,
            pressed8: false,
            
            univerFilter: "",
            specFilter: "",
            profFilter: "",
            ageFilter: "",
            regionFilter: "",

            university: [],
            spec: [],
            prof: [],
            age: "2001-1-1 ~ 2002-1-1",
            regions: [],

            search: '',
            page: 1,
            pageCount: 0,
            headers: [],
            tableItems: [],
            headers: [
                { text: 'Фамилия', align: 'start', sortable: false, value: 'lastname'},
                { text: 'Имя', value: 'name'},
                { text: 'Отчество', value: 'fathername'},
                { text: 'Дата рождения', value: 'birthdate'},
                { text: 'Паспорт', value: 'passport'},
                { text: 'Телефон', value: 'phone'},
                { text: 'Регион', value: 'region'},
                { text: 'Колледж', value: 'colledge_name'},
                { text: 'Курс', value: 'current_curse'},
                { text: 'Направление', value: 'spec_name'},
                { text: 'Специальность', value: 'prof_name'},
                { text: 'Ср. балл аттестата', value: 'att_score'},
                { text: 'Инвалидность', value: 'is_disabled'},
                { text: 'Сирота', value: 'is_orphan'},
                { text: 'Служил', value: 'is_served'},
                { text: 'Нуждается в жилище', value: 'needs_home'},
                { text: 'После 11 класса', value: 'is_higher'},
                { text: 'Академический отпуск', value: 'academ_duration'},
                { text: 'Дата поступления', value: 'receipt_date'},
                { text: 'Дата выпуска', value: 'study_end'},
                ]
            }),

        methods: {
            press() {
                console.log("pressed!")
            },

           async getFilters() {
            await axios.get(`${this.$store.state.backendUrl}/params/direction/`
                    ).then(response => {
                        for(let i=0; i<response.data.length; i++) {
                            if (response.data[i]["colledge_name"] != null) this.university.push(response.data[i]["colledge_name"])
                            if (response.data[i]["spec_name"] != null) this.spec.push(response.data[i]["spec_name"])
                            if (response.data[i]["prof_name"] != null) this.prof.push(response.data[i]["prof_name"])
                        }
                    })

            await axios.get(`${this.$store.state.backendUrl}/student/all/?birthdate_after=2001-1-1&birthdate_before=2002-1-1`
                    ).then(response => {
                        for(let i=0; i<response.data.length; i++) {
                            if (response.data[i]["region"] != null) this.regions.push(response.data[i]["region"])
                        }
                    })
            },

            async getData() {
                await axios.get(`${this.$store.state.backendUrl}/student/all/`
                    ).then(response => {
                        console.log(response.data.results[0])
                        for(let i=0; i<response.data.results.length; i++) {
                            let student = 
                                {
                                    "name": response.data.results[i]["name"],
                                    "lastname": response.data.results[i]["lastname"],
                                    "fathername": response.data.results[i]["fathername"],
                                    "current_curse": response.data.results[i]["current_curse"],
                                    "study_end": response.data.results[i]["study_end"],
                                    "birthdate": response.data.results[i]["birthdate"],
                                    "passport": response.data.results[i]["passport"],
                                    "phone": response.data.results[i]["phone"],
                                    "region": response.data.results[i]["region"],
                                    "att_score": response.data.results[i]["att_score"],
                                    "is_disabled": response.data.results[i]["is_disabled"],
                                    "is_orphan": response.data.results[i]["is_orphan"],
                                    "is_served": response.data.results[i]["is_served"],
                                    "needs_home": response.data.results[i]["needs_home"],
                                    "is_higher": response.data.results[i]["is_higher"],
                                    "academ_duration": response.data.results[i]["academ_duration"],
                                    "receipt_date": response.data.results[i]["receipt_date"],
                                    "spec_name": response.data.results[i]["spec_name"],
                                    "prof_name": response.data.results[i]["prof_name"],
                                    "colledge_name": response.data.results[i]["colledge_name"],
                                    "base_study_time": response.data.results[i]["base_study_time"],
                                    "short_study_time": response.data.results[i]["short_study_time"]
                                }
                                console.log(student)
                            this.tableItems.push(student)
                        }
                        this.loaded = true
                        this.pageCount = response.data["count"]
                    })
            }                
        },

        created(){
            this.getFilters()
        },

        // computed: {
        //     university: function() {
        //         return 
        //     }
        // }
    }
</script>