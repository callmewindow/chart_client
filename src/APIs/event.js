// 事件有关接口
import axios from "axios";
import { QS } from "./global";

// 获取所有现存事件
export const getAllEvent = () => {
  return axios({
    method: "GET",
    url: "/getEvents"
  });
};

// 获取单个现存事件
export const getEventById = eventId => {
  return axios({
    method: "GET",
    url: `/getOneEvent?id=${eventId}`
  });
};

// 创建新事件
export const createEvent = (labelList, title, intro, detail) => {
  return axios({
    headers: {
      "Content-Type": "application/json"
    },
    method: "POST",
    url: `/createEvent`,
    data: QS({
      labelList: labelList,
      title: title,
      synopsis: intro,
      detailSynopsis: detail,
    })
  });
};