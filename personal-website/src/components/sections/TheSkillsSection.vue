<template>
  <div :id="skillsData.tag">
    <div>
      <h2 class="mb-5">{{skillsData.name}}</h2>
      <div class="bubles-container">
        <b-avatar
          v-for="(skill, index) in skillsData.skills"
          :key="index"
          :size="bubbleSize"
          class="bubble"
          v-b-tooltip.hover
          :title="skill.name"
          :src="skill.link"
          >
        </b-avatar>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheSkillsSection',
  props: {
    skillsData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      bubbleSize: '5rem',
    };
  },
};
</script>

<style>
.bubble > .b-avatar-img {
  border: 5px solid rgb(123, 255, 0);
}

.bubles-container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  align-items: center;
}

.bubles-container > .bubble {
  margin: 2rem;
  margin-bottom: 10px;
}
</style>
