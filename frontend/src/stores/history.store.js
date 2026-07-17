import { defineStore } from "pinia";
import * as historyService from "@/services/api/history.service";

export const useHistoryStore = defineStore("history", {
  state: () => ({
    history: [],
    loading: false,
    error: null,
  }),

  actions: {
    async fetchHistory() {
      this.loading = true;
      this.error = null;

      try {
        const response = await historyService.getHistory();
        this.history = response.data;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },
  },
});