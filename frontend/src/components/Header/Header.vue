<template>
  <header>
    <div class="logo">
      <router-link to="/"><span>Moon</span>Solution</router-link>
    </div>
    <nav>
        <router-link to="/">Главная</router-link>
        <router-link to="/about">Портфолио</router-link>
        <a href="#">Отзывы</a>
        <a href="#">Сделать заказ</a>
    </nav>

    <div class="user">
      <div class="user__profile" v-if="this.$store.state.user.current">
        <a class="user-name" href="#" >{{this.$store.state.user.current.name}}</a>
        <div class="user__profile__menu">
          <a href="#"><span>Профиль</span></a>
          <a href="#"><span>Мои заказы</span></a>
          <a href="#"><span>Что-то еще</span></a>
          <a href="#" v-on:click="logout()"><span class="exit">Выйти</span></a>
        </div>
      </div>
      
      <router-link  to ="/signin" v-else class="login">
        <div class="circle">
          <span class="icon arrow"></span>
        </div>
        <p class="button-text">Войти</p>
      </router-link>
    </div>

  </header>
</template>

<script>
export default {
  name: 'Header',

  methods: {
    logout: function() {
      this.$store.dispatch('logout').then(
        () => {
          this.$router.push({'name' : 'home'});
        }
      );
    },
  }

};
</script>

<style lang ="scss" scoped src="./index.scss"></style>