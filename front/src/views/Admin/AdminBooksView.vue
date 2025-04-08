<template>
    <v-card max-width="800" class="elevation-0 mt-5 ml-auto mr-auto">
      <v-card-title class="text-wrap" align="center">
        Список книг (админ)
      </v-card-title>
    </v-card>
  
    <v-card class="elevation-5 mt-5 ml-auto mr-auto" max-width="800">
      <v-toolbar flat>
        <v-spacer></v-spacer>
        <v-btn icon="mdi-plus" color="primary" @click="openCreateDialog"></v-btn>
      </v-toolbar>
  
      <v-container v-if="books()">
        <v-data-table
          :headers="headers"
          :items="books()"
          :items-per-page="-1"
          hide-default-footer
        >
          <template v-slot:item.img_url="{ item }">
            <v-img :src="item.img_url" max-width="100" max-height="100" contain></v-img>
          </template>
          
          <template v-slot:item.quiz="{ item }">
            <v-btn size="small" color="secondary" class="mr-2" @click="goToQuiz(item)">
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
  
    <v-dialog v-model="editDialog" max-width="450px">
      <v-card>
        <v-card-title class="text-h5">
          {{ editingBook ? "Редактировать" : "Создать" }}
        </v-card-title>
        <v-card-text>
          <v-form ref="bookForm" v-model="valid" @submit.prevent="saveBook">
            <v-text-field
              v-model="bookForm.title"
              label="Название"
              clearable
              :rules="[rules.required]"
            ></v-text-field>
            <v-text-field
              v-model="bookForm.author"
              label="Автор"
              clearable
              :rules="[rules.required]"
            ></v-text-field>
            <v-text-field
              v-model="bookForm.img_url"
              label="URL изображения"
              clearable
              
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="closeEditDialog">Отмена</v-btn>
          <v-btn color="primary" :disabled="!valid" @click="saveBook">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
    <v-dialog v-model="confirmDeleteDialog" max-width="400px">
      <v-card>
        <v-card-title class="text-h5">Подтвердите удаление</v-card-title>
        <v-card-text>
          Вы уверены, что хотите удалить книгу «{{ bookToDelete?.title }}»?
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
  
  export default {
    data() {
      return {
        headers: [
          { title: "Название", key: "title" },
          { title: "Автор", key: "author" },
          { title: "Изображение", key: "img_url" },
          { title: "", key: "quiz", sortable: false },
          { title: "", key: "edit", sortable: false },
          { title: "", key: "delete", sortable: false },
        ],
        confirmDeleteDialog: false,
        editDialog: false,
        bookToDelete: null,
        editingBook: null,
        bookForm: {
          title: "",
          author: "",
          img_url: "",
        },
        valid: false,
        rules: {
          required: (value) => !!value || "Это поле обязательно",
        },
      };
    },
    computed: {
      
    },
    methods: {
        books() {
        return this.$store.state.books.data;
      },
      ...mapActions({
        getBooks: "books/getBooks",
        createBook: "books/createBook",
        updateBook: "books/updateBook",
        deleteBook: "books/deleteBook",
      }),
      goToQuiz(book) {
        this.$router.push(`/admin/quizzes/${book.book_id}`);
      },
      openCreateDialog() {
        this.editingBook = null;
        this.bookForm = { title: "", author: "", img_url: "" };
        this.editDialog = true;
      },
      openEditDialog(book) {
        this.editingBook = book;
        this.bookForm = { ...book };
        this.editDialog = true;
      },
      closeEditDialog() {
        this.editDialog = false;
        this.bookForm = { title: "", author: "", img_url: "" };
      },
      async saveBook() {
        const formData = { ...this.bookForm };
        if (this.editingBook) {
          formData.id = this.editingBook.book_id;
          await this.updateBook(formData);
        } else {
          await this.createBook(formData);
        }
        await this.getBooks();
        this.closeEditDialog();
      },
      confirmDelete(book) {
        this.bookToDelete = book;
        this.confirmDeleteDialog = true;
      },
      closeConfirmDialog() {
        this.confirmDeleteDialog = false;
        this.bookToDelete = null;
      },
      async deleteConfirmed() {
        if (this.bookToDelete) {
          await this.deleteBook(this.bookToDelete.book_id);
          await this.getBooks();
          this.closeConfirmDialog();
        }
      },
    },
    async created() {
      await this.getBooks();
    },
  };
  </script>
  