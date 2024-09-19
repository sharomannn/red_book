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
          <ElIcon class="text-inherit"> </ElIcon>
          <span> Все животные </span>
        </ElMenuItem>

        <ElMenuItem
          class="flex justify-center text-[14px]/[22.4px] text-text_main"
        >
          <ElIcon class="text-inherit"> </ElIcon>
          <span> Архив обращений </span>
        </ElMenuItem>

        <ElMenuItem
          class="flex justify-center text-[14px]/[22.4px] text-text_main"
        >
          <ElIcon> </ElIcon>
          <span> Журнал звонков </span>
        </ElMenuItem>
      </ElMenu>
    </div>
  </ElDrawer>
</template>
