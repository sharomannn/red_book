<script setup lang="ts">
import Header from "~/components/Header.vue";
</script>

<template>
  <el-header>
    <Header />
  </el-header>
  <el-container class="flex size-full flex-col gap-4 bg-bg_main p-4">
    <div class="flex flex-col">
      <div class="flex justify-between my-[50px]">
        <div class="w-[50%]">
          <h1 class="px-6 py-4 text-[32px]/[38.4px] text-brand_blue">
            КРАСНАЯ КНИГА
          </h1>
          <p class="px-6 text-[18px]/[29px] text-brand_blue">
            Безусловно, внедрение современных методик обеспечивает широкому
            кругу (специалистов) участие в формировании первоочередных
            требований. Банальные, но неопровержимые выводы, а также действия
            представителей оппозиции преданы социально-демократической анафеме.
            Для современного мира дальнейшее развитие различных форм
            деятельности предопределяет высокую востребованность новых
            предложений.
          </p>
        </div>
        <div class="w-full max-w-[50%]">
          <img
            src="../assets/animal.jpg"
            alt=""
            class="w-full rounded-[60px]"
          />
        </div>
      </div>
      <div>
        <h2 class="px-6 py-4 text-[32px]/[38.4px] text-brand_blue">
          Интерактивная карта краснокнижных животных
        </h2>
      </div>
    </div>
  </el-container>
</template>

<style>
.el-header {
  padding: 0;
}
</style>
