import instance from "@/middlewares";


export default {
  name: "answers",
  state: () => ({
    data: null,

  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },

  },
  actions: {
    //     # class for answers
    // class Answer(Base):
    //     __tablename__ = "answers"

    //     answer_id = Column(BigInteger, primary_key=True, index=True)
    //     answer_text = Column(Text, nullable=False)
    //     is_correct = Column(Boolean, nullable=False)
    //     question_id = Column(BigInteger, ForeignKey("questions.question_id"), nullable=False)
        
    //     question = relationship("Question", back_populates="answer")

    // answer crud
    // get answers
    async getAnswers({ commit }, question_id) {
      try {
        const response = await instance.get(`/api/answers/${question_id}`);
        if (response) return commit("setData", response.data);
      } catch (error) {
        console.log(error);
      }
    },

    // create answer
    async createAnswer({}, input) {
      try {
        const { answer_text, is_correct, question_id } = input;
        const response = await instance.post("/api/answers", { answer_text, is_correct, question_id });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },

    // update answer
    async updateAnswer({}, input) {
      try {
        const { id, answer_text, is_correct, question_id } = input;
        const response = await instance.put(`/api/answers/${id}`, { answer_text, is_correct, question_id });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },

    // delete answer
    async deleteAnswer({}, id) {
      try {
        const response = await instance.delete(`/api/answers/${id}`);
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },
    

},

namespaced: true,
};
