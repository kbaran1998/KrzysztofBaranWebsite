<template>
  <div :id="activitiesData.tag">
    <h2 class="mb-5">{{activitiesData.name}}</h2>
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
