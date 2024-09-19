<script setup lang="ts">
import {
  LCircleMarker,
  LControlZoom,
  LIcon,
  LMap,
  LMarker,
  LPopup,
  LTileLayer,
  LTooltip,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import { map } from "@/services/api";

const entries = ref();
const center = ref<[number, number] | []>([]);

const zoom = ref(6);
const mapComponent = ref<HTMLElement | null>();

function setMapCenter(latitude: string | number, longitude: string | number) {
  if (!+latitude || !+longitude) return;

  center.value = [+latitude, +longitude];
}
async function getAllCoordinates() {
  try {
    const { data } = await map.getRedBookEntries();
    entries.value = data;
  } catch (e) {
    console.error(e);
  }
}

onBeforeMount(async () => {
  entries.value = await getAllCoordinates();

  if (entries.value) {
    zoom.value = 12;
    await nextTick();
    setMapCenter();
  }
});
</script>

<template>
  <LMap
    v-if="center.length === 2"
    ref="mapComponent"
    :zoom="zoom"
    :use-global-leaflet="true"
    :center="center"
    @update:center="updateCenter"
    @update:zoom="updateZoom"
  >
    <LTileLayer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      layer-type="base"
      name="OpenStreetMap"
    />
    <LControlZoom position="topright" />
  </LMap>
</template>

<style lang="scss">
.leaflet-bottom {
  display: none;
}

.leaflet-touch .leaflet-control-layers,
.leaflet-touch .leaflet-bar {
  display: none;
}

.leaflet-touch .leaflet-control-layers,
.leaflet-touch .leaflet-bar {
  display: none;
}
</style>
