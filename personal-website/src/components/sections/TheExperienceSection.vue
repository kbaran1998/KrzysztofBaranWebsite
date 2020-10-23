<template>
  <div :id="experienceData.tag">
    <h2 class="mb-5">{{experienceData.name}}</h2>
    <b-container
      class="resume-item"
      fluid
      v-for="(experience, index) in experienceData.experiences"
      :key="index">
      <b-row>
        <b-col cols="12" md="auto">
          <b-img-lazy
            :src="experience.photoSrc"
            thumbnail
            :alt="experience.company"
            width="100">
          </b-img-lazy>
        </b-col>
        <b-col>
          <div class="resume-content entryinfo">
            <h3 class="mb-0 leftappear">{{experience.company}}</h3>
            <div class="subheading mb-3 leftappear">{{experience.position}}</div>
            <ul>
              <li
                v-for="(point, index) in experience.points"
                :key="index">
                {{point}}
              </li>
            </ul>
          </div>
        </b-col>
        <b-col cols="12" md="auto" class="place-time">
          <span class="text-primary">
            {{experience.place}}<br>{{experience.from}} - {{experience.to}}
          </span>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  name: 'TheExperienceSection',
  props: {
    experienceData: {
      type: Object,
      required: true,
    },
  },
  components: {
  },
};
</script>

<style>
.resume-item {
  margin-bottom: 3rem!important;
}
.place-time {
  text-align: right;
}
</style>
