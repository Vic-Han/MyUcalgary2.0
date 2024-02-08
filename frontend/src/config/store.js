import { createStore } from 'vuex'


// includes all singleton data that needs to be shared across the app
const store = createStore({
  state: {
    sessionId: null
  },
  mutations: {
    setSessionId(state, id) {
      state.sessionId = id
    }
  }
})

export default store