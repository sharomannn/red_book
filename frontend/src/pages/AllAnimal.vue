<template>
  <div>
    <h2 class="px-6 py-4 text-[32px]/[38.4px] text-brand_blue">
      Все краснокнижные животные
    </h2>
  </div>
  <div class="flex flex-col gap-4">
    <div>
      <el-input
        v-model="filter.name"
        placeholder="Введите животное"
        @input="getAnimals(filter)"
      />
    </div>
    <div class="flex gap-2">
      <div class="w-[250px]">
        <p>Категория</p>
        <el-select v-model="filter.category" @change="getAnimals(filter)">
          <el-option
            v-for="category of categoryes"
            :key="category.id"
            :value="category.id"
            :label="category.label"
          />
        </el-select>
      </div>
      <!-- <div class="w-[250px]">
        <p>Статус</p>
        <el-select></el-select>
      </div> -->
    </div>
  </div>
  <div class="grid grid-cols-4 gap-2">
    <AnimalCard v-for="animal of allAnimals" :data="animal" />
  </div>
</template>

<script setup lang="ts">
import AnimalCard from "@/components/AnimalCard.vue";
import { getAnimals } from "@/services/api/red_book_entries";

const categoryes = [
  { id: 1, label: "Вымирающие виды" },
  { id: 2, label: "Уязвимые виды" },
  { id: 3, label: "Редкие виды" },
  { id: 4, label: "Неопределенные виды" },
  { id: 5, label: "Восстанавливающиеся виды" },
];

const filter = ref({
  category: null,
  name: "",
});

const allAnimals = ref([]);

onMounted(() => {
  getAnimals(filter.value).then(({ data }) => {
    allAnimals.value = data;
  });
});
</script>
