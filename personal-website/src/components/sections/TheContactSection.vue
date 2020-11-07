<template>
  <div :id="contactData.tag">
    <div class="contacts">
      <h2 class="mb-5">{{contactData.name}}</h2>
      <b-tabs content-class="mt-3" align="center">
        <b-tab title="Email" active>
          <b-button
            target="_blank"
            variant="outline-primary"
            :href="`mailto:${contactData.email}`"
            :title="contactData.email"
            v-b-tooltip.hover
          >
            <h3>Send me an email</h3>
            <a target="_blank">
              <font-awesome-icon
                :icon="['fa', 'envelope']"
              />
            </a>
          </b-button>
        </b-tab>
        <b-tab title="Message">
          <b-button variant="primary">
            Send
          </b-button>
        </b-tab>
        <b-tab title="LinkedIn">
          <b-button
            variant="outline-primary"
            target="_blank"
            :href="contactData.linkedin"
          >
            <h3>Connect on LinkedIn</h3>
            <a>
              <font-awesome-icon
                :icon="['fab', 'linkedin']"
              />
            </a>
          </b-button>
        </b-tab>
      </b-tabs>
    </div>
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
.contacts {
  width: 100%;
}
</style>
