<script setup lang="ts">
const { show } = defineProps<{
  show: boolean;
}>();

const emit = defineEmits<{
  (e: "close", flag: boolean): void;
}>();
</script>

<template>
  <el-drawer v-model="show" title="I am the title" direction="ltr">
    <template #header="{ close, titleId, titleClass }">
      <h4 :id="titleId" :class="titleClass">sosem!</h4>
      <el-icon
        :size="16"
        color="#606266"
        class="cursor-pointer"
        @click="emit('close', false)"
      >
        <Close />
      </el-icon>
    </template>
  </el-drawer>
</template>
