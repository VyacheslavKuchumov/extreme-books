<template>
    <v-overlay :model-value="overlay" class="align-center justify-center">
      <v-progress-circular color="primary" size="64" indeterminate></v-progress-circular>
    </v-overlay>
    
    <!-- Dialog для уведомления об успешной регистрации -->
    <v-dialog v-model="dialog" max-width="400">
      <v-card>
        <v-card-title class="headline">Регистрация</v-card-title>
        <v-card-text>
          Вы успешно зарегистрированы на мероприятие.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            Закрыть
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
    <!-- Header Card -->
    <v-card max-width="800" class="elevation-0 mt-5 ml-auto mr-auto">
      <v-card-title class="text-wrap" align="center">
        Мероприятия
      </v-card-title>
    </v-card>
    
    <!-- Main Card with Event Grid -->
    <v-card class="elevation-0 mt-5 ml-auto mr-auto" max-width="800">
      <v-container v-if="events && events.length">
        <v-row>
          <v-col
            v-for="item in events"
            :key="item.event_id"
            cols="12"
            sm="6"
            md="4"
          >
            <v-card class="ma-2">
              <!-- Event Image with Title Overlay -->
              <v-img
                :src="item.img_url"
                min-height="150px"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.5)"
              ></v-img>
              <v-card-title class="text-wrap">{{ item.title }}</v-card-title>
              <!-- Event Details -->
              <v-card-text>
                <div>
                  <strong>Дата:</strong>
                  {{ isoToRussianDate(item.start_date) }}
                </div>
              </v-card-text>
              <!-- Action Button -->
              <v-card-actions class="justify-center">
                <v-btn color="primary" @click="register(item)">
                  Записаться
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    
      <!-- Alert in case no events are available -->
      <v-alert v-else type="info" class="ma-4">
        Нет данных
      </v-alert>
    </v-card>
  </template>
  
  <script>
  import user from "@/store/user";
import { mapActions } from "vuex";
  
  export default {
    data() {
      return {
        overlay: false,
        dialog: false, // Контролирует отображение диалога
      };
    },
    computed: {
      events() {
        return this.$store.state.events.data;
      },
      user() {
        return this.$store.state.user.user;
      },
    },
    methods: {
      ...mapActions({
        getEvents: "events/getEvents",
        createUserEvent: "user_event/createUserEvent",
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
      
      async register(item) {
        await this.createUserEvent({
          event_id: item.event_id,
          user_uid: localStorage.getItem("uid"),
        });
        this.dialog = true;
      },
    },
    async created() {
      this.overlay = true;
      await this.getEvents();
      

      this.overlay = false;
    },
  };
  </script>
  