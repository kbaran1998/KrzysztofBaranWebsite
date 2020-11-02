<template>
  <div :id="projectsData.tag">
    <h2 class="mb-5">{{projectsData.name}}</h2>
    <div class="cards-container">
    <b-card
      v-for="(project, index) in projectsData.projects"
      :key="index"
      :title="project.name"
      :img-src="project.mainPhotoSrc"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2 border border-primary projectCard text-gradient-cold"
    >
      <b-card-text class="description-text">
        {{ project.description }}
      </b-card-text>
      <b-button
        variant="primary"
        pill
        class="info-button"
        @click="$bvModal.show('modal-'.concat(project.name.toLowerCase().replace(' ', '-')))">
        More Info
      </b-button>
      <TheModal :title="project.name">
        <div>
          <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <b-carousel-slide
        v-for="(photo, index) in project.photos"
        :key="index"
        :img-src="photo"
        class="carousel-image"
        img-width="600"
        img-height="auto"
      ></b-carousel-slide>
    </b-carousel>
        </div>
      </TheModal>
    </b-card>
    </div>
  </div>
</template>

<script>
import TheModal from '../TheModal';

export default {
  name: 'TheProjectSection',
  props: {
    projectsData: {
      type: Object,
      required: true,
    },
  },
  components: {
    TheModal,
  },
  data() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
  },
};
</script>

<style>
.projectCard {
  border-width: medium medium medium !important;
}

.card-img .card-img-top .card-img-bottom {
  width: 60% !important;
}

.description-text {
  color: aliceblue;
}

.cards-container {
  display: inline-flex;
  flex-wrap: wrap;
}
.cards-container > div {
  margin: 6px;
}
.info-button {
  position:absolute;
  bottom:3px;
}
.card-title {
  font-weight: bold;
  color:yellow;
}
</style>
