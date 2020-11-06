<template>
  <div :id="publicationsData.tag">
    <h2 class="mb-5">{{publicationsData.name}}</h2>
    <b-container
      class="resume-item"
      fluid
      v-for="(publication, index) in publicationsData.publications"
      :key="index">
      <b-row>
        <b-col>
          <div class="resume-content entryinfo">
            <h3 class="mb-0 leftappear">{{publication.title}}</h3>
            <div class="subheading mb-3 leftappear" v-once>
              <ul>
                <li
                  v-for="(author, index) in publication.authors"
                  :key="index">
                  {{author}}
                </li>
              </ul>
            </div>
            <p>
              {{ publication.abstract }}
            </p>
            <div class="social-icons">
              <a target="_blank"
                v-for="(link, index) in publication.extraLinks"
                :key="`link-${index}`"
                :href="link.link"
                :title="link.explanation"
                v-b-tooltip.hover
              >
                <font-awesome-icon :icon="['fab', link.type]" />
              </a>
            </div>
          </div>
        </b-col>
        <b-col cols="12" md="auto" class="place-time">
          <span class="text-primary">
            {{publication.place}}<br>{{publication.published}}
          </span>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'ThePublicationsSection',
  props: {
    publicationsData: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>

</style>
