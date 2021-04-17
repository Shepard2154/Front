<template>
    <div>
      <Header />
      <v-container>
        <NavbarCabinet />
        <router-view />
      </v-container>
    </div>
</template>

<style scoped>

</style>

<script>
  import Header from "../components/Header.vue" 
  import NavbarCabinet from '../components/NavbarCabinet.vue'
  
  export default {
    name: 'Cabinet',
    components: {
      Header,
      NavbarCabinet
    }
  }
</script>