import { computed } from 'vue'
import { useRoute } from 'vue-router'

export type NavigationItem = {
  label: string
  to: string
  icon: string
}

const navigationItems: NavigationItem[] = [
  { label: 'Home', to: '/', icon: 'mdi:home-variant-outline' },
  { label: 'Week', to: '/week', icon: 'mdi:calendar-week-outline' },
  { label: 'Month', to: '/month', icon: 'mdi:calendar-month-outline' },
  { label: 'Analytics', to: '/analytics', icon: 'mdi:chart-line' },
  { label: 'Settings', to: '/settings', icon: 'mdi:cog-outline' },
]

export const useNavigation = () => {
  const route = useRoute()

  const items = computed(() =>
    navigationItems.map((item) => ({
      ...item,
      isActive: route.path === item.to,
    })),
  )

  return {
    items,
  }
}
