<script setup lang="ts">
import { ModalsContainer } from 'vue-final-modal'
</script>

<template>
  <RouterView />
  <ModalsContainer />
</template>

<style lang="scss">
.el-select__wrapper {
  border-radius: 50px !important;
  color: #f5f5f5 !important;
  padding: 12px 20px !important;
  background-color: #a2a2a233 !important;
}

.el-input {
  border-radius: 50px !important;
  background-color: #a2a2a233 !important;
  color: #f5f5f5 !important;
  max-height: 37px !important;
}

.el-input__wrapper {
  border-radius: 50px !important;
}

.el-divider--horizontal {
  margin: 10px 0 !important;
  border-color: #A2A2A266 !important;
}

.el-input-number {
  width: 100% !important;
  position: relative;
}

.el-input-number span {
  background-color: transparent !important;
  position: absolute;
  top: 13px;
}

.el-input-number .el-input-number__decrease {
  left: auto !important;
  right: 40px;
  border-radius: 50% !important;
  height: 10px !important;
  width: 10px !important;
  color: rgb(141, 144, 149);
}

.el-input-number .el-input-number__increase {
  border-radius: 50% !important;
  height: 10px !important;
  width: 10px !important;
  right: 19px;
  color: rgb(141, 144, 149);
}

.el-input-number .el-input__wrapper {
  padding-left: 16px !important;
  padding-right: 64px !important;
}

.el-input-number .el-input__inner {
  text-align: left !important;
}
</style>
