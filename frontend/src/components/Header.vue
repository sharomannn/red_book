<script setup lang="ts">
import DrawerNavigationMenu from "./DrawerNavigationMenu.vue";
import MenuIcon from "./MenuIcon.vue";
import ArrowIcon from "./ArrowIcon.vue";
import { useMap } from "@/utils/map";
import { useRoute, useRouter } from "vue-router";

const showNavigationDrawer = ref(false);
const route = useRoute();
const router = useRouter();

const map = useMap();

const isMapPage = computed(() => route.name === "AnimalsMap");

function navigateToAllAnimal() {
  router.push({ name: "AllAnimal" });
}

function openMap() {
  map.open();
}
</script>

<template>
  <div class="shadow-xl">
    <el-container class="flex size-full flex-col gap-4 bg-bg_main p-4">
      <div class="flex h-[4vh] w-full items-center justify-between">
        <div class="flex items-center">
          <ElButton link @click="showNavigationDrawer = true"
            ><MenuIcon
          /></ElButton>
        </div>

        <div class="flex flex-col items-center">
          <h2 class="py-1 text-[32px]/[38.4px] text-brand_blue">
            КРАСНАЯ КНИГА
          </h2>
          <h2>Москва</h2>
        </div>

        <ElButton v-if="!isMapPage" round color="#694DF9" @click="openMap">
          <div class="flex gap-2 items-center">
            Карта Москвы
            <ElIcon> <ArrowIcon /> </ElIcon>
          </div>
        </ElButton>
        <ElButton v-else round color="#694DF9" @click="navigateToAllAnimal">
          <div class="flex gap-2 items-center">
            Все краснокнижные животные
            <ElIcon> <ArrowIcon /> </ElIcon>
          </div>
        </ElButton>

        <Teleport to="body">
          <DrawerNavigationMenu v-model="showNavigationDrawer" />
        </Teleport></div
    ></el-container>
  </div>
</template>
