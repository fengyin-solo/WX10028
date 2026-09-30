import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Bridge = () => import('@/views/bridge/index.vue')
const Sensor = () => import('@/views/sensor/index.vue')
const Strain = () => import('@/views/strain/index.vue')
const Vibration = () => import('@/views/vibration/index.vue')
const CableForce = () => import('@/views/cable_force/index.vue')
const Deflection = () => import('@/views/deflection/index.vue')
const Crack = () => import('@/views/crack/index.vue')
const Corrosion = () => import('@/views/corrosion/index.vue')
const RoutineCheck = () => import('@/views/routine_check/index.vue')
const Assessment = () => import('@/views/assessment/index.vue')
const Repair = () => import('@/views/repair/index.vue')
const Bearing = () => import('@/views/bearing/index.vue')
const Anchor = () => import('@/views/anchor/index.vue')
const TrafficMonitor = () => import('@/views/traffic_monitor/index.vue')
const Tendon = () => import('@/views/tendon/index.vue')
const Emergency = () => import('@/views/emergency/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/bridge', name: 'bridge', component: Bridge },
    { path: '/sensor', name: 'sensor', component: Sensor },
    { path: '/strain', name: 'strain', component: Strain },
    { path: '/vibration', name: 'vibration', component: Vibration },
    { path: '/cable_force', name: 'cable_force', component: CableForce },
    { path: '/deflection', name: 'deflection', component: Deflection },
    { path: '/crack', name: 'crack', component: Crack },
    { path: '/corrosion', name: 'corrosion', component: Corrosion },
    { path: '/routine_check', name: 'routine_check', component: RoutineCheck },
    { path: '/assessment', name: 'assessment', component: Assessment },
    { path: '/repair', name: 'repair', component: Repair },
    { path: '/bearing', name: 'bearing', component: Bearing },
    { path: '/anchor', name: 'anchor', component: Anchor },
    { path: '/traffic_monitor', name: 'traffic_monitor', component: TrafficMonitor },
    { path: '/tendon', name: 'tendon', component: Tendon },
    { path: '/emergency', name: 'emergency', component: Emergency },
  ],
})

export default router
