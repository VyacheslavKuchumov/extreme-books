import instance from "@/middlewares";


export default {
  name: "user_quiz",
  state: () => ({
    data: null,

  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },


  },
  actions: {
    // get user quizzes for user uid
    async getUserQuiz({ commit }, user_uid) {
      try {
        const response = await instance.get(`/api/user_quiz/user/${user_uid}`);
        if (response) return commit("setData", response.data);
      } catch (error) {
        console.log(error);
      }
    },
    // get user quizzes for quiz id
    async getUserQuizzesByQuizId({ commit }, quiz_id) {
      try {
        const response = await instance.get(`/api/user_quiz/quiz/${quiz_id}`);
        if (response) return commit("setData", response.data);
      } catch (error) {
        console.log(error);
      }
    },
    // create a new user quiz
    async createUserQuiz({}, input) {
      try {
        const { user_uid, quiz_id, final_score } = input;
        const response = await instance.post("/api/user_quiz", { user_uid, quiz_id, final_score });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },
    // update an existing user quiz by id
    async updateUserQuiz({}, input) {
      try {
        const { user_quiz_id, user_uid, quiz_id } = input;
        const response = await instance.put(`/api/user_quiz/${user_quiz_id}`, { user_uid, quiz_id, final_score });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },
    // delete an existing user quiz by id
    async deleteUserQuiz({}, user_quiz_id) {
      try {
        const response = await instance.delete(`/api/user_quiz/${user_quiz_id}`);
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },


},

namespaced: true,
};
