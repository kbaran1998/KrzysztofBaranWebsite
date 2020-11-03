<template>
  <b-modal :id="modalId" size="xl" hide-footer>
    <template #modal-title>
      {{title}}
    </template>
    <div class="d-block">
      <slot></slot>
    </div>
    <b-button
      variant="danger"
      class="mt-3"
      block
      @click="$bvModal.hide(modalId)">
      Close Me
    </b-button>
  </b-modal>
</template>

<script>
export default {
  name: 'TheModal',
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  computed: {
    modalId() {
      return 'modal-'.concat(this.title.toLowerCase().replace(' ', '-'));
    },
  },
};
</script>
