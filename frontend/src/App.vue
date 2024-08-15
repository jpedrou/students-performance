<template>
  <v-app>
    <AppBar />
    <v-main>
      <router-view />
    </v-main>
    <AppFooter />
  </v-app>
</template>

<script setup>
import AppBar from "./components/AppBar.vue";
import AppFooter from "./components/AppFooter.vue";
</script>

<style>
html {
  overflow: auto;
}

* {
  font-family: Poppins !important;
}
</style>
