<template>
    <v-card max-width="800" class="elevation-0 mt-5 ml-auto mr-auto">
      <v-card-title class="text-wrap" align="center">
        Список квизов по книге "{{ one_book().title }}" (админ)
      </v-card-title>
    </v-card>
  
    <v-card class="elevation-5 mt-5 ml-auto mr-auto" max-width="800">
      <v-toolbar flat>
        <v-btn icon="mdi-keyboard-backspace" color="primary" @click="goBack"></v-btn>
        <v-spacer></v-spacer>
        <v-btn icon="mdi-plus" color="primary" @click="openCreateDialog"></v-btn>
      </v-toolbar>
  
      <v-container v-if="quizzes() && quizzes().length">
        <v-data-table
          :headers="headers"
          :items="quizzes()"
          :items-per-page="-1"
          hide-default-footer
        >
          <template v-slot:item.points="{ item }">
            <div>{{ item.points }}</div>
          </template>
          <template v-slot:item.book="{ item }">
            <div>
              {{ item.book ? item.book.title : item.book_id }}
            </div>
          </template>
          <template v-slot:item.question="{ item }">
            <v-btn size="small" color="secondary" class="mr-2" @click="goToQuestion(item)">
              <v-icon>mdi-chat-question</v-icon>
            </v-btn>
          </template>
          <template v-slot:item.edit="{ item }">
            <v-btn size="small" color="primary" class="mr-2" @click="openEditDialog(item)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </template>
          <template v-slot:item.delete="{ item }">
            <v-btn size="small" color="red" @click="confirmDelete(item)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </template>
        </v-data-table>
      </v-container>
  
      <v-alert v-else type="info" class="ma-4">
        Нет данных
      </v-alert>
    </v-card>
  
    <!-- Диалог создания/редактирования квиза -->
    <v-dialog v-model="editDialog" max-width="450px">
      <v-card>
        <v-card-title class="text-h5">
          {{ editingQuiz ? "Редактировать" : "Создать" }}
        </v-card-title>
        <v-card-text>
          <v-form ref="quizForm" v-model="valid" @submit.prevent="saveQuiz">
            <v-text-field
              v-model="quizForm.quiz_name"
              label="Название"
              clearable
              :rules="[rules.required]"
            ></v-text-field>
            <v-text-field
              v-model="quizForm.points"
              label="Баллы"
              type="number"
              clearable
              :rules="[rules.required]"
            ></v-text-field>
            
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="closeEditDialog">Отмена</v-btn>
          <v-btn color="primary" :disabled="!valid" @click="saveQuiz">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
    <!-- Диалог подтверждения удаления -->
    <v-dialog v-model="confirmDeleteDialog" max-width="400px">
      <v-card>
        <v-card-title class="text-h5">Подтвердите удаление</v-card-title>
        <v-card-text>
          Вы уверены, что хотите удалить квиз с ID «{{ quizToDelete?.quiz_id }}»?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="closeConfirmDialog">Отмена</v-btn>
          <v-btn color="red" @click="deleteConfirmed">Удалить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script>
  import { mapActions } from "vuex";
  import { useRoute } from "vue-router";
  
  export default {
    data() {
      return {
        confirmDeleteDialog: false,
        editDialog: false,
        quizToDelete: null,
        editingQuiz: null,
        quizForm: {
          quiz_name: "",
          points: "",
        },
        book_id: null,
        valid: false,
        rules: {
          required: (value) => !!value || "Это поле обязательно",
        },
        
      };
    },
    computed: {
      headers() {
        return [
            { title: "Название квиза", key: "quiz_name" },
            { title: "Баллы за прохождение", key: "points" },
            { title: "", key: "question", sortable: false },
          { title: "", key: "edit", sortable: false },
          { title: "", key: "delete", sortable: false },
        ];
      },
    },
    methods: {
      quizzes() {
        return this.$store.state.quizzes.data;
      },
      one_book() {
        return this.$store.state.books.one_book || {};
      },
      ...mapActions({
        getQuizzes: "quizzes/getQuizzes",
        createQuiz: "quizzes/createQuiz",
        updateQuiz: "quizzes/updateQuiz",
        deleteQuiz: "quizzes/deleteQuiz",
        getBookById: "books/getBookById",
      }),
      goBack() {
        this.$router.go(-1)
      },
      goToQuestion(quiz) {
        this.$router.push(`/admin/questions/${quiz.quiz_id}`);
      },
      async openCreateDialog() {
        this.editingQuiz = null;
        this.quizForm = { quiz_name: "", points: ""};
        this.editDialog = true;
      },
      openEditDialog(quiz) {
        this.editingQuiz = quiz;
        this.quizForm = {
          quiz_name: quiz.quiz_name,
          points: quiz.points,
        };
        this.editDialog = true;
      },
      closeEditDialog() {
        this.editDialog = false;
        this.quizForm = { quiz_name: "", points: "" };
      },
      async saveQuiz() {
        const formData = { ...this.quizForm, book_id: this.book_id };
        if (this.editingQuiz) {
          
          formData.id = this.editingQuiz.quiz_id;
          await this.updateQuiz(formData);
        } else {
          await this.createQuiz(formData);
        }

        await this.getQuizzes(this.book_id);
        this.closeEditDialog();
      },
      confirmDelete(quiz) {
        this.quizToDelete = quiz;
        this.confirmDeleteDialog = true;
      },
      closeConfirmDialog() {
        this.confirmDeleteDialog = false;
        this.quizToDelete = null;
      },
      async deleteConfirmed() {
        if (this.quizToDelete) {
          await this.deleteQuiz(this.quizToDelete.quiz_id);
          await this.getQuizzes(this.book_id);
          this.closeConfirmDialog();
        }
      },
      
    },
    async created() {
      const route = useRoute();
      this.book_id = route.params.id;
      await this.getQuizzes(this.book_id);
      await this.getBookById(this.book_id);
    },
  };
  </script>
  