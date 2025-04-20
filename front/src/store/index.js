import { createStore } from "vuex";
import auth from "@/store/auth";
import user from "@/store/user";
import books from "@/store/books";
import quizzes from "@/store/quizzes";
import events from "@/store/events";
import questions from "@/store/questions";
import answers from "@/store/answers";
import user_event from "@/store/user_event";
import user_quiz from "@/store/user_quiz";



export default createStore({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    auth: auth,
    user: user,
    books: books,
    quizzes: quizzes,
    events: events,
    questions: questions,
    answers: answers,
    user_event: user_event,
    user_quiz: user_quiz,
  },
});
