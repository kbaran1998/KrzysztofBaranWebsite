<template>
  <div id="page-top">
    <NavBar />
    <b-container fluid class="p-0">
      <ResumeSection
        color="#f0f0f0"
        data-aos="fade">
        <About :aboutData="profileAbout" />
      </ResumeSection>
    </b-container>
  </div>
</template>

<script>
import NavBar from './TheNavBar';
import ResumeSection from './TheResumeSection';
import Profile from '../assets/profile.json';
import About from './sections/TheAboutSection';

export default {
  name: 'MainView',
  components: {
    NavBar,
    ResumeSection,
    About,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      profileAbout: Profile[0],
      profileEducation: Profile[1],
      profileExperience: Profile[2],
      profileProjects: Profile[3],
      profileSkills: Profile[4],
      profilePublications: Profile[5],
      profileProgramCommittees: Profile[6],
      profileExtracurricularActivities: Profile[7],
      profileContact: Profile[8],
    };
  },
};
</script>

<style>
</style>
