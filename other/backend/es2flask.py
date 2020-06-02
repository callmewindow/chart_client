from elasticsearch import Elasticsearch


# elasticsearch集群服务器的地址
ES = [
    '127.0.0.1:9200'
]

# 创建elasticsearch客户端
es = Elasticsearch(
    ES,
    # 启动前嗅探es集群服务器
    sniff_on_start=True,
    # es集群服务器结点连接异常时是否刷新es节点信息
    sniff_on_connection_fail=True,
    # 每60秒刷新节点信息
    sniffer_timeout=60
)

map = {
            "properties":{
                "id": {"type":"integer"},
				"grade": {"type":"integer"},
				"type": {"type":"integer"},
				'address': {"type":'text'},
				"title": {"type":'text'},
				"longitude": {"type":'text'},
				"latitude": {"type":'text'},
				"number":{"type":"integer"},
				"synopsis":{"type":'text'},
 				'detailsynopsis':{"type":'text'},
				"createTime": {"type":'data'},
				"keyWord": {"type":'text'},
				"labelWord": {"type":'text'},
				"impactIndicators": {"type":'text'},
				'relation':{
						'name':  {"type":'text'},
						'value':  {"type":'text'},
						'type':  {"type":'text'},
						"effectList": {
							"selfMediaPopularity": {"type":"integer"},
							"selfMediaParticipation": {"type":"integer"},
							"emotional": {"type":"integer"},
							"liveness": {"type":"integer"},
							"clicks": {"type":"integer"},
							"trafficVolume": {"type":"integer"},
							"forwardingVolume": {"type":"integer"},
							"dateTime": {"type":"data"}
						},
						'relationDetail':{
   							"node":{
                                'name': {"type":'text'},
								'symbolSize': {"type":'text'},
								'category': {"type":'integer'}
							},
							"categories":{
								"name":{"type":'text'}
							},
							'relation':{
								"source":{"type":'integer'},
								"target":{"type":'integer'}
							}
						}
				}

            }
        }

