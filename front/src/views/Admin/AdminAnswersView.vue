<template>
    <v-card max-width="800" class="elevation-0 mt-5 ml-auto mr-auto">
      <v-card-title class="text-wrap" align="center">
        Варианты ответов для вопроса "{{ one_question().question_text }}" (админ)
      </v-card-title>
    </v-card>
  
    <v-card class="elevation-5 mt-5 ml-auto mr-auto" max-width="800">
      <v-toolbar flat>
        <v-btn icon="mdi-keyboard-backspace" color="primary" @click="goBack"></v-btn>
        <v-spacer></v-spacer>
        <v-btn icon="mdi-plus" color="primary" @click="openCreateDialog"></v-btn>
      </v-toolbar>
  
      <v-container v-if="answers() && answers().length">
        <v-data-table
          :headers="headers"
          :items="answers()"
          :items-per-page="-1"
          hide-default-footer
        >
          <template v-slot:item.answer_text="{ item }">
            <div>{{ item.answer_text }}</div>
          </template>
          <template v-slot:item.is_correct="{ item }">
            <div>{{ item.is_correct ? 'Да' : 'Нет' }}</div>
          </template>
          <template v-slot:item.question_id="{ item }">
            <div>{{ item.question_id }}</div>
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
  
    <!-- Диалог создания/редактирования ответа -->
    <v-dialog v-model="editDialog" max-width="450px">
      <v-card>
        <v-card-title class="text-h5">
          {{ editingAnswer ? "Редактировать" : "Создать" }}
        </v-card-title>
        <v-card-text>
          <v-form ref="answerForm" v-model="valid" @submit.prevent="saveAnswer">
            <v-text-field
              v-model="answerForm.answer_text"
              label="Ответ"
              clearable
              :rules="[rules.required]"
            ></v-text-field>
            <v-checkbox
              v-model="answerForm.is_correct"
              label="Правильный"
            ></v-checkbox>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="closeEditDialog">Отмена</v-btn>
          <v-btn color="primary" :disabled="!valid" @click="saveAnswer">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
    <!-- Диалог подтверждения удаления -->
    <v-dialog v-model="confirmDeleteDialog" max-width="400px">
      <v-card>
        <v-card-title class="text-h5">Подтвердите удаление</v-card-title>
        <v-card-text>
          Вы уверены, что хотите удалить ответ с ID «{{ answerToDelete?.answer_id }}»?
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
        answerToDelete: null,
        editingAnswer: null,
        answerForm: {
          answer_text: "",
          is_correct: false,
        },
        question_id: null,
        valid: false,
        rules: {
          required: (value) => !!value || "Это поле обязательно",
        },
      };
    },
    computed: {
      headers() {
        return [
          { title: "Ответ", key: "answer_text" },
          { title: "Правильный", key: "is_correct" },
          { title: "", key: "edit", sortable: false },
          { title: "", key: "delete", sortable: false },
        ];
      },
    },
    methods: {
      answers() {
        return this.$store.state.answers.data || [];
      },
      one_question() {
        return this.$store.state.questions.one_question || {};
      },
      ...mapActions({
        getAnswers: "answers/getAnswers",
        createAnswer: "answers/createAnswer",
        updateAnswer: "answers/updateAnswer",
        deleteAnswer: "answers/deleteAnswer",

        getQuestionById: "questions/getQuestionById",
      }),
      goBack() {
        this.$router.go(-1);
      },
      async openCreateDialog() {
        this.editingAnswer = null;
        this.answerForm = { answer_text: "", is_correct: false };
        this.editDialog = true;
      },
      openEditDialog(answer) {
        this.editingAnswer = answer;
        this.answerForm = {
          answer_text: answer.answer_text,
          is_correct: answer.is_correct,
        };
        this.editDialog = true;
      },
      closeEditDialog() {
        this.editDialog = false;
        this.answerForm = { answer_text: "", is_correct: false };
      },
      async saveAnswer() {
        const formData = { ...this.answerForm, question_id: this.question_id };
        if (this.editingAnswer) {
          formData.id = this.editingAnswer.answer_id;
          await this.updateAnswer(formData);
        } else {
          await this.createAnswer(formData);
        }
        await this.getAnswers(this.question_id);
        this.closeEditDialog();
      },
      confirmDelete(answer) {
        this.answerToDelete = answer;
        this.confirmDeleteDialog = true;
      },
      closeConfirmDialog() {
        this.confirmDeleteDialog = false;
        this.answerToDelete = null;
      },
      async deleteConfirmed() {
        if (this.answerToDelete) {
          await this.deleteAnswer(this.answerToDelete.answer_id);
          await this.getAnswers(this.question_id);
          this.closeConfirmDialog();
        }
      },
    },
    async created() {
      const route = useRoute();
      this.question_id = route.params.id;
      await this.getAnswers(this.question_id);
      await this.getQuestionById(this.question_id);
    },
  };
  </script>
  