<script setup lang="ts">
import DrawerNavigationMenu from "./DrawerNavigationMenu.vue";

const showNavigationDrawer = ref(false);
// const item = {
//   date: "2016-05-02",
//   name: "Tom",
//   address: "No. 189, Grove St, Los Angeles",
// };
// const tableData = ref(Array.from({ length: 20 }).fill(item));
</script>

<template>
  <div>
    <div class="flex h-[4vh] w-full items-center justify-between">
      <div class="flex items-center">
        <ElIcon
          size="32"
          icon="  "
          class="my-[3px] mr-4 cursor-pointer"
          @click="showNavigationDrawer = true"
        />
        {{ showNavigationDrawer }}
        <ElLink :underline="false" @click="">
          <h1 class="mr-6 text-[32px]/[38.4px] font-bold text-brand_blue">
            КРАСНАЯ КНИГА
          </h1>
        </ElLink>
      </div>

      <div class="flex items-center justify-center gap-2">
        <ElButton ref="buttonRef" size="small" round> </ElButton>
      </div>

      <Teleport to="body">
        <DrawerNavigationMenu v-model:show="showNavigationDrawer" />
      </Teleport>
    </div>
  </div>
</template>
