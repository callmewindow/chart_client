// 首页访问量数据
//type:类型   type=1、网站的访问量		type=2  不同语言的访问量
// source：名称
// total:访问量

const visitCount = {
	"message": "请求成功",
	"code": 200,
	"success": true,
	"data": {
		"totalRows": 21524,
		"resultList": [{
			"type": "1",
			"source": "纵览中国",
			"total": "487"
		}, {
			"type": "1",
			"source": "中国慧闻网",
			"total": "769"
		}, {
			"type": "1",
			"source": "新世纪新闻网",
			"total": "443"
		}, {
			"type": "1",
			"source": "中国瞭望",
			"total": "483"
		}, {
			"type": "1",
			"source": "腾讯",
			"total": "703"
		}, {
			"type": "1",
			"source": "网络游戏",
			"total": "224"
		}, {
			"type": "2",
			"source": "英语",
			"total": "887"
		}, {
			"type": "2",
			"source": "图片",
			"total": "897"
		}, {
			"type": "2",
			"source": "音视频",
			"total": "954"
		}, {
			"type": "2",
			"source": "文本",
			"total": "323"
		}]
	}
}
export default visitCount