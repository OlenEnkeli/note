<template>
  <div class="home">
    <section class="light about-us">
      <h1>Немного о нас</h1>
      <h2>Привет, мы MoonSolution - команда разработчиков-энтузиастов в духе rock`n`roll. </h2>
      <h2>Мы здесь, чтобы решить вашу проблему. </h2>
      <br><br><br><br><br><br><br><br><br><br><br>
    </section>
    <section class="dark kind">
      <h1>Вот, что мы можем</h1>
      <br><br><br><br><br><br><br><br><br><br><br><br><br>
    </section>

    <section class="light">
      <h1>Something another 2</h1>
      <h1>Немного о нас</h1>
      <h2>Привет, мы MoonSolution - команда разработчиков-энтузиастов в духе rock`n`roll. </h2>
      <h2>Мы здесь, чтобы решить вашу проблему. </h2>
      <br><br><br><br><br><br><br><br><br>
    </section>
  </div>
</template>


<style scoped lang="scss">
section {
  padding: 60px 30px;
  margin: 0;
  color: #F8F8F8;

  h1 {
    font-weight: 300;
    font-size: 1.9em;
    text-align: center;
    margin-bottom: 27px;
  }

  h2 {
    text-align: center;
    font-weight: 100;
    font-size: 1.3em;
    margin-bottom: 15px;
  }


  &.light {
    background-color: #F8F8F8;
    color: #2A2B2B;
  }

  &.dark {
    background-color: #1f1f1f;
    color: #F8F8F8;
  }
}
</style>

<script>
export default {
  name: 'home',
};
</script>
