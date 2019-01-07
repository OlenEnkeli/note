<template>
  <div class="home">
    <section class="light about-us">
      <h1>Немного о нас</h1>
      <h2>Привет, мы MoonSolution - команда разработчиков-энтузиастов в духе rock`n`roll. </h2>
      <h2>Мы здесь, чтобы решить вашу проблему. </h2>
      <div class="wrapper">
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-heart"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-globe"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-ok"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-home"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
      </div>
    </section>
    <section class="dark kind">
      <h1>Вот, что мы можем</h1>
            <div class="wrapper">
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-heart"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-globe"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-ok"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-home"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
      </div>
    </section>

    <section class="light">
      <h1>Something another 2</h1>
      <h1>Немного о нас</h1>
      <h2>Привет, мы MoonSolution - команда разработчиков-энтузиастов в духе rock`n`roll. </h2>
      <h2>Мы здесь, чтобы решить вашу проблему. </h2>
            <div class="wrapper">
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-heart"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-globe"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-ok"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
        <div>
          <h2>Персонализация</h2>
          <div class="icon icon-home"></div>
          <p>И вот, почему мы делаем это с любовью и всем таким - ...</p>
        </div>
      </div>
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

  .wrapper {
    display: flex;
    margin: 80px 0 20px 0;

    div {
      margin: 0 20px;
      text-align: center;

      h2 {
        font-size: 1.3rem;
        text-transform: uppercase;
      }

      .icon {
        font-size: 7rem;
      }

    }
  }
}
</style>

<script>
export default {
  name: 'home',
};
</script>
