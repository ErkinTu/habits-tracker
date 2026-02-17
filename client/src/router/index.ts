import { createRouter, createWebHistory } from 'vue-router'

import AnalyticsView from '@/views/AnalyticsView.vue'
import HomeView from '@/views/HomeView.vue'
import MonthView from '@/views/MonthView.vue'
import SettingsView from '@/views/SettingsView.vue'
import WeekView from '@/views/WeekView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/week',
      name: 'week',
      component: WeekView,
    },
    {
      path: '/month',
      alias: ['/moonth'],
      name: 'month',
      component: MonthView,
    },
    {
      path: '/analytics',
      alias: ['/analitics'],
      name: 'analytics',
      component: AnalyticsView,
    },
    {
      path: '/settings',
      name: 'settings',
      component: SettingsView,
    },
  ],
})

export default router
