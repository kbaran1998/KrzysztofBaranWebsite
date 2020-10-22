<template>
  <b-modal id="thisModal" size="xl" hide-footer>
    <template #modal-title>
      {{title}}
    </template>
    <div class="d-block text-center">
      <slot></slot>
    </div>
    <b-button class="mt-3" block @click="$bvModal.hide('thisModal')">Close Me</b-button>
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
};
</script>
