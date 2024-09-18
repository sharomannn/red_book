import { createResolver } from "@nuxt/kit";
const { resolve } = createResolver(import.meta.url);

export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  app: {
    // транзишион для паггесов  FIXMe
    pageTransition: { name: "page", mode: "out-in" },
    layoutTransition: { name: "layout", mode: "out-in" },
  },
  modules: [
    "@nuxtjs/eslint-module",
    "@pinia/nuxt",
    "@vueuse/nuxt",
    "vue-yandex-maps/nuxt",
    "@element-plus/nuxt",
  ],
  yandexMaps: {
    apikey: "409c07d0-9651-4cc8-8344-83e160f0263d",
  },
  components: [],

  imports: {
    dirs: [resolve("./stores"), "~/stores"],
  },
});
