<script setup lang="ts">
import { useMotionTokens } from '@/composables/useMotionTokens'

const { sectionHeader, subtleBounce } = useMotionTokens()
</script>

<template>
  <section class="space-y-6">
    <header v-motion :initial="sectionHeader.initial" :enter="sectionHeader.enter">
      <p class="page-eyebrow">Period</p>
      <h2 class="page-title">Month</h2>
      <p class="page-subtitle">Calendar overview for monthly consistency.</p>
    </header>

    <article v-motion class="panel-card min-h-72 p-5" :initial="subtleBounce(80).initial" :enter="subtleBounce(80).enter">
      <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Month Calendar</h3>
      <p class="mt-2 text-sm text-[color:var(--text-secondary)]">Placeholder for month heatmap and streak continuity.</p>
    </article>
  </section>
</template>
