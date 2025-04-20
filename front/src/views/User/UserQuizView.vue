<template>
    <v-container>
      <!-- Заголовок квиза -->
      <v-card max-width="800" class="mt-5 elevation-0 ml-auto mr-auto">
        <v-card-title class="headline text-center">
          Квиз "{{ quiz()?.quiz_name }}"
        </v-card-title>
      </v-card>
      <v-card class="elevation-1 mt-5 ml-auto mr-auto" max-width="610">
        <v-toolbar flat>
          <v-btn icon="mdi-keyboard-backspace" color="primary" @click="$router.go(-1)"></v-btn>
          <v-spacer></v-spacer>
          <!-- <v-btn icon="mdi-refresh" color="primary" @click="getQuizById(quiz().quiz_id)"></v-btn> -->
        </v-toolbar>
  
        <v-form v-if="quiz()" ref="quizForm" class="ml-auto mr-auto" max-width="600">
          <div v-for="(question, index) in quiz().question" :key="question.question_id" class="mt-4">
            <v-card class="pa-3">
              <v-card-title>
                {{ index + 1 }}. {{ question.question_text }}
              </v-card-title>
              <v-card-text>
                <v-radio-group v-model="selectedAnswers[question.question_id]" row>
                  <v-radio
                    v-for="answer in question.answer"
                    :key="answer.answer_id"
                    :label="answer.answer_text"
                    :value="answer.answer_id"
                  ></v-radio>
                </v-radio-group>
              </v-card-text>
            </v-card>
          </div>
        </v-form>
  
        <!-- Кнопка отправки ответов -->
        <v-card-actions class="justify-center">
          <v-btn color="primary" @click="submitQuiz" :disabled="!quiz()">
            Отправить ответы
          </v-btn>
        </v-card-actions>
      </v-card>
  
      <!-- Диалог с результатами -->
      <v-dialog v-model="dialogResult" max-width="500">
        <v-card>
          <v-card-title class="headline">Результаты квиза</v-card-title>
          <v-card-text>
            Вы набрали {{ score }} баллов из {{ totalPoints }}.<br>
            Правильных ответов: {{ correctCount }} из {{ quiz().question.length }}.
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="dialogResult = false">
              Закрыть
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  
  export default {
    name: "QuizView",
    data() {
      return {
        selectedAnswers: {}, // Объект выбранных ответов { [question_id]: answer_id }
        score: 0,            // Набранные баллы
        totalPoints: 0,      // Общая сумма баллов квиза (из данных квиза)
        correctCount: 0,     // Количество вопросов с правильным ответом
        dialogResult: false  // Флаг показа диалогового окна с результатами
      };
    },
    methods: {
      ...mapActions({
        getQuizById: "quizzes/getQuizById",
        createUserQuiz: "user_quiz/createUserQuiz",
      }),
      quiz() {
        // Получаем данные квиза из Vuex
        return this.$store.state.quizzes.one_quiz;
      },
      submitQuiz() {
        // Сброс предыдущего результата
        this.score = 0;
        this.correctCount = 0;
        
        const questions = this.$store.state.quizzes.one_quiz.question || [];
        this.totalPoints = this.quiz().points || 0; // Получаем общую сумму баллов из данных квиза
        // Если есть вопросы - делим общие баллы поровну на каждый вопрос
        const pointsPerQuestion = questions.length > 0 ? this.totalPoints / questions.length : 0;
  
        // Проходим по всем вопросам и вычисляем набранные баллы и количество правильных ответов
        questions.forEach(question => {
          const selected = this.selectedAnswers[question.question_id];
          // Находим правильный ответ по флагу is_correct
          const correctAnswer = question.answer.find(ans => ans.is_correct);
          if (selected === correctAnswer?.answer_id) {
            this.score += pointsPerQuestion;
            this.correctCount += 1;
          }
        });

        this.score = Math.round(this.score * 10) / 10;

        this.createUserQuiz({
          quiz_id: this.quiz().quiz_id,
          user_uid: localStorage.getItem("uid"),
          final_score: this.score,
        })
        // Показываем диалоговое окно с результатами
        this.dialogResult = true;
      }
    },
    async created() {
      // Извлекаем quiz_id из параметров маршрута
      const quizId = this.$route.params.id;
      await this.getQuizById(quizId); // Получаем данные квиза по ID
      // Если в данных квиза есть информация о суммарных баллах, можно инициализировать totalPoints здесь
      // Например: this.totalPoints = this.quiz().totalPoints
    },
  };
  </script>
  
  <style scoped>
  /* Добавьте или измените стили по необходимости */
  </style>
  