import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

export type Habit = {
  id: string
  title: string
  doneToday: boolean
}

export const useHabitsStore = defineStore('habits', () => {
  const habits = ref<Habit[]>([
    { id: 'water', title: 'Drink water', doneToday: false },
    { id: 'walk', title: 'Walk 30 min', doneToday: true },
    { id: 'read', title: 'Read 20 min', doneToday: false },
  ])

  const completedToday = computed(() => habits.value.filter((habit) => habit.doneToday).length)

  return {
    habits,
    completedToday,
  }
})
