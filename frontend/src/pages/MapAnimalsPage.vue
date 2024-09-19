<script setup lang="ts">
import {
  LCircleMarker,
  LControlZoom,
  LIcon,
  LMap,
  LMarker,
  LPopup,
  LTileLayer,
  // LTooltip,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";

const zoom = ref(6);
const center = ref();
const map = ref<HTMLElement | null>();

function zoomPlus() {
  zoom.value++;
}

function zoomMinus() {
  zoom.value -= 1;
}
</script>

<template>
  <LMap ref="map" :zoom="zoom" :use-global-leaflet="true" :center="center">
    <LTileLayer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      layer-type="base"
      name="OpenStreetMap"
    />
    <LControlZoom position="topright" />  
  </LMap>
  <div
    class="relative right-[-96vw] top-[-50vh] flex size-0 flex-col gap-3"
    style="z-index: 1000"
  >
    <ElButton circle class="shadow-lg" @click="zoomPlus">
      <ElIcon :size="14" color="#000000">
        <Plus />
      </ElIcon>
    </ElButton>
    <ElButton circle class="shadow-lg" @click="zoomMinus">
      <ElIcon :size="14" color="#000000">
        <Minus />
      </ElIcon>
    </ElButton>
  </div>
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

.leaflet-container a.leaflet-popup-close-button {
  display: none;
}

.leaflet-marker-icon.leaflet-interactive,
.leaflet-image-layer.leaflet-interactive,
.leaflet-pane > svg path.leaflet-interactive,
svg.leaflet-image-layer.leaflet-interactive path {
  background: none;
  border: none;
}

.leaflet-popup-content p {
  margin: 0 0 2px 0;
}

.leaflet-popup.leaflet-zoom-animated {
  bottom: -25px !important;
  left: auto !important;
  right: -10px !important;
}

.leaflet-popup-content-wrapper {
  border-radius: 16px 16px 0 16px;
}

.leaflet-popup-tip {
  display: none;
}

.marker-cluster-small div {
  background-color: #ffffff;
}
</style>
