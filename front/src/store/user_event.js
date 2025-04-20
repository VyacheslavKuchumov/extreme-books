import instance from "@/middlewares";


export default {
  name: "user_event",
  state: () => ({
    data: null,

  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },


  },
  actions: {

    // get user events for user uid
    async getUserEvents({ commit }, user_uid) {
      try {
        const response = await instance.get(`/api/user_event/user/${user_uid}`);
        if (response) return commit("setData", response.data);
      } catch (error) {
        console.log(error);
      }
    },
    // get user events for event id
    async getUserEventsByEventId({ commit }, event_id) {
      try {
        const response = await instance.get(`/api/user_event/event/${event_id}`);
        if (response) return commit("setData", response.data);
      } catch (error) {
        console.log(error);
      }
    },
    // create a new user event
    async createUserEvent({}, input) {
      try {
        const { user_uid, event_id } = input;
        const response = await instance.post("/api/user_event", { user_uid, event_id });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },
    // update an existing user event by id
    async updateUserEvent({}, input) {
      try {
        const { user_event_id, user_uid, event_id } = input;
        const response = await instance.put(`/api/user_event/${user_event_id}`, { user_uid, event_id });
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },
    // delete an existing user event by id
    async deleteUserEvent({}, user_event_id) {
      try {
        const response = await instance.delete(`/api/user_event/${user_event_id}`);
        if (response.ok) return console.log("ok");
      } catch (error) {
        console.log(error);
      }
    },


},

namespaced: true,
};
