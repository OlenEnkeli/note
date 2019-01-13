import userApi from '../api/user';

export default {
  state: {
    current: [],
  },

  mutations: {
    setUser(state, user) {
      state.current = user;
    },
    unsetUser(state) {
      state.current = [];
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

    logout({ commit }) {
      userApi.logout();
      commit('unsetUser');
    },
  },
};
