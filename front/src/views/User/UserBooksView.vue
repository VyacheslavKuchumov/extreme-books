<template>
    <div>
      <!-- Loading Overlay -->
      <v-overlay :model-value="overlay" class="align-center justify-center">
        <v-progress-circular color="primary" size="64" indeterminate></v-progress-circular>
      </v-overlay>
  
      <!-- Header Card -->
      <v-card max-width="800" class="elevation-0 mt-5 ml-auto mr-auto">
        <v-card-title class="text-wrap" align="center">
          Книги
        </v-card-title>
      </v-card>
  
      <!-- Main Card with Books Grid -->
      <v-card class="elevation-0 mt-5 ml-auto mr-auto" max-width="800">
        <v-container v-if="books && books.length">
          <v-row>
            <v-col
              v-for="item in books"
              
              cols="12"
              sm="6"
              md="4"
            >
              <v-card class="ma-2">
                <!-- Book Cover Image -->
                <v-img
                  :src="item.img_url"
                  min-height="120px"
                  class="white--text align-end"
                  gradient="to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.5)"
                ></v-img>
                <!-- Book Title -->
                <v-card-title class="text-wrap">{{ item.title }}</v-card-title>
                <!-- Book Author -->
                <v-card-text>
                  <div>
                    <strong>Автор:</strong> {{ item.author }}
                  </div>
                </v-card-text>
                <!-- Action Button -->
                <v-card-actions class="justify-center">
                  <v-btn color="primary" @click="openQuizzesDialog(item)">
                    пройти квиз
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
  
        <!-- Alert when no books are available -->
        <v-alert v-else type="info" class="ma-4">
          Нет данных
        </v-alert>
      </v-card>
  
      <!-- Dialog для квизов -->
      <v-dialog v-model="showDialog" max-width="600">
        <v-card>
            <v-card-title class="headline">
                Квизы для "{{ selectedBook && selectedBook.title }}"
            </v-card-title>
            <v-card-text>
                <v-data-table
                v-if="selectedBook && selectedBook.quiz && selectedBook.quiz.length"
                :headers="quizTableHeaders"
                :items="selectedBook.quiz"
                :items-per-page="-1"
                hide-default-footer
                
                item-key="id"
                class="elevation-0"
                >
                <!-- Optional: Customize each column (if needed) using slots -->
                <template v-slot:item.quiz_name="{ item }">
                    {{ item.quiz_name }}
                </template>
                <template v-slot:item.points="{ item }">
                    {{ item.points }}
                </template>
                <template v-slot:item.action="{ item }">
                    <v-btn color="secondary" @click="goToQuiz(item)">
                      Пройти
                    </v-btn>
                </template>
                </v-data-table>
                <v-alert v-else type="info" class="ma-4">
                Нет доступных квизов для этой книги
                </v-alert>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="showDialog = false">Закрыть</v-btn>
            </v-card-actions>
            </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script>
  import { mapActions } from "vuex";
  
  export default {
    data() {
      return {
        overlay: false,
        showDialog: false,
        selectedBook: null,
        quizTableHeaders: [
            { title: 'Название квиза', key: 'quiz_name' },
            { title: 'Баллы', key: 'points' },
            { title: '', key: 'action', sortable: false }
        ],
      };
    },
    computed: {
      // Получаем список книг из Vuex-модуля books
      books() {
        return this.$store.state.books.data;
      },
    },
    methods: {
      ...mapActions({
        getBooks: "books/getBooks",
      }),
      // Метод для открытия диалога с квизами
      openQuizzesDialog(item) {
        this.selectedBook = item;
        this.showDialog = true;
      },
      // Метод перехода на страницу прохождения квиза
      goToQuiz(item) {
        // Замените "QuizPage" на фактическое имя маршрута
        console.log(item);
        this.$router.push(`/quiz/${item.quiz_id}`);
        this.showDialog = false;
      },
    },
    async created() {
      this.overlay = true;
      await this.getBooks();
      this.overlay = false;
    },
  };
  </script>
  