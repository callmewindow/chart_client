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

// Http请求部分配置
Vue.prototype.$http = axios
// 服务器接口的地址
axios.defaults.baseURL = 'http://47.94.234.255:5000';
Vue.config.productionTip = false;

Vue.prototype.$echarts = echarts
Vue.prototype.$BMap = BMap

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
