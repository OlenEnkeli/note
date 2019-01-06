import userApi from '../api/user';

export default {
  state: {
    users: [],
    current: [],
  },

  mutations: {
    setUser(state, user) {
      state.current = user;
    },
  },

  actions: {
    getCurrentUser({ commit }) {
      const current = userApi.getCurrentUser();
      current.then((user) => {
        commit('setUser', user);
      });

    },
  },
};
