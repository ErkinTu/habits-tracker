import { ref } from 'vue'

const themeMotionKey = ref(0)

export const useThemeTransitionSignal = () => {
  const triggerThemeMotion = () => {
    themeMotionKey.value += 1
  }

  return {
    themeMotionKey,
    triggerThemeMotion,
  }
}
