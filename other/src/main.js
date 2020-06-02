
import Vue from 'vue'
import App from './App'
import router from './router'
import echarts from 'echarts'
import axios from "axios"
import VueAwesomeSwiper from 'vue-awesome-swiper'
import Element from 'element-ui';
// import BMap from "bmap"
import $ from 'jquery'



// require styles

import 'swiper/dist/css/swiper.css'
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Element, { size: 'small', zIndex: 3000 });
Vue.use(VueAwesomeSwiper)
// Vue.use(BMap)
Vue.prototype.$http = axios
// axios.defaults.baseURL = 'http://120.53.13.124:5000'
axios.defaults.baseURL = 'http://127.0.0.1:5000'

Vue.prototype.$echarts = echarts
Vue.prototype.$BMap = BMap


Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
