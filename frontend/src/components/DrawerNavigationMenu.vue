<script setup lang="ts">
const { modelValue } = defineProps<{
  modelValue: boolean;
}>();

const emits = defineEmits<{
  (e: "update:modelValue", flag: boolean): void;
}>();
</script>

<template>
  <ElDrawer
    title="КРАСНАЯ КНИГА"
    size="360"
    direction="ltr"
    :with-header="false"
    :model-value="modelValue"
    @close="emits('update:modelValue', false)"
  >
    <div class="flex flex-col items-center">
      <h2 class="px-6 py-4 text-[32px]/[38.4px] text-brand_blue">
        КРАСНАЯ КНИГА
      </h2>
      <h3>Москва</h3>
      <ElMenu class="w-full">
        <ElMenuItem
          class="flex justify-center text-[14px]/[22.4px] text-text_main"
        >
          <router-link :to="{ name: 'AllAnimal' }"
            ><ElIcon class="text-inherit"> </ElIcon>
            <span> Все животные </span></router-link
          >
        </ElMenuItem>

        <ElMenuItem
          class="flex justify-center text-[14px]/[22.4px] text-text_main"
        >
          <router-link :to="{ name: 'Home' }">
            <ElIcon class="text-inherit"> </ElIcon>
            <span> Главная страница </span>
          </router-link>
        </ElMenuItem>

        <ElMenuItem
          class="flex justify-center text-[14px]/[22.4px] text-text_main"
        >
          <router-link :to="{ name: 'Auth' }">
            <ElIcon> </ElIcon>
            <span> Авторизация </span>
          </router-link>
        </ElMenuItem>
      </ElMenu>
    </div>
  </ElDrawer>
</template>
