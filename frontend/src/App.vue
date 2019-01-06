<template>
  <div id="app">

    <Header/>
    <main>
      <router-view/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import Header from './components/Header/Header.vue';
import Footer from './components/Footer/Footer.vue';

export default {
  components: {
    Header,
    Footer,
  },
};

</script>

<style lang="scss" src="./style.scss"></style>
