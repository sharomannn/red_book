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
    "@nuxt/ui",
    "vue-yandex-maps/nuxt",
  ],
  yandexMaps: {
    apikey: "409c07d0-9651-4cc8-8344-83e160f0263d",
  },
  components: [
    {
      prefix: "Layout",
      path: resolve("./components/layouts"),
      global: true,
    },
    {
      prefix: "Awesome",
      path: resolve("./components/awesome"),
      global: true,
    },
  ],

  imports: {
    dirs: [resolve("./stores"), "~/stores"],
  },
});
