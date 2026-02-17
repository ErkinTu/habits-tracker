<script setup lang="ts">
import { useMotionTokens } from '@/composables/useMotionTokens'

const { sectionHeader, subtleBounce } = useMotionTokens()
</script>

<template>
  <section class="space-y-6">
    <header v-motion :initial="sectionHeader.initial" :enter="sectionHeader.enter">
      <p class="page-eyebrow">Period</p>
      <h2 class="page-title">Week</h2>
      <p class="page-subtitle">Weekly board with progress by day.</p>
    </header>

    <article v-motion class="panel-card min-h-72 p-5" :initial="subtleBounce(80).initial" :enter="subtleBounce(80).enter">
      <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Week Grid</h3>
      <p class="mt-2 text-sm text-[color:var(--text-secondary)]">Placeholder for Mon-Sun columns and habit completion markers.</p>
    </article>
  </section>
</template>
