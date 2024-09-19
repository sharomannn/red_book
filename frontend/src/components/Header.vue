<script setup lang="ts">
import DrawerNavigationMenu from "./DrawerNavigationMenu.vue";
import MenuIcon from "./MenuIcon.vue";
import ArrowIcon from "./ArrowIcon.vue";
import { useRouter } from "vue-router";

const showNavigationDrawer = ref(false);
const router = useRouter();

function navigateToMap(): void {
  router.push({ name: "Map" });
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

        <ElButton round color="#694DF9" @click="navigateToMap">
          <div class="flex gap-2 items-center">
            Карта Москвы
            <ElIcon> <ArrowIcon /> </ElIcon>
          </div>
        </ElButton>

        <Teleport to="body">
          <DrawerNavigationMenu v-model="showNavigationDrawer" />
        </Teleport></div
    ></el-container>
  </div>
</template>
