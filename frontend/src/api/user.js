import axios from './index';

export default {
  async getCurrentUser() {
    const user = await axios.get('/');
    return user.data;
  },
};
