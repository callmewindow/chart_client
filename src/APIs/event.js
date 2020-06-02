// 事件有关接口
import axios from 'axios'
import { QS } from './global'

// 获取所有事件的统计量
export const getEventNumber = () => {
  return axios({
    method: 'GET',
    url: "/visitCount",
  })
}

// 获取所有现存事件
export const getAllEvent = () => {
  return axios({
    method: 'GET',
    url: "/newsetData",
  });
}

// 获取影响力列表
export const getEffectList = () => {
  return axios({
    method: 'GET',
    url: `/api/paper/getPaperInfo`
  })
}

// 获取所有预警事件
export const getAllWarning = () => {
  return axios({
    method: 'GET',
    url: `/api/paper/getPaperInfo`
  })
}

// 获取某一事件
export const getEventById = eventId => {
  return axios({
    method: 'GET',
    url: `/api/paper/getPaperInfo?eventId=${eventId}`
  })
}

// 获取话题分布列表
export const getAllTopic = () => {
  return axios({
    method: 'GET',
    url: `/api/paper/getPaperInfo`
  })
}

// 手动上传新信息
export const uploadEvent = (newEvent) => {
  return axios({
    method: 'POST',
    url: `/api/paper/uploadPaper`,
    data: { newEvent }
  })
}

// 搜索事件
export const getEventByTitle = eventTitle => {
  return axios({
    method: 'GET',
    url: `/api/paper/getPaperInfo?eventTitle=${eventTitle}`
  })
}

// 以下为低优先级接口

// 获取现存话题关键词
export const getTopicKeyword = () => {
  return axios({
    method: 'GET',
    url: `/api/paper/getPaperInfo`
  })
}

// 获取事件关键词
export const getEventKeyword = () => {
  return axios({
    method: 'GET',
    url: `/api/paper/getPaperInfo`
  })
}