<template>
  <div>
    <h2 class="px-6 py-4 text-[32px]/[38.4px] text-brand_blue">
      Все краснокнижные животные
    </h2>
  </div>
  <div class="flex flex-col gap-4">
    <div><el-input placeholder="Введите животное" /></div>
    <div class="flex gap-2">
      <div class="w-[200px]">
        <p>Категория</p>
        <el-select></el-select>
      </div>
      <div class="w-[200px]">
        <p>Статус</p>
        <el-select></el-select>
      </div>
    </div>
  </div>
  <div class="grid grid-cols-4 gap-2">
    <AnimalCard v-for="nub of 5" />
  </div>
</template>

<script setup lang="ts">
import AnimalCard from "@/components/AnimalCard.vue";
</script>
