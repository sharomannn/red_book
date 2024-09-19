<template>
  <el-header>
    <Header />
  </el-header>
  <el-container class="flex size-full flex-col gap-4 bg-bg_main p-4">
    <router-view></router-view>
  </el-container>
</template>

<script setup lang="ts">
import Header from "@/components/Header.vue";
</script>
