<template>
  <div :id="educationData.tag">
    <h2 class="mb-5">{{educationData.name}}</h2>
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

</style>
