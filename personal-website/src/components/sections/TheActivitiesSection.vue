<template>
  <div :id="activitiesData.tag">
    <h2 class="mb-5">{{activitiesData.name}}</h2>
    <b-container
      class="resume-item"
      fluid
      v-for="(activity, index) in activitiesData.activities"
      :key="index">
      <b-row>
        <b-col md="auto">
          <b-img-lazy
            :src="activity.src"
            thumbnail
            :alt="activity.organisation"
            width="100">
          </b-img-lazy>
        </b-col>
        <b-col>
          <div class="resume-content entryinfo">
            <h3 class="mb-0 leftappear">{{ activity.organisation }}</h3>
            <div class="subheading mb-3 leftappear">{{ activity.activity }}</div>
          </div>
        </b-col>
        <b-col md="auto" class="place-time">
          <span class="text-primary">
            {{activity.place}}<br>{{activity.from}}-{{activity.to}}
          </span>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'TheActivitiesSection',
  props: {
    activitiesData: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>

</style>
