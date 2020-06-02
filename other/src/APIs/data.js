import axios from "axios"


export const getVisitCount = () => {
  return axios({
    method:'GET',
    url:"/visitCount",
  })
}

export const getNewsetData = () => {
  var result = axios({
    method:'GET',
    url:"/newsetData",
  });
  return result
}
