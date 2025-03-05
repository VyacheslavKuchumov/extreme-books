import instance from "@/middlewares";


export default {
  name: "events",
  state: () => ({
    data: null,

  }),
  mutations: {
    setData(state, data) {
      state.data = data;
    },

  },
  actions: {
    // class Event(Base):
    // __tablename__ = "events"

    // event_id = Column(BigInteger, primary_key=True, index=True)
    // title = Column(Text, nullable=False)
    // description = Column(Text, nullable=False)
    // start_date = Column(Date, nullable=False)
    // img_url = Column(Text, nullable=True)

    // events crud
    // get events
    async getEvents({ commit }) {
        try {
            const response = await instance.get("/api/events");
            if (response) return commit("setData", response.data);
        }
        catch (error) {
            console.log(error);
        }
    },

    // create event
    // title: string
    // description: string
    // start_date: string
    // img_url: string
    async createEvent({}, input) {
        try {
            const { title, description, start_date, img_url } = input;
            const response = await instance.post("/api/events", { title, description, start_date, img_url });
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },

    // update event
    // title: string
    // description: string
    // start_date: string
    // img_url: string
    async updateEvent({}, input) {
        try {
            const { id, title, description, start_date, img_url } = input;
            const response = await instance.put(`/api/events/${id}`, { title, description, start_date, img_url });
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },

    // delete event
    async deleteEvent({}, id) {
        try {
            const response = await instance.delete(`/api/events/${id}`);
            if (response.ok) return console.log("ok");
        }
        catch (error) {
            console.log(error);
        }
    },
    

},

namespaced: true,
};
