<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function changeRoute(route_path) {
  console.log("Entrou aqui na função");
  router.push(route_path);
}
</script>

<template>
  <v-app-bar :elevation="2" class="app-bar">
    <v-app-bar-title class="text-center text-h4">Students Performance Prediction</v-app-bar-title>

    <template v-slot:append>
    </template>
  </v-app-bar>
</template>

<style scoped>
</style>
