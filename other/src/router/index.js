import Vue from 'vue'
import Router from 'vue-router'

import PoliticsInfo from '@/pages/PoliticsInfo/PoliticsInfo'
import policyAnalyze from '@/pages/policyAnalyze/policyAnalyze'
import Group from '@/pages/group/group'
import AddMes from '@/pages/addMes/addMes'
import Ping from '@/components/Ping'

Vue.use(Router)

export default new Router({
  routes: [
   
    {
      path: '/',
      name: 'PoliticsInfo',
      component: PoliticsInfo
    },
    {
      path: '/policyanalyze',
      name: 'policyAnalyze',
      component: policyAnalyze
    },
    {
      path: '/group',
      name: 'Group',
      component: Group
    },
    {
      path: '/addmes',
      name: 'AddMes',
      component: AddMes
    },
  ],
  mode: 'history'
})
