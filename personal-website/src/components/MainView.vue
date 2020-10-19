<template>
  <NavBar />
</template>

<script>
import NavBar from './TheNavBar';

export default {
  name: 'MainView',
  components: {
    NavBar,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
