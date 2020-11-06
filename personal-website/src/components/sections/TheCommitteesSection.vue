<template>
  <div :id="committeesData.tag">
    <h2 class="mb-5">{{committeesData.name}}</h2>
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
