export type MotionState = Record<string, unknown>

const easeOutSoft = 'ease-out'

const pageTransition = {
  duration: 320,
  easing: easeOutSoft,
}

const sectionTransition = {
  duration: 360,
  easing: easeOutSoft,
}

const cardTransition = {
  duration: 380,
  easing: easeOutSoft,
}

export const useMotionTokens = () => {
  const routeContainer = {
    initial: { opacity: 0, y: 10, scale: 0.995 } satisfies MotionState,
    enter: {
      opacity: 1,
      y: 0,
      scale: 1,
      transition: pageTransition,
    } satisfies MotionState,
  }

  const themeFlash = {
    initial: { opacity: 0.28, scale: 1.015 } satisfies MotionState,
    enter: {
      opacity: 0,
      scale: 1,
      transition: { duration: 480, easing: easeOutSoft },
    } satisfies MotionState,
  }

  const sectionHeader = {
    initial: { opacity: 0, y: 8 } satisfies MotionState,
    enter: {
      opacity: 1,
      y: [8, 0, -2, 0],
      transition: sectionTransition,
    } satisfies MotionState,
  }

  const subtleBounce = (delay = 0) => ({
    initial: { opacity: 0, y: 10 } satisfies MotionState,
    enter: {
      opacity: 1,
      y: [10, 0, -2, 0],
      transition: { ...cardTransition, delay },
    } satisfies MotionState,
  })

  const tapAction = {
    initial: { rotate: 0, scale: 1 } satisfies MotionState,
    hovered: { scale: 1.06 } satisfies MotionState,
    tapped: { scale: 0.94 } satisfies MotionState,
  }

  return {
    routeContainer,
    themeFlash,
    sectionHeader,
    subtleBounce,
    tapAction,
  }
}
