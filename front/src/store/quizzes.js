import instance from "@/middlewares";


export default {
  name: "quizzes",
  state: () => ({
    data: null,

  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },

  },
  actions: {
    // class Quiz(Base):
    // __tablename__ = "quizzes"

    // quiz_id = Column(BigInteger, primary_key=True, index=True)
    // points = Column(BigInteger, nullable=False)
    // book_id = Column(BigInteger, ForeignKey("books.book_id"), nullable=False)
    
    // book = relationship("Book", back_populates="quizzes")
    
    
    // quizzes crud
    // get quizzes
    async getQuizzes({ commit }) {
        try {
            const response = await instance.get("/api/quizzes");
            if (response) return commit("setData", response.data);
        }
        catch (error) {
            console.log(error);
        }
    },

    // create quiz
    // points: number
    // book_id: number
    async createQuiz({}, input) {
        try {
            const { points, book_id } = input;
            const response = await instance.post("/api/quizzes", { points, book_id });
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },

    // update quiz
    // points: number
    // book_id: number
    async updateQuiz({}, input) {
        try {
            const { id, points, book_id } = input;
            const response = await instance.put(`/api/quizzes/${id}`, { points, book_id });
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },

    // delete quiz
    async deleteQuiz({}, id) {
        try {
            const response = await instance.delete(`/api/quizzes/${id}`);
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },

},

namespaced: true,
};
