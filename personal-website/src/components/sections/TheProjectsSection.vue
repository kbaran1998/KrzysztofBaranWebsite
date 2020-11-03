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
        <b-avatar
          v-for="(tech, index) in project.technologies"
          :key="index"
          size="2em"
          v-b-tooltip.hover
          :title="tech.name"
          :src="tech.link">
        </b-avatar>
        <br>
        <br>
        <b-button
          variant="outline-success"
          pill
          class="info-button"
          @click="$bvModal.show('modal-'.concat(createTagText(project.name)))">
          Gallery
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
            <h3>Description</h3>
            <p>{{ project.description }}</p>
            <h3>Technologies</h3>
            <b-avatar
              v-for="(tech, index) in project.technologies"
              :key="index"
              size="5em"
              v-b-tooltip.hover
              :title="tech.name"
              :src="tech.link">
            </b-avatar>
            <h3 v-if="project.links">Links</h3>
            <div v-if="project.links" class="social-icons">
              <a target="_blank"
                v-for="(link, index) in project.links"
                :key="`link-${index}`"
                :href="link.link"
                v-b-tooltip.hover
                :title="link.link">
                  <font-awesome-icon :icon="['fab', createTagText(link.type)]" />
              </a>
            </div>
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
    createTagText(text) {
      return text.toLowerCase().replace(' ', '-');
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
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  align-items: center;
}
.cards-container > article {
  margin: 10px;
  margin-bottom: 10px;
}
.card-title {
  font-weight: bold;
  color:yellow;
}

.info-button {
  margin-top: 10px;
  position:absolute;
  bottom:1px;
}

.b-avatar-img {
  border: 4px solid aqua;
}
</style>
