import { watch } from 'vue'
import { useStorage } from '@vueuse/core'

export type AccentTheme = 'teal' | 'sun' | 'violet'

const THEME_ACCENT_KEY = 'habits-theme-accent'

const accent = useStorage<AccentTheme>(THEME_ACCENT_KEY, 'teal')
let initialized = false

const applyAccentAttribute = (value: AccentTheme) => {
  if (typeof document === 'undefined') return
  document.documentElement.dataset.accent = value
}

export const useTheme = () => {
  if (!initialized) {
    watch(
      accent,
      (value) => {
        applyAccentAttribute(value)
      },
      { immediate: true },
    )

    initialized = true
  }

  return {
    accent,
    setAccent: (value: AccentTheme) => {
      accent.value = value
    },
  }
}
