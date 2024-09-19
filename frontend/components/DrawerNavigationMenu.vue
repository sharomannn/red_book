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
          <ElIcon class="text-inherit">
            <TableCellIcon />
          </ElIcon>
          <span> Активные обращения </span>
        </ElMenuItem>

        <ElMenuItem
          class="flex justify-center text-[14px]/[22.4px] text-text_main"
        >
          <ElIcon class="text-inherit">
            <DocumentEditingIcon />
          </ElIcon>
          <span> Архив обращений </span>
        </ElMenuItem>

        <ElMenuItem
          class="flex justify-center text-[14px]/[22.4px] text-text_main"
        >
          <ElIcon>
            <Phone />
          </ElIcon>
          <span> Журнал звонков </span>
        </ElMenuItem>
      </ElMenu>
    </div>
  </ElDrawer>
</template>

<style scoped lang="scss">
.el-menu {
  border-right: 0;
}

.el-sub-menu__title {
  padding-right: 0;
}

:deep(.el-menu .el-sub-menu__title .el-sub-menu__icon-arrow) {
  position: initial;
  margin-top: 2px;
  margin-left: 8px;

  svg {
    width: 16px;
    height: 16px;
  }
}

:deep(.el-menu .el-menu-item [class^="el-icon"]) {
  margin-right: 8px;
}

:deep(.el-menu .el-menu-item-group__title) {
  display: none;
}
</style>
