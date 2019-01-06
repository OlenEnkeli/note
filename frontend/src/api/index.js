import axios from 'axios';

const instance = axios.create({
  baseURL: '/api',
});

instance.defaults.headers.post['Content-Type'] = 'application/json';
instance.defaults.headers.patch['Content-Type'] = 'application/json';

export default instance;
