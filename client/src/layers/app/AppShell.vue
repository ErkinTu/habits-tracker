<script setup lang="ts">
import AppNavigation from '@/components/navigation/AppNavigation.vue'
import { useMotionTokens } from '@/composables/useMotionTokens'
import { useThemeTransitionSignal } from '@/composables/useThemeTransitionSignal'

const { themeMotionKey } = useThemeTransitionSignal()
const { routeContainer, themeFlash } = useMotionTokens()
</script>

<template>
  <div class="app-shell">
    <div
      :key="themeMotionKey"
      v-motion
      class="theme-motion-layer"
      :initial="themeFlash.initial"
      :enter="themeFlash.enter"
    />

    <div class="relative z-10 mx-auto flex min-h-dvh max-w-[1440px] md:pr-6">
      <AppNavigation class="shrink-0" />

      <main class="flex-1 px-4 pb-28 pt-6 md:px-8 md:pb-10 md:pt-10">
        <div class="mx-auto w-full max-w-5xl">
          <RouterView v-slot="{ Component, route }">
            <component
              :is="Component"
              :key="route.fullPath"
              v-motion
              :initial="routeContainer.initial"
              :enter="routeContainer.enter"
            />
          </RouterView>
        </div>
      </main>
    </div>
  </div>
</template>
