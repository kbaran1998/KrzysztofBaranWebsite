<template>
  <div id="page-top">
    <NavBar />
    <b-container fluid class="p-0">
      <ResumeSection
        color="#e8f5dc"
        data-aos="fade">
        <About :aboutData="profileAbout" />
      </ResumeSection>
      <ResumeSection
        color="#f3f5dc"
        data-aos="fade">
        <Education :educationData="profileEducation" />
      </ResumeSection>
    </b-container>
  </div>
</template>

<script>
import NavBar from './TheNavBar';
import ResumeSection from './TheResumeSection';
import ProfileData from '../assets/profile.json';
import About from './sections/TheAboutSection';
import Education from './sections/TheEducationSection';

export default {
  name: 'MainView',
  components: {
    NavBar,
    ResumeSection,
    About,
    Education,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      profileAbout: ProfileData[0],
      profileEducation: ProfileData[1],
      profileExperience: ProfileData[2],
      profileProjects: ProfileData[3],
      profileSkills: ProfileData[4],
      profilePublications: ProfileData[5],
      profileProgramCommittees: ProfileData[6],
      profileExtracurricularActivities: ProfileData[7],
      profileContact: ProfileData[8],
    };
  },
};
</script>

<style>
</style>
