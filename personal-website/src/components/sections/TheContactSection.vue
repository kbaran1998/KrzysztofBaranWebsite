<template>
  <div :id="contactData.tag">
    <h2 class="mb-5">{{contactData.name}}</h2>
  </div>
</template>

<script>

/* https://www.emailjs.com/docs/examples/vuejs/
  https://www.freecodecamp.org/news/send-emails-from-your-vue-application/
*/

export default {
  name: 'TheContactSection',
  props: {
    contactData: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>

</style>
