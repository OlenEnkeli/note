import userApi from '../api/user';

export default {
  state: {
    current: [],
  },

  mutations: {
    setUser(state, user) {
      state.current = user;
    },
  },

  actions: {
    getCurrentUser({ commit }) {
      userApi.getCurrentUser()
        .then((user) => {
          commit('setUser', user);
        });
    },

    login({ commit }, email, password) {
      userApi.login(email, password);
    },
  },
};
