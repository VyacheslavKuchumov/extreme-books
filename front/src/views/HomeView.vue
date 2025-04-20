<template>
  <v-card v-if="user()" class="mx-auto" max-width="400">
    <template v-slot:title>
      <span class="font-black">Пользователь: {{ user().name }}</span>
    </template>
    <v-card-text>
      <!-- Список событий -->
      <v-list dense>
        <v-list-item
          v-for="event in userEvents()"
          :key="event.event_id"
          class="mb-2"
        >
          
            <v-list-item-title class="font-medium">Запись на мероприятие: "{{ event.event.title }}"</v-list-item-title>
            <v-list-item-subtitle>{{ event.event.start_date }}</v-list-item-subtitle>
          
        </v-list-item>
        <v-divider></v-divider>
        <div v-if="!userEvents()" class="text-center grey--text">
          Нет записей о событиях
        </div>
      </v-list>

      <!-- Слайдер с итоговым баллом -->
      <div class="mt-4">
        <span class="subtitle-2 font-medium">Итоговый балл за опросы: {{ totalScore }}</span>
        <v-slider
          v-model="totalScore"
          :min="0"
          :max="20"
          readonly
          hide-details
          class="mt-2"
        ></v-slider>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "HomeView",
  data() {
    return {
      hasUserInfo: false,
    };
  },
  computed: {
    // Сумма всех final_score
    totalScore() {
      return this.userQuiz().reduce(
        (sum, quiz) => sum + (Number(quiz.final_score) || 0),
        0
      );
    },

  },
  methods: {
    ...mapActions({
      getUser: "user/getUserByUid",
      getUserEvents: "user_event/getUserEvents",
      getUserQuiz: "user_quiz/getUserQuiz",
    }),

    user() {
      return this.$store.state.user.user;
    },
    userEvents() {
      return this.$store.state.user_event.data || [];
    },
    userQuiz() {
      return this.$store.state.user_quiz.data || [];
    },
  },
  async mounted() {
    this.uid = localStorage.getItem("uid");

    if (this.uid) {
      await this.getUser();
      this.getUserEvents(this.uid);
      this.getUserQuiz(this.uid);
    }
  },
};
</script>
