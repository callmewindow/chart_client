import Vue from 'vue'
import Router from 'vue-router'
import PoliticsInfo from '@/pages/PoliticsInfo/PoliticsInfo'
import PolicyAnalyze from '@/pages/PolicyAnalyze/PolicyAnalyze'
import Group from '@/pages/Group/Group'
import AddMessage from '@/pages/AddMessage/AddMessage'
import test from '@/pages/test';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/Home'
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/Home',
      name: 'PoliticsInfo',
      component: PoliticsInfo
    },
    {
      path: '/PolicyAnalyze',
      name: 'PolicyAnalyze',
      component: PolicyAnalyze
    },
    {
      path: '/Group',
      name: 'Group',
      component: Group
    },
    {
      path: '/AddMessage',
      name: 'AddMessage',
      component: AddMessage
    }
    
  ]
})
