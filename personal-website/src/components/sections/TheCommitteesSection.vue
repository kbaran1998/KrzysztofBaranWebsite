<template>
  <div :id="committeesData.tag">
    <h2 class="mb-5">{{committeesData.name}}</h2>
    <b-container
      class="resume-item"
      fluid
      v-for="(committee, index) in committeesData.committees"
      :key="index">
      <b-row>
        <b-col md="auto">
          <b-img-lazy
            :src="committee.src"
            thumbnail
            :alt="committee.organisation"
            width="100">
          </b-img-lazy>
        </b-col>
        <b-col>
          <div class="resume-content entryinfo">
            <h3 class="mb-0 leftappear">{{ committee.organisation }}</h3>
            <div class="subheading mb-3 leftappear">{{ committee.position }}</div>
          </div>
        </b-col>
        <b-col md="auto" class="place-time">
          <span class="text-primary">
            {{committee.place}}<br>{{committee.year}}
          </span>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'TheCommitteesSection',
  props: {
    committeesData: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>

</style>
