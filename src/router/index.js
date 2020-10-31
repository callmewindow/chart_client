import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/Home'
    },
    {
      path: '/Home',
      name: 'PoliticsInfo',
      component: () => import('@/pages/PoliticsInfo/PoliticsInfo')
    },
    {
      path: '/PolicyAnalyze',
      name: 'PolicyAnalyze',
      component: () => import('@/pages/PolicyAnalyze/PolicyAnalyze')
    },
    // {
    //   path: '/Group',
    //   name: 'Group',
    //   component: () => import('@/pages/Group/Group')
    // },
    {
      path: '/Group/:eventId',
      name: 'Group',
      component: () => import('@/pages/Group/Group')
    },
    {
      path: '/AddMessage',
      name: 'AddMessage',
      component: () => import('@/pages/AddMessage/AddMessage')
    }
    
  ]
})
