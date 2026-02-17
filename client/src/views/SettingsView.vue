<script setup lang="ts">
import ThemeControls from '@/components/settings/ThemeControls.vue'
import { useMotionTokens } from '@/composables/useMotionTokens'

const { sectionHeader, subtleBounce } = useMotionTokens()
</script>

<template>
  <section class="space-y-6">
    <header v-motion :initial="sectionHeader.initial" :enter="sectionHeader.enter">
      <p class="page-eyebrow">Profile</p>
      <h2 class="page-title">Settings</h2>
      <p class="page-subtitle">Manage account, style preferences, and reminder defaults.</p>
    </header>

    <div v-motion :initial="subtleBounce(70).initial" :enter="subtleBounce(70).enter">
      <ThemeControls />
    </div>

    <article v-motion class="panel-card p-5" :initial="subtleBounce(120).initial" :enter="subtleBounce(120).enter">
      <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Profile Card</h3>
      <p class="mt-2 text-sm text-[color:var(--text-secondary)]">
        Placeholder for avatar, username, notifications, and timezone settings.
      </p>
    </article>
  </section>
</template>
