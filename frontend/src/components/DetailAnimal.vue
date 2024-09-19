<template>
  <div v-if="detailAnimalInfo" class="flex flex-col gap-3">
    <div>{{ detailAnimalInfo.name }}</div>
    <p v-html="detailAnimalInfo.description"></p>
  </div>
  <div v-else>Загрузка...</div>
</template>

<script setup lang="ts">
import { detailAnimal } from "@/services/api/red_book_entries";

const route = useRoute();
const detailAnimalInfo = ref(null);

onMounted(() => {
  detailAnimal(route.params.id).then(
    ({ data }) => (detailAnimalInfo.value = data)
  );
});
</script>
