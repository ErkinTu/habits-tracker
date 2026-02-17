<script setup lang="ts">
import { useMotionTokens } from '@/composables/useMotionTokens'

const { sectionHeader, subtleBounce } = useMotionTokens()
</script>

<template>
  <section class="space-y-6">
    <header v-motion :initial="sectionHeader.initial" :enter="sectionHeader.enter">
      <p class="page-eyebrow">Insights</p>
      <h2 class="page-title">Analytics</h2>
      <p class="page-subtitle">Visual metrics for long-term habit performance.</p>
    </header>

    <div class="grid gap-4 lg:grid-cols-3">
      <article
        v-motion
        class="panel-card min-h-40 p-5 lg:col-span-2"
        :initial="subtleBounce(70).initial"
        :enter="subtleBounce(70).enter"
      >
        <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Performance Graph</h3>
        <p class="mt-2 text-sm text-[color:var(--text-secondary)]">
          Placeholder for trend line and weekly consistency chart.
        </p>
      </article>

      <article v-motion class="panel-card min-h-40 p-5" :initial="subtleBounce(120).initial" :enter="subtleBounce(120).enter">
        <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Top Habit</h3>
        <p class="mt-2 text-sm text-[color:var(--text-secondary)]">Placeholder for strongest and weakest habits.</p>
      </article>
    </div>
  </section>
</template>
