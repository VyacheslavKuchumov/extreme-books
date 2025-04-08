import instance from "@/middlewares";


export default {
  name: "quizzes",
  state: () => ({
    data: null,
    one_quiz: null,
  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },
    setOneQuiz(state, data) {
      state.one_quiz = data;
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
    async getQuizzes({ commit }, book_id) {
        try {
            const response = await instance.get(`/api/quizzes/${book_id}`);
            if (response) return commit("setData", response.data);
        }
        catch (error) {
            console.log(error);
        }
    },
    // get quiz by id
    async getQuizById({ commit }, id) {
        try {
            const response = await instance.get(`/api/quizzes/search/${id}`);
            if (response) return commit("setOneQuiz", response.data);
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
            const { quiz_name, points, book_id } = input;
            console.log(input);
            const response = await instance.post("/api/quizzes", { quiz_name, points, book_id });
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
            const { id, quiz_name, points, book_id } = input;
            const response = await instance.put(`/api/quizzes/${id}`, { quiz_name, points, book_id });
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
