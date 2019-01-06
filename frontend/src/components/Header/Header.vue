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
      <router-link v-if="!this.$store.state.user.current" to ="/signin"
        class="login">Войти</router-link>
      <div class="user__profile">
        <a class="user-name" href="#">{{this.$store.state.user.current.name}}</a>
      </div>
    </div>

  </header>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style lang ="scss" scoped src="./index.scss"></style>