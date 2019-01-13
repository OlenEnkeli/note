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

  async login(credential) {
    try {
      await axios.post('/login', {
        email: credential.email,
        password: credential.password,
      });
      return true;
    } catch (error) {
      return false;
    }
  },

  async logout() {
    try {
      await axios.get('/logout');
      return true;
    } catch (error) {
      return false;
    }
  },

};
