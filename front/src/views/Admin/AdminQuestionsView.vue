<template>
    <v-card max-width="800" class="elevation-0 mt-5 ml-auto mr-auto">
      <v-card-title class="text-wrap" align="center">
        Список вопросов для квиза "{{ one_quiz().quiz_name }}" (админ)
      </v-card-title>
    </v-card>
  
    <v-card class="elevation-5 mt-5 ml-auto mr-auto" max-width="800">
      <v-toolbar flat>
        <v-btn icon="mdi-keyboard-backspace" color="primary" @click="goBack"></v-btn>
        <v-spacer></v-spacer>
        <v-btn icon="mdi-plus" color="primary" @click="openCreateDialog"></v-btn>
      </v-toolbar>
  
      <v-container v-if="questions() && questions().length">
        <v-data-table
          :headers="headers"
          :items="questions()"
          :items-per-page="-1"
          hide-default-footer
        >
          <template v-slot:item.question_text="{ item }">
            <div>{{ item.question_text }}</div>
          </template>
          <template v-slot:item.quiz_id="{ item }">
            <div>{{ item.quiz_id }}</div>
          </template>
          <template v-slot:item.answer="{ item }">
            <v-btn size="small" color="secondary" class="mr-2" @click="goToAnswer(item)">
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
  
    <!-- Диалог создания/редактирования вопроса -->
    <v-dialog v-model="editDialog" max-width="450px">
      <v-card>
        <v-card-title class="text-h5">
          {{ editingQuestion ? "Редактировать" : "Создать" }}
        </v-card-title>
        <v-card-text>
          <v-form ref="questionForm" v-model="valid" @submit.prevent="saveQuestion">
            <v-text-field
              v-model="questionForm.question_text"
              label="Вопрос"
              clearable
              :rules="[rules.required]"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="closeEditDialog">Отмена</v-btn>
          <v-btn color="primary" :disabled="!valid" @click="saveQuestion">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
    <!-- Диалог подтверждения удаления -->
    <v-dialog v-model="confirmDeleteDialog" max-width="400px">
      <v-card>
        <v-card-title class="text-h5">Подтвердите удаление</v-card-title>
        <v-card-text>
          Вы уверены, что хотите удалить вопрос с ID «{{ questionToDelete?.question_id }}»?
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
        questionToDelete: null,
        editingQuestion: null,
        questionForm: {
          question_text: "",
        },
        quiz_id: null,
        valid: false,
        rules: {
          required: (value) => !!value || "Это поле обязательно",
        },
      };
    },
    computed: {
      headers() {
        return [
          { title: "Вопрос", key: "question_text" },
          { title: "", key: "answer", sortable: false },
          { title: "", key: "edit", sortable: false },
          { title: "", key: "delete", sortable: false },
        ];
      },
    },
    methods: {
      questions() {
        return this.$store.state.questions.data || [];
      },
      one_quiz() {
        return this.$store.state.quizzes.one_quiz || {};
      },
      ...mapActions({
        getQuestions: "questions/getQuestions",
        createQuestion: "questions/createQuestion",
        updateQuestion: "questions/updateQuestion",
        deleteQuestion: "questions/deleteQuestion",

        getQuizById: "quizzes/getQuizById",
      }),
      goBack() {
        this.$router.go(-1);
      },
        goToAnswer(question) {
            this.$router.push(`/admin/answers/${question.question_id}`);
        },
      async openCreateDialog() {
        this.editingQuestion = null;
        this.questionForm = { question_text: "" };
        this.editDialog = true;
      },
      openEditDialog(question) {
        this.editingQuestion = question;
        this.questionForm = {
          question_text: question.question_text,
        };
        this.editDialog = true;
      },
      closeEditDialog() {
        this.editDialog = false;
        this.questionForm = { question_text: "" };
      },
      async saveQuestion() {
        const formData = { ...this.questionForm, quiz_id: this.quiz_id };
        if (this.editingQuestion) {
          formData.id = this.editingQuestion.question_id;
          await this.updateQuestion(formData);
        } else {
          await this.createQuestion(formData);
        }
        await this.getQuestions(this.quiz_id);
        this.closeEditDialog();
      },
      confirmDelete(question) {
        this.questionToDelete = question;
        this.confirmDeleteDialog = true;
      },
      closeConfirmDialog() {
        this.confirmDeleteDialog = false;
        this.questionToDelete = null;
      },
      async deleteConfirmed() {
        if (this.questionToDelete) {
          await this.deleteQuestion(this.questionToDelete.question_id);
          await this.getQuestions(this.quiz_id);
          this.closeConfirmDialog();
        }
      },
    },
    async created() {
      const route = useRoute();
      this.quiz_id = route.params.id;
      await this.getQuestions(this.quiz_id);
        await this.getQuizById(this.quiz_id);
    },
  };
  </script>
  