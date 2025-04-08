import instance from "@/middlewares";


export default {
  name: "questions",
  state: () => ({
    data: null,
    one_question: null,

  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },
    setOneQuestion(state, data) {
      state.one_question = data;
    },

  },
  actions: {
    // class Question(Base):
    // __tablename__ = "questions"

    // question_id = Column(BigInteger, primary_key=True, index=True)
    // question_text = Column(Text, nullable=False)
    // quiz_id = Column(BigInteger, ForeignKey("quizzes.quiz_id"), nullable=False)
    
    // quiz = relationship("Quiz", back_populates="question")
    // answer = relationship("Answer", back_populates="question", cascade="all, delete")

    // question crud
    // get questions
    async getQuestions({ commit }, quiz_id) {
      try {
        const response = await instance.get(`/api/questions/${quiz_id}`);
        if (response) return commit("setData", response.data);
      } catch (error) {
        console.log(error);
      }
    },
    // get question by id
    async getQuestionById({ commit }, id) {
      try {
        const response = await instance.get(`/api/questions/search/${id}`);
        if (response) return commit("setOneQuestion", response.data);
      } catch (error) {
        console.log(error);
      }
    },

    // create question
    async createQuestion({}, input) {
      try {
        const { question_text, quiz_id } = input;
        const response = await instance.post("/api/questions", { question_text, quiz_id });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },

    // update question
    async updateQuestion({}, input) {
      try {
        const { id, question_text, quiz_id } = input;
        const response = await instance.put(`/api/questions/${id}`, { question_text, quiz_id });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },

    // delete question
    async deleteQuestion({}, id) {
      try {
        const response = await instance.delete(`/api/questions/${id}`);
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },

},

namespaced: true,
};
