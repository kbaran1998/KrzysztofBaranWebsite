<template>
  <div :id="projectsData.tag">
    <h2 class="mb-5">{{projectsData.name}}</h2>
    <b-card
      title="Robyn Chatbot"
      img-src="../../../static/projects/robynChatBot/robynLogo.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2 border border-primary projectCard"
    >
      <b-card-text>
      A counselling Chatbot (powered by machine learning) made for Police Officers
       who are struggling with mental or work related issues they
       cannot discuss with their colleagues or family.
      </b-card-text>
      <b-button variant="primary" pill @click="$bvModal.show('modal-project')">
        More Info
      </b-button>
      <TheModal title="Project">
        <div>
          Hello!
        </div>
      </TheModal>
    </b-card>
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
};
</script>

<style>
.projectCard {
  border-width: medium medium medium !important;
}

.card-img .card-img-top .card-img-bottom {
  width: 60% !important;
}
</style>
