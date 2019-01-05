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
    <div class="user-menu">
      <router-link to ="/signin">Войти</router-link>
    </div>

  </header>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style lang ="scss" scoped src="./index.scss"></style>