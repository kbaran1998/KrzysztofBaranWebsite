<template>
  <b-navbar
    toggleable="lg"
    type="dark"
    class="navbar-horizontal bg-gradient-warm"
    id="sideNav"
  >
    <div class="brandContainer">
    <b-navbar-brand id="nameDisplay">
      <h2 class="text-gradient-cold">
        <b>Krzysztof Baran</b>
      </h2>
    </b-navbar-brand>
    </div>
    <div class="profileLinksContainer">
      <b-img
        thumbnail
        fluid
        v-bind="profilePictureProps"
        src="../../static/KrzysztofB.jpg"
        rounded="circle"
        alt="Circle Profile Picture"
        id="profilePic">
      </b-img>
      <div id="links">
        <b-link href="#" class="sectionLink boring">About</b-link>
        <b-link href="#" class="sectionLink">Education</b-link>
        <b-link href="#" class="sectionLink">Experience</b-link>
        <b-link href="#" class="sectionLink">Projects</b-link>
        <b-link href="#" class="sectionLink">Skills</b-link>
        <b-link href="#" class="sectionLink">Publications</b-link>
        <b-link href="#" class="sectionLink">Program Committees</b-link>
        <b-link href="#" class="sectionLink">Extracurricular Activities</b-link>
      </div>
    </div>
  </b-navbar>
</template>

<script>
export default {
  data() {
    return {
      profilePictureProps: {
        fluid: true,
        width: 200,
        height: 200,
      },
    };
  },
};
</script>

<style scoped>

.sectionLink {
  font-weight: bold;
  color: white;
}

@media (max-width: 992px) {
  #profilePic {
    width: 25px;
    height: 25px;
  }
}
@media (min-width: 992px) {
  #sideNav {
    text-align: center;
    position: fixed;
    top: 0;
    left: 0;
    display: -webkit-box !important;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 17rem;
    height: 100vh;
  }
  .brandContainer {
    display: flex;
    align-items: flex-start;
  }
  .profileLinksContainer {
    margin-top: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  #links {
    margin-top: 25px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}
</style>
