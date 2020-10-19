import '@babel/polyfill';
import 'mutationobserver-shim';
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// eslint-disable-next-line import/first
import Vue from 'vue';
import './plugins/bootstrap-vue';

import App from './App';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
});