es.indices.put_mapping(index="database", body=map, ignore=400, doc_type='test')
data = {
					"id": "1",
					"grade": "1",
					"type": "1",
					'address': '香港',
					"title": "航空界机场集会",
					"longitude": "113.927056",
					"latitude": "22.302855",
					"number": "60",
					"synopsis": "香港航空界人士星期五（7月26日）在香港国际机场集会抗议，要求政府立即回应市民的五大诉求。",
					'detailsynopsis': "香港航空界人士星期五（7月26日）在香港国际机场集会抗议，要求政府立即回应市民的五大诉求，争取国际关注。集会从下午1时开始一直持续到晚上，抗议者身着黑色衣服，很多人还带着口罩，在香港国际机场一号客运大楼五楼的接机大堂静坐。示威者高举“接良知HK726”，“林郑下台”、“香港人加油”等横幅。 一些示威者将印有中英文的有关反送中运动的传单分发给入境的外国旅客。机场当局表示，机场运作未受影响，但建议旅客提前前往机场，预留充裕的时间，并留意最新航班资讯。",
					"createTime": "2019-07-26",
					"keyWord": "機場,五大诉求,集會,7月26日,抗议",
					"labelWord": "群体性时间",
					"impactIndicators": "83.6",
					'relation': [
						{
						'name': 'facebook',
						'value': '1',
						'type': 1,
						"effectList": [
							{
							"selfMediaPopularity": ["39", '56'],
							"selfMediaParticipation": ["13", '23'],
							"emotional": ['30', '50'],
							"liveness": ['29', '49'],
							"clicks": ["12", '18'],
							"trafficVolume": ["23", '43'],
							"forwardingVolume": ["28", '8'],
							"dateTime": "2019-07-26"
						},
							{
							"selfMediaPopularity": ["42", '58'],
							"selfMediaParticipation": ["30", '39'],
							"emotional": ['40', '60'],
							"liveness": ['39', '59'],
							"clicks": ["22", '28'],
							"trafficVolume": ["33", '53'],
							"forwardingVolume": ["38", '18'],
							"dateTime": "2019-07-27"
						},
							{
							"selfMediaPopularity": ["48", '49'],
							"selfMediaParticipation": ["40", '50'],
							"emotional": ['45', '65'],
							"liveness": ['44', '63'],
							"clicks": ["27", '33'],
							"trafficVolume": ["38", '58'],
							"forwardingVolume": ["43", '23'],
							"dateTime": "2019-07-28"
						},
							{
							"selfMediaPopularity": ["32", '25'],
							"selfMediaParticipation": ["29", '23'],
							"emotional": ['23', '53'],
							"liveness": ['32', '51'],
							"clicks": ["15", '18'],
							"trafficVolume": ["26", '46'],
							"forwardingVolume": ["19", '15'],
							"dateTime": "2019-07-29"
						}
						],
						'relationDetail':{
							'node': [
									{
								'name': 'Alvin3456789',
								'symbolSize': 17.5,
								'category': 1
							},
								{
									'name': 'alvinyeungnk',
									'symbolSize': 19.75,
									'category': 1
								},
								{
									'name': 'Andychanhotin',
									'symbolSize': 20.5,
									'category': 1
								},
								{
									'name': 'anti_elab',
									'symbolSize': 57.249996,
									'category': 1
								},
								{
									'name': 'antKuga',
									'symbolSize': 11.5,
									'category': 1
								},
								{
									'name': 'charlesmok',
									'symbolSize': 59.5,
									'category': 1
								},
								{
									'name': 'cheesindave',
									'symbolSize': 53.5,
									'category': 1
								},
								{
									'name': 'mike',
									'symbolSize': 0,
									'category': 1
								},
								{
									'name': 'chrlcg',
									'symbolSize': 66.25,
									'category': 1
								},
								{
									'name': 'civicpartyhk',
									'symbolSize': 19.75,
									'category': 1
								},
								{
									'name': 'CivicPassion',
									'symbolSize': 10.75,
									'category': 1
								},
								{
									'name': 'claudiamcmo',
									'symbolSize': 29.5,
									'category': 1
								},
								{
									'name': 'cowcfj',
									'symbolSize': 25.0,
									'category': 1
								},
								{
									'name': 'danceroy1',
									'symbolSize': 10.0,
									'category': 1
								},
								{
									'name': 'Demosisto',
									'symbolSize': 43.0,
									'category': 1
								},
								{
									'name': 'dopjcs8kzsj6w8r',
									'symbolSize': 57.249996,
									'category': 1
								},
								{
									'name': 'Dr_ming_13',
									'symbolSize': 20.5,
									'category': 1
								},
								{
									'name': 'EricCheungwc',
									'symbolSize': 55.75,
									'category': 1
								},
								{
									'name': 'Fight4HongKong',
									'symbolSize': 54.25,
									'category': 1
								},
								{
									'name': 'galileocheng',
									'symbolSize': 62.5,
									'category': 1
								},
								{
									'name': 'gaoyu200812',
									'symbolSize': 55.75,
									'category': 1
								},
								{
									'name': 'Hk60740379Hk',
									'symbolSize': 24.25,
									'category': 1
								},
								{
									'name': 'HKA1989',
									'symbolSize': 55.75,
									'category': 1
								},
								{
									'name': 'hkaffairs',
									'symbolSize': 15.25,
									'category': 1
								},
								{
									'name': 'HKFS1958',
									'symbolSize': 46.75,
									'category': 1
								},
								{
									'name': 'hkindigenous',
									'symbolSize': 15.25,
									'category': 1
								},
								{
									'name': 'HKNationalFront',
									'symbolSize': 27.25,
									'category': 1
								},
								{
									'name': 'hknationalparty',
									'symbolSize': 29.5,
									'category': 1
								},
								{
									'name': 'hkpeanutnews',
									'symbolSize': 13.75,
									'category': 1
								},
								{
									'name': 'HongKongFP',
									'symbolSize': 39.25,
									'category': 1
								},
								{
									'name': 'HongKongHermit',
									'symbolSize': 45.25,
									'category': 1
								},
								{
									'name': 'initiumnews',
									'symbolSize': 68.5,
									'category': 1
								},
								{
									'name': 'jeffreychngo',
									'symbolSize': 37.0,
									'category': 1
								},
								{
									'name': 'joshuawongcf',
									'symbolSize': 78.25,
									'category': 1
								},
								{
									'name': 'KitLeeCaptain',
									'symbolSize': 22.0,
									'category': 1
								},
								{
									'name': 'leetasizan',
									'symbolSize': 26.25,
									'category': 1
								},
								{
									'name': 'liuyun2018',
									'symbolSize': 53.5,
									'category': 1
								},
								{
									'name': 'lO90F0s4rLSGNxN',
									'symbolSize': 32.5,
									'category': 1
								},
								{
									'name': 'lokinhei',
									'symbolSize': 73.0,
									'category': 1
								},
								{
									'name': 'ManYuen_Ng',
									'symbolSize': 28.0,
									'category': 1
								},
								{
									'name': 'mizrdg',
									'symbolSize': 27.25,
									'category': 1
								},
								{
									'name': 'mzbs212',
									'symbolSize': 19.75,
									'category': 1
								},
								{
									'name': 'nathanlawkc',
									'symbolSize': 55.75,
									'category': 1
								},
								{
									'name': 'kevin',
									'symbolSize': 0,
									'category': 1
								},
								{
									'name': 'peter13690',
									'symbolSize': 38.5,
									'category': 1
								},
								{
									'name': 'PeterPan_da',
									'symbolSize': 17.5,
									'category': 1
								},
								{
									'name': 'PocFriends',
									'symbolSize': 34.0,
									'category': 1
								},
								{
									'name': 'rachel_cheung1',
									'symbolSize': 49.75,
									'category': 1
								},
								{
									'name': 'ray_slowbeat',
									'symbolSize': 71.5,
									'category': 1
								},
								{
									'name': 'rhokilpatrick',
									'symbolSize': 41.5,
									'category': 1
								},
								{
									'name': 'RZLHK',
									'symbolSize': 100.0,
									'category': 1
								},
								{
									'name': 'sabaocean',
									'symbolSize': 64.75,
									'category': 1
								},
								{
									'name': 'sanzhao4',
									'symbolSize': 50.5,
									'category': 1
								},
								{
									'name': 'serika_sino',
									'symbolSize': 12.25,
									'category': 1
								},
								{
									'name': 'studentlocalism',
									'symbolSize': 12.25,
									'category': 1
								},
								{
									'name': 'sumlokkei',
									'symbolSize': 21.25,
									'category': 1
								},
								{
									'name': 'szeyan1220',
									'symbolSize': 45.25,
									'category': 1
								},
								{
									'name': 'tess731',
									'symbolSize': 10.75,
									'category': 1
								},
								{
									'name': 'TonyChungHonLam',
									'symbolSize': 18.25,
									'category': 1
								},
								{
									'name': 'ttingxiao',
									'symbolSize': 46.75,
									'category': 1
								},
								{
									'name': 'VivienneChow',
									'symbolSize': 64.75,
									'category': 1
								},
								{
									'name': 'VOAHK',
									'symbolSize': 59.5,
									'category': 1
								},
								{
									'name': 'wd3qtioghikts7j',
									'symbolSize': 13.75,
									'category': 1
								},
								{
									'name': 'wildwong',
									'symbolSize': 42.25,
									'category': 1
								},
								{
									'name': 'XiaosongWangUSA',
									'symbolSize': 25.0,
									'category': 1
								},
								{
									'name': 'XinqiSu',
									'symbolSize': 52.0,
									'category': 1
								},
								{
									'name': 'yauwaiching',
									'symbolSize': 46.0,
									'category': 1
								},
								{
									'name': 'zhanglifan',
									'symbolSize': 67.0,
									'category': 1
								}
							],
							'categories': [{
								"name": "航空界机场集会"
							},
							],
							'relation': [{
								'source': 20,
								'target': 0
							},
								{
									'source': 9,
									'target': 0
								},
								{
									'source': 29,
									'target': 1
								},
								{
									'source': 39,
									'target': 1
								},
								{
									'source': 42,
									'target': 1
								},
								{
									'source': 48,
									'target': 1
								},
								{
									'source': 5,
									'target': 1
								},
								{
									'source': 8,
									'target': 1
								},
								{
									'source': 9,
									'target': 1
								},
								{
									'source': 29,
									'target': 11
								},
								{
									'source': 48,
									'target': 11
								},
								{
									'source': 60,
									'target': 11
								},
								{
									'source': 20,
									'target': 12
								},
								{
									'source': 40,
									'target': 12
								},
								{
									'source': 65,
									'target': 12
								},
								{
									'source': 27,
									'target': 14
								},
								{
									'source': 29,
									'target': 14
								},
								{
									'source': 31,
									'target': 14
								},
								{
									'source': 32,
									'target': 14
								},
								{
									'source': 33,
									'target': 14
								},
								{
									'source': 39,
									'target': 14
								},
								{
									'source': 42,
									'target': 14
								},
								{
									'source': 48,
									'target': 14
								},
								{
									'source': 8,
									'target': 14
								},
								{
									'source': 9,
									'target': 14
								},
								{
									'source': 0,
									'target': 15
								},
								{
									'source': 16,
									'target': 15
								},
								{
									'source': 19,
									'target': 15
								},
								{
									'source': 20,
									'target': 15
								},
								{
									'source': 21,
									'target': 15
								},
								{
									'source': 26,
									'target': 15
								},
								{
									'source': 30,
									'target': 15
								},
								{
									'source': 31,
									'target': 15
								},
								{
									'source': 33,
									'target': 15
								},
								{
									'source': 34,
									'target': 15
								},
								{
									'source': 36,
									'target': 15
								},
								{
									'source': 39,
									'target': 15
								},
								{
									'source': 42,
									'target': 15
								},
								{
									'source': 5,
									'target': 15
								},
								{
									'source': 50,
									'target': 15
								},
								{
									'source': 51,
									'target': 15
								},
								{
									'source': 52,
									'target': 15
								},
								{
									'source': 54,
									'target': 15
								},
								{
									'source': 59,
									'target': 15
								},
								{
									'source': 63,
									'target': 15
								},
								{
									'source': 64,
									'target': 15
								},
								{
									'source': 66,
									'target': 15
								},
								{
									'source': 9,
									'target': 15
								},
								{
									'source': 20,
									'target': 16
								},
								{
									'source': 31,
									'target': 16
								},
								{
									'source': 33,
									'target': 16
								},
								{
									'source': 60,
									'target': 16
								},
								{
									'source': 29,
									'target': 17
								},
								{
									'source': 31,
									'target': 17
								},
								{
									'source': 5,
									'target': 17
								},
								{
									'source': 55,
									'target': 17
								},
								{
									'source': 17,
									'target': 18
								},
								{
									'source': 27,
									'target': 18
								},
								{
									'source': 28,
									'target': 18
								},
								{
									'source': 29,
									'target': 18
								},
								{
									'source': 30,
									'target': 18
								},
								{
									'source': 31,
									'target': 18
								},
								{
									'source': 33,
									'target': 18
								},
								{
									'source': 38,
									'target': 18
								},
								{
									'source': 39,
									'target': 18
								},
								{
									'source': 42,
									'target': 18
								},
								{
									'source': 49,
									'target': 18
								},
								{
									'source': 55,
									'target': 18
								},
								{
									'source': 9,
									'target': 18
								},
								{
									'source': 24,
									'target': 19
								},
								{
									'source': 25,
									'target': 19
								},
								{
									'source': 29,
									'target': 19
								},
								{
									'source': 4,
									'target': 19
								},
								{
									'source': 9,
									'target': 19
								},
								{
									'source': 31,
									'target': 20
								},
								{
									'source': 64,
									'target': 20
								},
								{
									'source': 8,
									'target': 20
								},
								{
									'source': 26,
									'target': 21
								},
								{
									'source': 33,
									'target': 21
								},
								{
									'source': 42,
									'target': 21
								},
								{
									'source': 54,
									'target': 21
								},
								{
									'source': 20,
									'target': 22
								},
								{
									'source': 24,
									'target': 22
								},
								{
									'source': 29,
									'target': 22
								},
								{
									'source': 31,
									'target': 22
								},
								{
									'source': 36,
									'target': 22
								},
								{
									'source': 39,
									'target': 22
								},
								{
									'source': 46,
									'target': 22
								},
								{
									'source': 5,
									'target': 22
								},
								{
									'source': 56,
									'target': 22
								},
								{
									'source': 61,
									'target': 22
								},
								{
									'source': 67,
									'target': 22
								},
								{
									'source': 8,
									'target': 22
								},
								{
									'source': 12,
									'target': 24
								},
								{
									'source': 38,
									'target': 24
								},
								{
									'source': 5,
									'target': 24
								},
								{
									'source': 25,
									'target': 26
								},
								{
									'source': 33,
									'target': 26
								},
								{
									'source': 29,
									'target': 27
								},
								{
									'source': 24,
									'target': 28
								},
								{
									'source': 17,
									'target': 3
								},
								{
									'source': 19,
									'target': 3
								},
								{
									'source': 29,
									'target': 3
								},
								{
									'source': 30,
									'target': 3
								},
								{
									'source': 32,
									'target': 3
								},
								{
									'source': 33,
									'target': 3
								},
								{
									'source': 55,
									'target': 3
								},
								{
									'source': 66,
									'target': 3
								},
								{
									'source': 29,
									'target': 30
								},
								{
									'source': 5,
									'target': 30
								},
								{
									'source': 29,
									'target': 31
								},
								{
									'source': 39,
									'target': 31
								},
								{
									'source': 42,
									'target': 31
								},
								{
									'source': 5,
									'target': 31
								},
								{
									'source': 29,
									'target': 32
								},
								{
									'source': 30,
									'target': 32
								},
								{
									'source': 66,
									'target': 32
								},
								{
									'source': 27,
									'target': 33
								},
								{
									'source': 29,
									'target': 33
								},
								{
									'source': 39,
									'target': 33
								},
								{
									'source': 66,
									'target': 33
								},
								{
									'source': 9,
									'target': 33
								},
								{
									'source': 30,
									'target': 34
								},
								{
									'source': 33,
									'target': 34
								},
								{
									'source': 38,
									'target': 34
								},
								{
									'source': 42,
									'target': 34
								},
								{
									'source': 5,
									'target': 34
								},
								{
									'source': 61,
									'target': 34
								},
								{
									'source': 26,
									'target': 35
								},
								{
									'source': 33,
									'target': 35
								},
								{
									'source': 36,
									'target': 35
								},
								{
									'source': 50,
									'target': 35
								},
								{
									'source': 67,
									'target': 35
								},
								{
									'source': 25,
									'target': 36
								},
								{
									'source': 27,
									'target': 36
								},
								{
									'source': 28,
									'target': 36
								},
								{
									'source': 29,
									'target': 36
								},
								{
									'source': 30,
									'target': 36
								},
								{
									'source': 31,
									'target': 36
								},
								{
									'source': 32,
									'target': 36
								},
								{
									'source': 39,
									'target': 36
								},
								{
									'source': 40,
									'target': 36
								},
								{
									'source': 42,
									'target': 36
								},
								{
									'source': 48,
									'target': 36
								},
								{
									'source': 54,
									'target': 36
								},
								{
									'source': 58,
									'target': 36
								},
								{
									'source': 66,
									'target': 36
								},
								{
									'source': 8,
									'target': 36
								},
								{
									'source': 9,
									'target': 36
								},
								{
									'source': 33,
									'target': 37
								},
								{
									'source': 64,
									'target': 37
								},
								{
									'source': 67,
									'target': 37
								},
								{
									'source': 13,
									'target': 38
								},
								{
									'source': 17,
									'target': 38
								},
								{
									'source': 20,
									'target': 38
								},
								{
									'source': 29,
									'target': 38
								},
								{
									'source': 40,
									'target': 38
								},
								{
									'source': 42,
									'target': 38
								},
								{
									'source': 47,
									'target': 38
								},
								{
									'source': 49,
									'target': 38
								},
								{
									'source': 5,
									'target': 38
								},
								{
									'source': 55,
									'target': 38
								},
								{
									'source': 8,
									'target': 38
								},
								{
									'source': 9,
									'target': 38
								},
								{
									'source': 9,
									'target': 39
								},
								{
									'source': 29,
									'target': 40
								},
								{
									'source': 30,
									'target': 40
								},
								{
									'source': 31,
									'target': 40
								},
								{
									'source': 8,
									'target': 40
								},
								{
									'source': 56,
									'target': 41
								},
								{
									'source': 24,
									'target': 42
								},
								{
									'source': 28,
									'target': 42
								},
								{
									'source': 29,
									'target': 42
								},
								{
									'source': 19,
									'target': 44
								},
								{
									'source': 25,
									'target': 44
								},
								{
									'source': 29,
									'target': 44
								},
								{
									'source': 31,
									'target': 44
								},
								{
									'source': 39,
									'target': 44
								},
								{
									'source': 42,
									'target': 44
								},
								{
									'source': 48,
									'target': 44
								},
								{
									'source': 12,
									'target': 45
								},
								{
									'source': 19,
									'target': 45
								},
								{
									'source': 40,
									'target': 45
								},
								{
									'source': 5,
									'target': 45
								},
								{
									'source': 66,
									'target': 45
								},
								{
									'source': 10,
									'target': 46
								},
								{
									'source': 9,
									'target': 46
								},
								{
									'source': 20,
									'target': 47
								},
								{
									'source': 29,
									'target': 47
								},
								{
									'source': 33,
									'target': 47
								},
								{
									'source': 42,
									'target': 47
								},
								{
									'source': 20,
									'target': 48
								},
								{
									'source': 24,
									'target': 48
								},
								{
									'source': 29,
									'target': 48
								},
								{
									'source': 39,
									'target': 48
								},
								{
									'source': 55,
									'target': 48
								},
								{
									'source': 61,
									'target': 48
								},
								{
									'source': 29,
									'target': 49
								},
								{
									'source': 33,
									'target': 49
								},
								{
									'source': 36,
									'target': 49
								},
								{
									'source': 5,
									'target': 49
								},
								{
									'source': 8,
									'target': 49
								},
								{
									'source': 12,
									'target': 5
								},
								{
									'source': 29,
									'target': 5
								},
								{
									'source': 9,
									'target': 5
								},
								{
									'source': 10,
									'target': 50
								},
								{
									'source': 12,
									'target': 50
								},
								{
									'source': 16,
									'target': 50
								},
								{
									'source': 17,
									'target': 50
								},
								{
									'source': 18,
									'target': 50
								},
								{
									'source': 19,
									'target': 50
								},
								{
									'source': 24,
									'target': 50
								},
								{
									'source': 25,
									'target': 50
								},
								{
									'source': 26,
									'target': 50
								},
								{
									'source': 27,
									'target': 50
								},
								{
									'source': 29,
									'target': 50
								},
								{
									'source': 3,
									'target': 50
								},
								{
									'source': 30,
									'target': 50
								},
								{
									'source': 31,
									'target': 50
								},
								{
									'source': 32,
									'target': 50
								},
								{
									'source': 33,
									'target': 50
								},
								{
									'source': 38,
									'target': 50
								},
								{
									'source': 39,
									'target': 50
								},
								{
									'source': 4,
									'target': 50
								},
								{
									'source': 40,
									'target': 50
								},
								{
									'source': 46,
									'target': 50
								},
								{
									'source': 47,
									'target': 50
								},
								{
									'source': 48,
									'target': 50
								},
								{
									'source': 49,
									'target': 50
								},
								{
									'source': 5,
									'target': 50
								},
								{
									'source': 54,
									'target': 50
								},
								{
									'source': 55,
									'target': 50
								},
								{
									'source': 56,
									'target': 50
								},
								{
									'source': 59,
									'target': 50
								},
								{
									'source': 6,
									'target': 50
								},
								{
									'source': 60,
									'target': 50
								},
								{
									'source': 61,
									'target': 50
								},
								{
									'source': 66,
									'target': 50
								},
								{
									'source': 67,
									'target': 50
								},
								{
									'source': 8,
									'target': 50
								},
								{
									'source': 9,
									'target': 50
								},
								{
									'source': 21,
									'target': 51
								},
								{
									'source': 24,
									'target': 51
								},
								{
									'source': 25,
									'target': 51
								},
								{
									'source': 26,
									'target': 51
								},
								{
									'source': 27,
									'target': 51
								},
								{
									'source': 28,
									'target': 51
								},
								{
									'source': 29,
									'target': 51
								},
								{
									'source': 3,
									'target': 51
								},
								{
									'source': 31,
									'target': 51
								},
								{
									'source': 32,
									'target': 51
								},
								{
									'source': 33,
									'target': 51
								},
								{
									'source': 42,
									'target': 51
								},
								{
									'source': 61,
									'target': 51
								},
								{
									'source': 65,
									'target': 51
								},
								{
									'source': 66,
									'target': 51
								},
								{
									'source': 8,
									'target': 51
								},
								{
									'source': 17,
									'target': 52
								},
								{
									'source': 29,
									'target': 52
								},
								{
									'source': 3,
									'target': 52
								},
								{
									'source': 30,
									'target': 52
								},
								{
									'source': 31,
									'target': 52
								},
								{
									'source': 33,
									'target': 52
								},
								{
									'source': 42,
									'target': 52
								},
								{
									'source': 48,
									'target': 52
								},
								{
									'source': 60,
									'target': 52
								},
								{
									'source': 65,
									'target': 52
								},
								{
									'source': 33,
									'target': 53
								},
								{
									'source': 25,
									'target': 54
								},
								{
									'source': 27,
									'target': 54
								},
								{
									'source': 26,
									'target': 56
								},
								{
									'source': 28,
									'target': 56
								},
								{
									'source': 29,
									'target': 56
								},
								{
									'source': 31,
									'target': 56
								},
								{
									'source': 44,
									'target': 56
								},
								{
									'source': 5,
									'target': 56
								},
								{
									'source': 8,
									'target': 56
								},
								{
									'source': 25,
									'target': 58
								},
								{
									'source': 26,
									'target': 58
								},
								{
									'source': 27,
									'target': 58
								},
								{
									'source': 29,
									'target': 58
								},
								{
									'source': 33,
									'target': 58
								},
								{
									'source': 42,
									'target': 58
								},
								{
									'source': 66,
									'target': 58
								},
								{
									'source': 29,
									'target': 59
								},
								{
									'source': 31,
									'target': 59
								},
								{
									'source': 33,
									'target': 59
								},
								{
									'source': 46,
									'target': 59
								},
								{
									'source': 52,
									'target': 59
								},
								{
									'source': 61,
									'target': 59
								},
								{
									'source': 67,
									'target': 59
								},
								{
									'source': 8,
									'target': 59
								},
								{
									'source': 24,
									'target': 6
								},
								{
									'source': 25,
									'target': 6
								},
								{
									'source': 27,
									'target': 6
								},
								{
									'source': 29,
									'target': 6
								},
								{
									'source': 3,
									'target': 6
								},
								{
									'source': 33,
									'target': 6
								},
								{
									'source': 42,
									'target': 6
								},
								{
									'source': 47,
									'target': 6
								},
								{
									'source': 48,
									'target': 6
								},
								{
									'source': 5,
									'target': 6
								},
								{
									'source': 60,
									'target': 6
								},
								{
									'source': 65,
									'target': 6
								},
								{
									'source': 66,
									'target': 6
								},
								{
									'source': 27,
									'target': 60
								},
								{
									'source': 30,
									'target': 60
								},
								{
									'source': 36,
									'target': 60
								},
								{
									'source': 5,
									'target': 60
								},
								{
									'source': 55,
									'target': 60
								},
								{
									'source': 66,
									'target': 60
								},
								{
									'source': 19,
									'target': 61
								},
								{
									'source': 25,
									'target': 61
								},
								{
									'source': 28,
									'target': 61
								},
								{
									'source': 29,
									'target': 61
								},
								{
									'source': 31,
									'target': 61
								},
								{
									'source': 33,
									'target': 61
								},
								{
									'source': 39,
									'target': 61
								},
								{
									'source': 42,
									'target': 61
								},
								{
									'source': 5,
									'target': 61
								},
								{
									'source': 56,
									'target': 61
								},
								{
									'source': 66,
									'target': 61
								},
								{
									'source': 8,
									'target': 61
								},
								{
									'source': 9,
									'target': 61
								},
								{
									'source': 56,
									'target': 62
								},
								{
									'source': 33,
									'target': 63
								},
								{
									'source': 48,
									'target': 63
								},
								{
									'source': 5,
									'target': 63
								},
								{
									'source': 60,
									'target': 63
								},
								{
									'source': 66,
									'target': 63
								},
								{
									'source': 21,
									'target': 64
								},
								{
									'source': 29,
									'target': 64
								},
								{
									'source': 33,
									'target': 64
								},
								{
									'source': 36,
									'target': 64
								},
								{
									'source': 20,
									'target': 65
								},
								{
									'source': 29,
									'target': 65
								},
								{
									'source': 3,
									'target': 65
								},
								{
									'source': 33,
									'target': 65
								},
								{
									'source': 42,
									'target': 65
								},
								{
									'source': 5,
									'target': 65
								},
								{
									'source': 29,
									'target': 66
								},
								{
									'source': 48,
									'target': 66
								},
								{
									'source': 29,
									'target': 67
								},
								{
									'source': 33,
									'target': 67
								},
								{
									'source': 48,
									'target': 67
								},
								{
									'source': 63,
									'target': 67
								},
								{
									'source': 65,
									'target': 67
								},
								{
									'source': 8,
									'target': 67
								},
								{
									'source': 29,
									'target': 8
								},
								{
									'source': 31,
									'target': 8
								},
								{
									'source': 39,
									'target': 8
								},
							]

						}
						},
						{
							'name': 'Twitter',
							'value': '2',
							'type': 1,
							"effectList": [{
								"selfMediaPopularity": ["19", '15'],
								"selfMediaParticipation": ["3", '13'],
								"emotional": ['30', '50'],
								"liveness": ['29', '49'],
								"clicks": ["12", '18'],
								"trafficVolume": ["23", '43'],
								"forwardingVolume": ["28", '8'],
								"dateTime": "2019-07-26"
							}, {

								"selfMediaPopularity": ["19", '25'],
								"selfMediaParticipation": ["13", '23'],
								"emotional": ['40', '60'],
								"liveness": ['39', '59'],
								"clicks": ["22", '28'],
								"trafficVolume": ["33", '53'],
								"forwardingVolume": ["38", '18'],
								"dateTime": "2019-07-27"
							}, {

								"selfMediaPopularity": ["24", '30'],
								"selfMediaParticipation": ["18", '28'],
								"emotional": ['45', '65'],
								"liveness": ['44', '63'],
								"clicks": ["27", '33'],
								"trafficVolume": ["38", '58'],
								"forwardingVolume": ["43", '23'],
								"dateTime": "2019-07-28"
							}, {

								"selfMediaPopularity": ["12", '18'],
								"selfMediaParticipation": ["6", '16'],
								"emotional": ['23', '53'],
								"liveness": ['32', '51'],
								"clicks": ["15", '18'],
								"trafficVolume": ["26", '46'],
								"forwardingVolume": ["31", '11'],
								"dateTime": "2019-08-7"
							}],
							'relationDetail': {
								"node": [{
									"name": "1号大佬",
									"symbolSize": 44,
									"category": 0,
								}, {
									"name": "DriverHiro",
									"symbolSize": 50,
									'category': 0,
								}, {
									"name": "time",
									"symbolSize": 70,
									'category': 0,
								}, {
									"name": "2号大佬",
									"symbolSize": 71,
									'category': 0,
								}, {
									"name": "3号大佬",
									"symbolSize": 75,
									"category": 0,
								}, {
									"name": "4号大佬",
									"symbolSize": 75,
									"category": 0,
								},
									{
										"name": "5号大佬",
										"symbolSize": 75,
										"category": 0,
									}, {
										"name": "6号大佬",
										"symbolSize": 75,
										"category": 0,
									}, {
										"name": "7号大佬",
										"symbolSize": 75,
										"category": 0,
									}
								],
								'categories': [

									{
										"name": "事件1"
									},
								],
								'relation': [
											# edges是其别名代表节点间的关系数据。
	{
		"source": 1,
		"target": 0,
	},
	{
		"source": 2,
		"target": 0,
	},
	{
		"source": 3,
		"target": 0,
	},
	{
		"source": 4,
		"target": 0,
	},
	{
		"source": 5,
		"target": 0,

	},
	{
		"source": 6,
		"target": 1,

	},
	{
		"source": 7,
		"target": 1,

	},
	{
		"source": 8,
		"target": 1,

	},
	{
		"source": 9,
		"target": 1,

	},

	]
	}
	},
						{
		'name': 'Youtube',
		'value': '3',
		'type': 2,
		"effectList": [{

			"selfMediaPopularity": ["89", '15'],
			"selfMediaParticipation": ["3", '13'],
			"emotional": ['30', '50'],
			"liveness": ['29', '49'],
			"clicks": ["12", '18'],
			"trafficVolume": ["23", '43'],
			"forwardingVolume": ["28", '8'],
			"dateTime": "2019-07-26"
		}, {

			"selfMediaPopularity": ["19", '25'],
			"selfMediaParticipation": ["13", '23'],
			"emotional": ['40', '60'],
			"liveness": ['39', '59'],
			"clicks": ["22", '28'],
			"trafficVolume": ["33", '53'],
			"forwardingVolume": ["38", '18'],
			"dateTime": "2019-07-27"
		}, {

			"selfMediaPopularity": ["24", '30'],
			"selfMediaParticipation": ["18", '28'],
			"emotional": ['45', '65'],
			"liveness": ['44', '63'],
			"clicks": ["27", '33'],
			"trafficVolume": ["38", '58'],
			"forwardingVolume": ["43", '23'],
			"dateTime": "2019-07-28"
		}, {

			"selfMediaPopularity": ["12", '18'],
			"selfMediaParticipation": ["6", '16'],
			"emotional": ['23', '53'],
			"liveness": ['32', '51'],
			"clicks": ["15", '18'],
			"trafficVolume": ["26", '46'],
			"forwardingVolume": ["31", '11'],
			"dateTime": "2019-08-7"
		}],
		'relationDetail': {
			"node": [{
				"name": "1号大佬",
				"symbolSize": 44,
				"category": 0,
			}, {
				"name": "DriverHiro",
				"symbolSize": 50,
				'category': 0,
			}, {
				"name": "time",
				"symbolSize": 70,
				'category': 0,
			}, {
				"name": "2号大佬",
				"symbolSize": 71,
				'category': 0,
			}, {
				"name": "3号大佬",
				"symbolSize": 75,
				"category": 0,
			}, {
				"name": "4号大佬",
				"symbolSize": 75,
				"category": 0,
			},
				{
					"name": "5号大佬",
					"symbolSize": 75,
					"category": 0,
				}, {
					"name": "6号大佬",
					"symbolSize": 75,
					"category": 0,
				}, {
					"name": "7号大佬",
					"symbolSize": 75,
					"category": 0,
				}
			],
			'categories': [

				{
					"name": "事件1"
				},
			],
			'relation': [
						# edges是其别名代表节点间的关系数据。
	{
		"source": 1,
		"target": 0,
	},
	{
		"source": 2,
		"target": 0,
	},
	{
		"source": 3,
		"target": 0,
	},
	{
		"source": 4,
		"target": 0,
	},
	{
		"source": 5,
		"target": 0,

	},
	{
		"source": 6,
		"target": 2,

	},
	{
		"source": 7,
		"target": 2,

	},
	{
		"source": 8,
		"target": 1,

	},
	{
		"source": 9,
		"target": 1,

	},

	]
	}
	},
						{
		'name': 'Instagram',
		'value': '4',
		'type': 2,
		"effectList": [{

			"selfMediaPopularity": ["59", '15'],
			"selfMediaParticipation": ["53", '13'],
			"emotional": ['30', '50'],
			"liveness": ['29', '49'],
			"clicks": ["12", '18'],
			"trafficVolume": ["23", '43'],
			"forwardingVolume": ["28", '8'],
			"dateTime": "2019-07-26"
		}, {

			"selfMediaPopularity": ["19", '25'],
			"selfMediaParticipation": ["13", '23'],
			"emotional": ['40', '60'],
			"liveness": ['39', '59'],
			"clicks": ["22", '28'],
			"trafficVolume": ["33", '53'],
			"forwardingVolume": ["38", '18'],
			"dateTime": "2019-07-27"
		}, {

			"selfMediaPopularity": ["24", '30'],
			"selfMediaParticipation": ["18", '28'],
			"emotional": ['45', '65'],
			"liveness": ['44', '63'],
			"clicks": ["27", '33'],
			"trafficVolume": ["38", '58'],
			"forwardingVolume": ["43", '23'],
			"dateTime": "2019-07-28"
		}, {

			"selfMediaPopularity": ["12", '18'],
			"selfMediaParticipation": ["6", '16'],
			"emotional": ['23', '53'],
			"liveness": ['32', '51'],
			"clicks": ["15", '18'],
			"trafficVolume": ["26", '46'],
			"forwardingVolume": ["31", '11'],
			"dateTime": "2019-08-7"
		}],
		'relationDetail': {
			"node": [{
				"name": "1号大佬",
				"symbolSize": 44,
				"category": 0,

			}, {
				"name": "DriverHiro",
				"symbolSize": 50,
				"category": 0,
			}, {
				"name": "time",
				"symbolSize": 70,
				"category": 0,
			}, {
				"name": "2号大佬",
				"symbolSize": 71,
				"category": 0,
			}, {
				"name": "3号大佬",
				"symbolSize": 75,
				"category": 0,
			}, {
				"name": "4号大佬",
				"symbolSize": 75,
				"category": 0,
			},
				{
					"name": "5号大佬",
					"symbolSize": 75,
					"category": 0,
				},
				{
					"name": "6号大佬",
					"symbolSize": 75,
					"category": 0,
				},
				{
					"name": "7号大佬",
					"symbolSize": 75,
					"category": 0,
				},
				{
					"name": "8号大佬",
					"symbolSize": 75,
					"category": 0,
				},
				{
					"name": "9号大佬",
					"symbolSize": 75,
					"category": 0,
				},
				{
					"name": "10号大佬",
					"symbolSize": 75,
					"category": 0,
				}
			],
			'categories': [
						  # symbol name：用于和 legend 对应以及格式化 tooltip 的内容。 label有效
	{
		"name": "事件1"
	},
	],
	'relation': [
				# edges是其别名代表节点间的关系数据。
	{
		"source": 1,
		"target": 0,
	},
	{
		"source": 6,
		"target": 0,
	},
	{
		"source": 5,
		"target": 0,
	},
	{
		"source": 2,
		"target": 1,
	},
	{
		"source": 3,
		"target": 1,

	},
	{
		"source": 4,
		"target": 1,

	},

	{
		"source": 7,
		"target": 5,

	},
	{
		"source": 8,
		"target": 6,

	},
	{
		"source": 9,
		"target": 6,

	},
	{
		"source": 10,
		"target": 6,

	},
	{
		"source": 11,
		"target": 6,

	},
	]
	}
	}
					],

	},
# es.index(index="database", body=data

#
# res = es.get(index='my-index', doc_type='test-type', id=1)
# print(res)
result = es.indices.delete(index='database', ignore=[400, 404])
print(result)
res = es.search(index="database", doc_type="testData")
print(res)

# body = {
#     'query':{
#         "match_all":{}
#     }
# }
# res = es.search(index='my-index', doc_type='test-type', body=body)


# res = es.get(index="my-index", doc_type="test-type", id=01)
es.get(index='indexName', doc_type='typeName', id='idValue')