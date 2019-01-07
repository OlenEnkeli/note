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
      <div class="user__profile" v-if="!this.$store.state.user.current">
        <a class="user-name" href="#">{{this.$store.state.user.current.name}}</a>
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
};
</script>

<style lang ="scss" scoped src="./index.scss"></style>