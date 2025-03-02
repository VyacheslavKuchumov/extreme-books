import { createStore } from "vuex";
import auth from "@/store/auth";
import user from "@/store/user";
import books from "@/store/books";



export default createStore({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    auth: auth,
    user: user,
    books: books,
  },
});
