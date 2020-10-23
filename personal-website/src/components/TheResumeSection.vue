<template>
  <section
    :style="{ backgroundColor: color }"
    class="resume-section p-3 p-lg-5 d-flex d-column"
    data-metatip="true"
    data-selected="true"
    data-label-id="0">
    <slot></slot>
    <hr>
  </section>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: '#ffffff',
    },
  },
};
</script>

<style scoped>
 @media (min-width: 992px) {
  section.resume-section {
    padding-top: 3rem!important;
    padding-bottom: 3rem!important;
  }
 }
 .resume-section {
    padding-top: 5rem!important;
    padding-bottom: 5rem!important;
    max-width: 100%;
    height: 100vh;
    color:#868e96;
    display: flex;
    gap: normal;
    line-height: 24px;
    padding: 48px;
    text-align: left;
 }
 @media (min-width: 992px) {
  .resume-section {
    margin-left: 18%;
  }
 }
</style>
