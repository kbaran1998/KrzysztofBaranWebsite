<template>
  <b-navbar toggleable="lg"
    type="dark"
    variant="info"
    class="bg-gradient-burned"
    id="sideNav">

    <div class="brandContainer">
      <b-navbar-brand id="nameDisplay">
        <h2 class="text-gradient-cold">
          <b>Krzysztof Baran</b>
        </h2>
      </b-navbar-brand>
    </div>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-img
        thumbnail
        fluid
        v-bind="profilePictureProps"
        src="../../static/KrzysztofB.jpg"
        rounded="circle"
        alt="Circle Profile Picture"
        id="profilePic">
      </b-img>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav id="links" class="sectionLink">
          <b-nav-item href="#">About</b-nav-item>
          <b-nav-item href="#">Education</b-nav-item>
          <b-nav-item href="#">Experience</b-nav-item>
          <b-nav-item href="#">Projects</b-nav-item>
          <b-nav-item href="#">Skills</b-nav-item>
          <b-nav-item href="#">Publications</b-nav-item>
          <b-nav-item href="#">Program Committees</b-nav-item>
          <b-nav-item href="#">Extracurricular Activities</b-nav-item>
          <b-nav-item href="#">Contact Me</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
  </b-navbar>
</template>

<script>
import VueResponsiveText from 'vue-responsive-text';

export default {
  components: {
    VueResponsiveText,
  },
  data() {
    return {
      profilePictureProps: {
        fluid: true,
        width: 300,
      },
    };
  },
};
</script>

<style scoped>

.sectionLink {
  font-weight: bold;
  font-size:1.1rem;
  background-image: linear-gradient(90deg, #ffffff, #adadad);
  background-size: 100%;
  background-repeat: repeat;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-background-clip: text;
  -moz-text-fill-color: transparent;
}

@media (max-width: 991px) {
  #profilePic {
    display: none;
  }
  #sideNav {
    position: absolute;
    width: 100%
  }
}
@media (min-width: 992px) {
  #sideNav {
    position: fixed;
    text-align: center;
    top: 0;
    left: 0;
    display: -webkit-box !important;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 18%;
    height: 100vh;
  }
  .brandContainer {
    display: flex;
    align-items: flex-start;
  }

  #profilePic {
    background-color: rgba(255, 255, 255, 0.2);
    border: 8px solid rgba(255, 255, 255, 0.2);
  }

  #nameDisplay {
    display: none;
  }
}

#links {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-weight: bold;
  }
</style>
