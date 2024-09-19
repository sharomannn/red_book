import type { RouteRecordRaw } from "vue-router";
import MainPage from "../pages/MainPage.vue";
import AuthPage from "../pages/AuthPage.vue";
import HomePage from "../pages/HomePage.vue";
import AllAnimal from "@/pages/AllAnimal.vue";

const routes: readonly RouteRecordRaw[] = [
  {
    path: "/auth",
    name: "Auth",
    component: AuthPage,
    meta: {
      title: "auth",
    },
  },
  {
    path: "/",
    name: "Main",
    component: MainPage,
    redirect: "/home",
    children: [
      { path: "/home", name: "Home", component: HomePage },
      { path: "/all", name: "AllAnimal", component: AllAnimal },
    ],
  },
];

export default routes;
