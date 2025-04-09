<template>
    <v-card max-width="800" class="elevation-0 mt-5 ml-auto mr-auto">
      <v-card-title class="text-wrap" align="center">
        Список мероприятий (админ)
      </v-card-title>
    </v-card>
  
    <v-card class="elevation-5 mt-5 ml-auto mr-auto" max-width="800">
      <v-toolbar flat>
        <v-spacer></v-spacer>
        <v-btn icon="mdi-plus" color="primary" @click="openCreateDialog"></v-btn>
      </v-toolbar>
  
      <v-container v-if="events() && events().length">
        <v-data-table
          :headers="headers"
          :items="events()"
          :items-per-page="-1"
          hide-default-footer
        >
          <template v-slot:item.img_url="{ item }">
            <v-img :src="item.img_url" max-width="100" max-height="100" contain></v-img>
          </template>
          <template v-slot:item.start_date="{ item }">
            <div>{{ isoToRussianDate(item.start_date) }}</div>
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
  
    <!-- Диалог создания/редактирования события -->
    <v-dialog v-model="editDialog" max-width="450px">
      <v-card>
        <v-card-title class="text-h5">
          {{ editingEvent ? "Редактировать" : "Создать" }}
        </v-card-title>
        <v-card-text>
          <v-form ref="eventForm" v-model="valid" @submit.prevent="saveEvent">
            <v-text-field
              v-model="eventForm.title"
              label="Название"
              clearable
              :rules="[rules.required]"
            ></v-text-field>

            <v-text-field
              v-model="eventForm.description"
              label="Описание"
              clearable
              
            ></v-text-field>
  
            <v-text-field
              v-model="eventForm.start_date"
              label="Дата события"
              prepend-icon="mdi-calendar"
              @click="openDateDialog"
              readonly
              clearable
              :rules="[rules.required]"
            ></v-text-field>
  
            <v-text-field
              v-model="eventForm.img_url"
              label="URL изображения"
              clearable
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="closeEditDialog">Отмена</v-btn>
          <v-btn color="primary" :disabled="!valid" @click="saveEvent">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
    <!-- Диалог выбора даты -->
    <v-dialog v-model="dateDialog" max-width="400px">
      <v-card>
        <v-date-picker v-model="datePickerDate" />
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="dateDialog = false">Закрыть</v-btn>
          <v-btn text color="primary" @click="updateDate">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
    <!-- Диалог подтверждения удаления -->
    <v-dialog v-model="confirmDeleteDialog" max-width="400px">
      <v-card>
        <v-card-title class="text-h5">Подтвердите удаление</v-card-title>
        <v-card-text>
          Вы уверены, что хотите удалить событие «{{ eventToDelete?.title }}»?
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
        dateDialog: false,
        datePickerDate: new Date().toISOString().substr(0, 10),
        confirmDeleteDialog: false,
        editDialog: false,
        eventToDelete: null,
        editingEvent: null,
        eventForm: {
          title: "",
          start_date: "",
          description: "",
          img_url: "",
        },
        valid: false,
        rules: {
          required: (value) => !!value || "Это поле обязательно",
        },
      };
    },
    computed: {
      headers() {
        return [
          { title: "Название", key: "title" },
          {title: "Описание", key: "description"},
          { title: "Дата начала", key: "start_date" },
          { title: "Изображение", key: "img_url" },
          { title: "", key: "edit", sortable: false },
          { title: "", key: "delete", sortable: false },
        ];
      },
    },
    methods: {
      events() {
        return this.$store.state.events.data;
      },
      ...mapActions({
        getEvents: "events/getEvents",
        createEvent: "events/createEvent",
        updateEvent: "events/updateEvent",
        deleteEvent: "events/deleteEvent",
      }),
      isoToRussianDate(isoDate) {
        if (!isoDate || typeof isoDate !== "string") {
          throw new Error("Invalid input. Please provide a valid ISO date string.");
        }
        const [year, month, day] = isoDate.split("-");
        if (!year || !month || !day || isNaN(Date.parse(isoDate))) {
          throw new Error("Invalid ISO date format.");
        }
        return `${day}.${month}.${year}`;
      },
      russianDateToIso(russianDate) {
        if (!russianDate || typeof russianDate !== "string") {
          throw new Error("Invalid input. Please provide a valid Russian date string.");
        }
        const [day, month, year] = russianDate.split(".");
        if (!year || !month || !day || isNaN(Date.parse(`${year}-${month}-${day}`))) {
          throw new Error("Invalid Russian date format.");
        }
        return `${year}-${month}-${day}`;
      },
      updateDate() {
        const date = new Date(this.datePickerDate);
        date.setMinutes(date.getMinutes() - date.getTimezoneOffset());
        this.eventForm.start_date = this.isoToRussianDate(date.toISOString().split("T")[0]);
        this.dateDialog = false;
      },
      openDateDialog() {
        this.datePickerDate = new Date().toISOString().substr(0, 10);
        this.dateDialog = true;
      },
      openCreateDialog() {
        this.editingEvent = null;
        this.eventForm = { title: "", start_date: "", img_url: "", description: "" };
        this.editDialog = true;
      },
      openEditDialog(event) {
        this.editingEvent = event;
        this.eventForm = { 
          title: event.title, 
          description: event.description,
          start_date: this.isoToRussianDate(event.start_date),
          img_url: event.img_url,
        };
        this.editDialog = true;
      },
      closeEditDialog() {
        this.editDialog = false;
        this.eventForm = { title: "", date: "", img_url: "", description: "" };
      },
      async saveEvent() {
        const formData = { ...this.eventForm };
        formData.start_date = this.russianDateToIso(formData.start_date);
        if (this.editingEvent) {
          formData.id = this.editingEvent.event_id;
          await this.updateEvent(formData);
        } else {
          await this.createEvent(formData);
        }
        await this.getEvents();
        this.closeEditDialog();
      },
      confirmDelete(event) {
        this.eventToDelete = event;
        this.confirmDeleteDialog = true;
      },
      closeConfirmDialog() {
        this.confirmDeleteDialog = false;
        this.eventToDelete = null;
      },
      async deleteConfirmed() {
        if (this.eventToDelete) {
          await this.deleteEvent(this.eventToDelete.event_id);
          await this.getEvents();
          this.closeConfirmDialog();
        }
      },
    },
    async created() {
      await this.getEvents();
    },
  };
  </script>
  