import axios from './index';

export default {
  async getCurrentUser() {
    try {
      const user = await axios.get('/users');
      return user.data;
    } catch (error) {
      return undefined;
    }
  },
};
