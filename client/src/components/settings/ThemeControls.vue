<script setup lang="ts">
import type { AccentTheme } from '@/composables/useTheme'
import { useTheme } from '@/composables/useTheme'

const { accent, setAccent } = useTheme()

const accentOptions: Array<{ label: string; value: AccentTheme; description: string; swatch: string }> = [
  {
    label: 'Green-Blue',
    value: 'teal',
    description: 'Calm and focused.',
    swatch: 'linear-gradient(135deg, #0d9488 0%, #0ea5e9 100%)',
  },
  {
    label: 'Yellow-Blue',
    value: 'sun',
    description: 'Energetic and bright.',
    swatch: 'linear-gradient(135deg, #ca8a04 0%, #0284c7 100%)',
  },
  {
    label: 'Violet-Blue',
    value: 'violet',
    description: 'Creative and smooth.',
    swatch: 'linear-gradient(135deg, #7c3aed 0%, #2563eb 100%)',
  },
]
</script>

<template>
  <article class="panel-card p-5">
    <h3 class="text-base font-semibold text-[color:var(--text-primary)]">Accent Palette</h3>
    <p class="mt-2 text-sm text-[color:var(--text-secondary)]">
      Select your main focus color. Theme mode switch (sun/moon) is in the navigation panel.
    </p>

    <div class="mt-5">
      <p class="text-xs font-semibold uppercase tracking-[0.18em] text-[color:var(--text-muted)]">Accent</p>
      <div class="mt-2 grid gap-2 sm:grid-cols-3">
        <button
          v-for="item in accentOptions"
          :key="item.value"
          type="button"
          class="choice-card"
          :class="accent === item.value ? 'choice-card-active' : ''"
          @click="setAccent(item.value)"
        >
          <span class="h-8 w-full rounded-lg border border-white/20" :style="{ background: item.swatch }" />
          <span class="mt-2 text-sm font-semibold">{{ item.label }}</span>
          <span class="mt-1 text-xs text-[color:var(--text-secondary)]">{{ item.description }}</span>
        </button>
      </div>
    </div>
  </article>
</template>
