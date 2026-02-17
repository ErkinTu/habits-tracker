<script setup lang="ts">
import { useMotionTokens } from '@/composables/useMotionTokens'

const { sectionHeader, subtleBounce } = useMotionTokens()
</script>

<template>
  <section class="space-y-6">
    <header v-motion :initial="sectionHeader.initial" :enter="sectionHeader.enter">
      <p class="page-eyebrow">Today</p>
      <h2 class="page-title">Home</h2>
      <p class="page-subtitle">Track habits for today and keep your streak in focus.</p>
    </header>

    <div class="grid gap-4 lg:grid-cols-2">
      <article v-motion class="panel-card p-5" :initial="subtleBounce(70).initial" :enter="subtleBounce(70).enter">
        <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Main Habits</h3>
        <p class="mt-2 text-sm text-[color:var(--text-secondary)]">
          Placeholder for habit checklist, completion state, and quick actions.
        </p>
      </article>

      <article v-motion class="panel-card p-5" :initial="subtleBounce(120).initial" :enter="subtleBounce(120).enter">
        <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Daily Summary</h3>
        <p class="mt-2 text-sm text-[color:var(--text-secondary)]">
          Placeholder for completion ratio, streak, and motivation block.
        </p>
      </article>
    </div>
  </section>
</template>
