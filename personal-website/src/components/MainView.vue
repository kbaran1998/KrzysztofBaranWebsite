<template>
  <div id="page-top">
    <NavBar />
    <b-container fluid class="p-0">
      <ResumeSection color="#f0f0f0" />
    </b-container>
  </div>
</template>

<script>
import NavBar from './TheNavBar';
import ResumeSection from './TheResumeSection';

export default {
  name: 'MainView',
  components: {
    NavBar,
    ResumeSection,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    };
  },
};
</script>

<style>
</style>
