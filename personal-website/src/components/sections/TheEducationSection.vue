<template>
  <div :id="educationData.tag">
    <h2 class="mb-5">{{educationData.name}}</h2>
    <b-container
      class="resume-item"
      fluid
      v-for="(school, index) in educationData.schools"
      :key="index">
      <b-row>
        <b-col cols="12" md="auto">
          <b-img-lazy
            :src="school.photoSrc"
            thumbnail
            :alt="school.name"
            width="100">
          </b-img-lazy>
        </b-col>
        <b-col>
          <div class="resume-content entryinfo">
            <h3 class="mb-0 leftappear">{{school.name}}</h3>
            <div class="subheading mb-3 leftappear">{{school.study}}</div>
            <div>{{school.description}}</div>
          </div>
        </b-col>
        <b-col cols="12" md="auto" class="place-time">
          <span class="text-primary">{{school.place}}<br>{{school.from}} - {{school.to}}</span>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  name: 'TheEducationSection',
  props: {
    educationData: {
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
