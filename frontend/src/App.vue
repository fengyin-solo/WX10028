<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">桥梁健康监测管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向传感器布设、应变监测、振动监测、索力监测、裂缝巡检、定期检测、评定报告与维修加固的一体化桥梁健康监测管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "桥梁台账", path: "/bridge" }, { label: "传感器管理", path: "/sensor" }, { label: "应变监测", path: "/strain" }, { label: "振动监测", path: "/vibration" }, { label: "索力监测", path: "/cable_force" }, { label: "挠度监测", path: "/deflection" }, { label: "裂缝巡检", path: "/crack" }, { label: "锈蚀检测", path: "/corrosion" }, { label: "定期检测", path: "/routine_check" }, { label: "评定报告", path: "/assessment" }, { label: "维修加固", path: "/repair" }, { label: "支座管理", path: "/bearing" }, { label: "锚碇锚固管理", path: "/anchor" }, { label: "交通荷载监测", path: "/traffic_monitor" }, { label: "预应力监测", path: "/tendon" }, { label: "应急处置", path: "/emergency" }]
</script>
