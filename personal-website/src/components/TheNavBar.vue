<template>
  <b-navbar
    toggleable="lg"
    type="dark"
    class="navbar-horizontal"
    id="sideNav"
  >
    <b-navbar-brand href="#">Krzysztof Baran</b-navbar-brand>
  </b-navbar>
</template>

<script>
export default {};
</script>

<style scoped>
@media (min-width: 992px) {
  #sideNav {
    text-align: center;
    position: fixed;
    top: 0;
    left: 0;
    display: -webkit-box !important;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 17rem;
    height: 100vh;
  }
  #header h1 {
    margin: 0px;
  }
}
</style>

<style lang="scss">
  $green: rgba(177,240,10,1);
  $orange: rgb(189, 147, 56);

  $list1: $green, $orange;
  @mixin gradient($direction, $list) {
    background: -webkit-linear-gradient($direction, $list);
    background: -moz-linear-gradient($direction, $list);
    background: -o-linear-gradient($direction, $list);
    background: linear-gradient($direction, $list);
  }
  #sideNav {
    @include gradient(right, $list1);
  }
</style>
