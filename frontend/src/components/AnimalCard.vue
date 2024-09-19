<template>
  <el-card>
    <div>
      <img :src="props.data.image" alt="" />
    </div>
    <div class="flex flex-col gap-2">
      <h3>{{ props.data.name }}</h3>
      <div>Семейство: {{ props.data.family.name }}</div>
      <p>Отряд: {{ props.data.order.name }}</p>
      <router-link
        :to="{ name: 'DetailAnimal', params: { id: props.data.id } }"
      >
        <el-link type="primary"> Подробная информация </el-link>
      </router-link>
    </div>
  </el-card>
</template>

<script setup lang="ts">
interface Animal {
  id: number;
  order: Family;
  family: Family;
  order_id: number;
  family_id: number;
  name: string;
  latin_name: string;
  category: string;
  description: string;
  image: string;
  public: boolean;
  section: number;
  sector: number[];
}

interface Family {
  id: number;
  name: string;
  description: null;
  order?: number;
}

const props = defineProps<{
  data: Animal;
}>();
</script>
