// 首页柱状图数据结构
// source:网站名称
// id:网站id
// topictList {  //不同事件的访问量的数据合集
// "topict": "事件名称",
// "total": "访问量"
// }

const topic = {
	"message": "请求成功",
	"code": 200,
	"success": true,
	"data": {
		"totalRows": 4,
		"resultList": [
			{
				"source": "facebook",
				"id": "1",
				"topictList": [{
					"topict": "美警暴力执法",
					"total": "542"
				}, {
					"topict": "华盛顿雕像推倒",
					"total": "121"
				}]
			},{
				"source": "twitter",
				"id": "1",
				"topictList": [{
					"topict": "美警暴力执法",
					"total": "842"
				}, {
					"topict": "华盛顿雕像推倒",
					"total": "321"
				}]
			}
		]
	}
}
export default topic