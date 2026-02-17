<script setup lang="ts">
import { Icon } from '@iconify/vue'
import { UseDark } from '@vueuse/components'

import { useMotionTokens } from '@/composables/useMotionTokens'
import { useNavigation } from '@/composables/useNavigation'
import { useThemeTransitionSignal } from '@/composables/useThemeTransitionSignal'

const { items } = useNavigation()
const { triggerThemeMotion } = useThemeTransitionSignal()
const { tapAction } = useMotionTokens()

const onToggleTheme = (toggleDark: () => void) => {
  toggleDark()
  triggerThemeMotion()
}
</script>

<template>
  <aside class="navigation-surface hidden md:flex md:w-56 md:flex-col md:border-r md:px-4 md:py-5 md:backdrop-blur">
    <div class="flex items-center justify-between gap-2">
      <div>
        <p class="text-[11px] font-semibold uppercase tracking-[0.24em] text-[color:var(--text-muted)]">Habits</p>
        <h1 class="mt-1 text-lg font-semibold text-[color:var(--text-primary)]">Daily Rhythm</h1>
      </div>

      <UseDark
        v-slot="{ isDark, toggleDark }"
        selector="html"
        attribute="data-theme"
        value-dark="dark"
        value-light="light"
        :disable-transition="false"
        storage-key="habits-theme-mode"
      >
        <button
          v-motion
          class="theme-toggle"
          type="button"
          :initial="tapAction.initial"
          :hovered="tapAction.hovered"
          :tapped="tapAction.tapped"
          @click="onToggleTheme(toggleDark)"
        >
          <Icon :icon="isDark ? 'mdi:white-balance-sunny' : 'mdi:moon-waning-crescent'" class="h-5 w-5" />
        </button>
      </UseDark>
    </div>

    <nav class="mt-5 flex flex-col gap-1.5">
      <RouterLink
        v-for="item in items"
        :key="item.to"
        :to="item.to"
        class="nav-item flex w-full items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium"
        :class="item.isActive ? 'nav-item-active' : ''"
      >
        <Icon :icon="item.icon" class="h-5 w-5 shrink-0" />
        <span>{{ item.label }}</span>
      </RouterLink>
    </nav>

    <div class="mt-auto pt-4">
      <button class="user-card" type="button">
        <span class="user-avatar">ER</span>
        <span class="flex flex-col text-left">
          <span class="text-sm font-semibold text-[color:var(--text-primary)]">Erkin</span>
          <span class="text-xs text-[color:var(--text-secondary)]">Habit Builder</span>
        </span>
      </button>
    </div>
  </aside>

  <nav
    class="navigation-surface fixed inset-x-0 bottom-0 z-30 border-t px-2 pb-[calc(env(safe-area-inset-bottom)+0.5rem)] pt-2 backdrop-blur md:hidden"
  >
    <ul class="grid grid-cols-5 gap-1">
      <li v-for="item in items" :key="item.to">
        <RouterLink
          :to="item.to"
          class="nav-item flex w-full flex-col items-center gap-1 rounded-xl px-1 py-2 text-[11px] font-medium"
          :class="item.isActive ? 'nav-item-active' : ''"
        >
          <Icon :icon="item.icon" class="h-[18px] w-[18px]" />
          <span class="truncate">{{ item.label }}</span>
        </RouterLink>
      </li>
    </ul>
  </nav>
</template>
