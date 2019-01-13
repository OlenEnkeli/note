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
      state.current = undefined;
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
      commit('unsetUser');
      userApi.logout();
    },
  },
};
