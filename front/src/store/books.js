import instance from "@/middlewares";


export default {
  name: "books",
  state: () => ({
    data: null,
    one_book: null,
  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },
    setOneBook(state, data) {
      state.one_book = data;
    },

  },
  actions: {
    // books crud
    // get books
    async getBooks({ commit }) {
        try {
            const response = await instance.get("/api/books");
            if (response) return commit("setData", response.data);
        }
        catch (error) {
            console.log(error);
        }
    },
    // get book by id
    async getBookById({commit}, id) {
        try {
            const response = await instance.get(`/api/books/search/${id}`);
            console.log(response);
            if (response) return commit("setOneBook", response.data);
        }
        catch (error) {
            console.log(error);
        }
    },

    // create book
    // title: string
    // author: string
    // img_url: string
    async createBook({}, input) {
        try {
            const { title, author, img_url } = input;
            const response = await instance.post("/api/books", { title, author, img_url });
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },

    // update book
    // title: string
    // author: string
    // img_url: string
    async updateBook({}, input) {
        try {
            const { id, title, author, img_url } = input;
            const response = await instance.put(`/api/books/${id}`, { title, author, img_url });
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },

    // delete book
    async deleteBook({}, id) {
        try {
            const response = await instance.delete(`/api/books/${id}`);
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },
    
},

namespaced: true,
};
