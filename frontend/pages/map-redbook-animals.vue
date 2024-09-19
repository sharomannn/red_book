<script setup lang="ts">
import {
  YandexMap,
  YandexMapDefaultFeaturesLayer,
  YandexMapListener,
} from "vue-yandex-maps";
import type { YMap } from "@yandex/ymaps3-types";

const map = shallowRef<null | YMap>(null);
</script>

<template>
  <div>
    <yandex-map
      v-model="map"
      :settings="{
        location: {
          center: [37.617644, 55.755819],
          zoom: 9,
        },
      }"
    >
      <yandex-map-default-features-layer />
      <yandex-map-listener />
    </yandex-map>
    <ClientOnly />
  </div>
</template>
