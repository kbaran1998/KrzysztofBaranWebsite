<template>
  <div id="page-top">
    <NavBar />
    <b-container fluid class="p-0">
      <ResumeSection
        v-for="profile in profileData"
        :key="profile.tag"
        :id="profile.tag"
        color="#f0f0f0"
        data-aos="fade">
        <h1>{{ profile.name }}</h1>
      </ResumeSection>
    </b-container>
  </div>
</template>

<script>
import NavBar from './TheNavBar';
import ResumeSection from './TheResumeSection';
import Profile from '../assets/profile.json';

export default {
  name: 'MainView',
  components: {
    NavBar,
    ResumeSection,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      profileData: Profile,
    };
  },
};
</script>

<style>
</style>
