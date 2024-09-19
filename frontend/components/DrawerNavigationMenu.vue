<script setup lang="ts">
const { show } = defineProps<{
  show: boolean;
}>();

const emits = defineEmits<{
  (e: "update:show", flag: boolean): void;
}>();
</script>

<template>
  <ElDrawer
    title="КРАСНАЯ КНИГА"
    size="14%"
    direction="ltr"
    :with-header="false"
    :model-value="show"
    @close="emits('update:show', false)"
  >
    <div>
      <h2
        class="m-auto mb-4 px-6 py-4 text-[32px]/[38.4px] font-bold text-brand_blue"
      >
        КРАСНАЯ КНИГА
      </h2>
      <ElMenu>
        <ElMenuItem class="text-[14px]/[22.4px] text-text_main">
          <ElIcon class="text-inherit">
            <TableCellIcon />
          </ElIcon>
          <span> Активные обращения </span>
        </ElMenuItem>

        <ElMenuItem class="text-[14px]/[22.4px] text-text_main">
          <ElIcon class="text-inherit">
            <DocumentEditingIcon />
          </ElIcon>
          <span> Архив обращений </span>
        </ElMenuItem>

        <ElMenuItem class="text-[14px]/[22.4px] text-text_main">
          <ElIcon>
            <Phone />
          </ElIcon>
          <span> Журнал звонков </span>
        </ElMenuItem>

        <!-- <ElMenuItem
          :index="CALL_CENTER_ROUTE_NAMES.KNOWLEDGE_BASE"
          class="text-[14px]/[22.4px] text-text_main"
        >
          <ElIcon>
            <InfoOutlineIcon />
          </ElIcon>
          <span> База знаний </span>
        </ElMenuItem> -->

        <ElMenuItem class="text-[14px]/[22.4px] text-text_main">
          <ElIcon>
            <DataAnalysis />
          </ElIcon>
          <span> Статистика </span>
        </ElMenuItem>
      </ElMenu>
    </div>
  </ElDrawer>
</template>
