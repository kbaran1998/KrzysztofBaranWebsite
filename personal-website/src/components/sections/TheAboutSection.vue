<template>
  <div class="contentCenter" :id="aboutData.tag">
    <div>
      <h1 class="display-1">{{aboutData.title}}</h1>
      <h4>
        <a :href="`mailto: ${aboutData.email}`">{{aboutData.email}}</a>
      </h4>
      <hr>
      <p class="lead">{{aboutData.summary}}</p>
      <b-button pill id="viewCVbtn" @click="$bvModal.show('thisModal')">Resume</b-button>
      <b-tooltip target="viewCVbtn" triggers="hover" placement="right">
        View my <b>Resume</b> here!
      </b-tooltip>
      <TheModal title="Resume">
        <iframe
          :src="aboutData.CVlink"
          width="70%"
          height="300px"
          frameborder="1"
          scrolling="yes"
          loading="lazy"
          >
        </iframe>
        <b-button class="mt-3" block v-on:click="openDownloadWindow()">Download Resume</b-button>
      </TheModal>
      <div class="social-icons">
        <a target="_blank"
          v-for="(link, index) in aboutData.socailLinks"
          :key="`link-${index}`"
          :href="link">
            <font-awesome-icon :icon="['fab', index]" />
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import TheModal from '../TheModal';

export default {
  name: 'TheAboutSection',
  props: {
    aboutData: {
      type: Object,
      required: true,
    },
  },
  components: {
    TheModal,
  },
  methods: {
    openDownloadWindow() {
      window.open(this.aboutData.CVdownloadLink, '_blank');
    },
  },
};
</script>

<style>
.contentCenter {
  display: flex;
  align-items: center;
}
.buttonLinks {
  display: flex;
  flex-direction: row;
}
.social-icons a {
    margin-top: 1.5rem;
    display: inline-block;
    height: 3.5rem;
    width: 3.5rem;
    background-color: #495057;
    color: #fff!important;
    border-radius: 100%;
    text-align: center;
    font-size: 1.5rem;
    line-height: 3.5rem;
    margin-right: 1rem;
}

#viewCVbtn {
  margin-top: 1.5rem;
}
</style>
