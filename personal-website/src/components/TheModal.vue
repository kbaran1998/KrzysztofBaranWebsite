<template>
  <b-modal id="resumeModal" hide-footer>
    <template #modal-title>
      Resume
    </template>
    <div class="d-block text-center">
      <b-loading :show="!iframeLoaded"></b-loading>
      <iframe
          src="https://onedrive.live.com/embed?cid=1038528792C40471&resid=1038528792C40471%2122966&authkey=AD11GlJdhx2w9us&em=2"
          width="476"
          height="288"
          frameborder="0"
          scrolling="yes"
          @loadeddata="iframeIsLoaded"
          >
      </iframe>
    </div>
    <b-button class="mt-3" block @click="$bvModal.hide('resumeModal')">Close Me</b-button>
  </b-modal>
</template>

<script>
export default {
  name: 'TheModal',
  data() {
    return {
      iframeLoaded: false,
    };
  },
  methods: {
    iframeIsLoaded() {
      this.iframeLoaded = true;
    },
  },
};
</script>
