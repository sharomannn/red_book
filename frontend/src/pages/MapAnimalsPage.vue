<script setup lang="ts">
import Header from "@/components/Header.vue";
import MapAnimals from "@/components/MapAnimals.vue";

</script>

<template>
  <div class="flex size-full flex-col gap-[2px] overflow-hidden">
    <Header />
    <MapAnimals ref="incidentMap" />
  </div>
</template>
