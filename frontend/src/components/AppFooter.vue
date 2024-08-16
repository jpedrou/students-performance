<template>
  <v-footer height="60" app class="d-flex align-center justify-center">
    <a
      v-for="item in items"
      :key="item.title"
      :href="item.href"
      :title="item.title"
      class="d-inline-block mx-2 social-link"
      rel="noopener noreferrer"
      target="_blank"
    >
      <v-icon :icon="item.icon" :size="item.icon === '$vuetify' ? 25 : 30" />
    </a>
  </v-footer>
</template>

<script setup>
const items = [
  {
    title: "GitHub",
    icon: `mdi-github`,
    href: "https://github.com/jpedrou",
  },
  {
    title: "LinkedIn",
    icon: `mdi-linkedin`,
    href: "https://www.linkedin.com/in/jpedroprofile/",
  },
];
</script>

<style scoped lang="sass">
.social-link :deep(.v-icon)
  color: rgba(var(--v-theme-on-background), var(--v-disabled-opacity))
  text-decoration: none
  transition: .2s ease-in-out

  &:hover
    color: rgba(25, 118, 210, 1)
</style>
