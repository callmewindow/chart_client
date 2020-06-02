#coding:utf-8
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Albert"]#选择库
mytable = mydb["Albert"]#选择表

myst = mydb["statistics"]
mytotal = mydb["totalRow"]



#所有数据库
dblist = myclient.list_database_names()
print(dblist)


list = [
        {
            "id": "1",
            "collect_time": "[]",
            "publish_time": "杭州一中学五成新生不会穿鞋带叠衣服",
            "source": "大纪元大陆",
            "author": "",
            "content": "【大纪元2019年09月02日讯】又到了开学季，近日，在浙江杭州一所中学的新生训练现场，多名初一新生不会叠衣服、穿鞋带。老师表示，能同时完成这两项的学生只有一半。有学生说，这些事情在家都是妈妈做；也有家长称，孩子还小，要以学习为主。 据大陆媒体报导，8月29日，杭州一所中学的新生训练现场，校方组织了一场穿鞋带、叠衣服的比赛。 “十个里面吧，大概总有一两个人是不会做的。”该校一名老师说，“叠衣服相对来说好一点，系鞋带、穿鞋带对很多孩子来说可能从来没有弄过”。 老师说，这些新生里，只有一半学生能同时完成这两项工作。 一名初一新生表示，她从商店买来的鞋子，鞋带都已穿好，自己系上鞋带就行。“穿鞋带这是第二次，之前还有第一次，就昨天。” 另一名初一新生说，他只会叠袜子，“其他的基本上都是我妈妈帮我叠的”。他说，在训练现场叠衣服时，他回想着妈妈是怎么叠的，但自己叠完后却是一团糟。 一名学生家长说，他如果叫孩子做家务，孩子会去做，“一般不需要他做，奶奶做，他还小嘛，刚刚上初中一年级，对小孩没什么大要求，反正以学习为主”。 另一位家长也表示：“有时候是大人做，有时候会外面请阿姨来做，洗了衣服基本上是我在叠，他（孩子）自己的衣服估计他也不太会去叠。” 此事在网络上引起了民众关注和热议。民众表示：“中学还小？学到最后连生活基本技能都不会了。” “这不是幼儿园就该会的吗？ “现在的教育怎么呢？我记得穿鞋带都是幼儿园必修哎。” “可悲！家长的观念都是扭曲的。”",
            "abstract_txt": "",
            "url": "[]",
            "title": "28",
            "publish_address": "[]",
            "related_address": "",
            "related_url": "",
            "related_person": "",
            "images": "",
            "attaches": "",
            "comment": "",
            "importance_auto": "",
            "importance_assist": "",
            "tags": [],
            "source_type": "",
            "task_id": "",
            "comment_number": "",
            "repost": "",
            "likes": "",
            "isRepost": "",
            "isReply": "愤怒",
            "user_id": "",
            "sj_id": 0,
            "keywords": [
                "鞋带",
                "衣服",
                "新生",
                "孩子",
                "初一",
                "新生训练",
                "家长",
                "中学",
                "妈妈",
                "老师",
                "这两项",
                "现场",
                "一名",
                "学生",
                "幼儿园",
                "表示",
                "一所",
                "有时候",
                "民众",
                "不会"
            ],
            "sj_name": "",
            "yxl_zb": 0,
            "djl": 0,
            "fwl": 0,
            "zfl": 0,
            "zmtrd": 0,
            "zmtcyd": 0,
            "xxs": 0
        },
        {
            "id": "2",
            "collect_time": "[]",
            "publish_time": "美国和波兰签署5G网络安全声明 剑指华为",
            "source": "大纪元大陆",
            "author": "",
            "content": "【大纪元2019年09月02日讯】（大纪元记者徐简综合报导）周一（9月2日）正在波兰出席二战80周年纪念活动的美国副总统彭斯（Mike Pence），与波兰总理莫拉维茨（Mateusz Morawiecki）签署了一项关于5G网络安全的联合声明。 根据这份联合声明，两国再次认可了在布拉格安全会议中关于为了应对威胁，以及确保下一代网路安全而确立的发展准则，为了“保护下一代通讯网路避遭破坏或操纵，以及确保美国、波兰及其它国家人民的隐私及自由，是至关重要之事。” 美国和波兰一致同意，政府应该对5G网络设备的供应商进行严格评估，检查该供应商是否受外国政府控制。 “所有国家都必须确保，只有值得信赖和可靠的供应商才能参与（5G）网络建设。”声明中还说，政府还应该审查供应商，看他们的所有权结构是否透明。 该协议并没有提及任何特定国家或公司的名称，但外界认为这是在剑指中国的电信巨头华为公司。 美国认为华为有中共背景，透过网路设备监控用户，并窃取美国的数据资料和知识产权，因此美国一直游说欧洲盟国抵制华为参加各国5G 建设。彭斯说，两国就数码网络安全达成协议，将为欧洲其它国家树立一个至关重要的榜样。 波兰官员曾在1 月份表示，波兰政府逮捕了一名中国华为员工和一名被指控间谍的前波兰资安官员后，曾考虑过要将华为从5G网路供应商名单中删除。 美国副总统彭斯离开波兰后，还将访问爱尔兰、冰岛和英国。#",
            "abstract_txt": "",
            "url": "[]",
            "title": "15",
            "publish_address": "[]",
            "related_address": "",
            "related_url": "",
            "related_person": "",
            "images": "",
            "attaches": "",
            "comment": "",
            "importance_auto": "",
            "importance_assist": "",
            "tags": [],
            "source_type": "",
            "task_id": "",
            "comment_number": "",
            "repost": "",
            "likes": "",
            "isRepost": "",
            "isReply": "愤怒",
            "user_id": "",
            "sj_id": 0,
            "keywords": [
                "5G",
                "波兰",
                "华为",
                "供应商",
                "网路",
                "美国",
                "彭斯",
                "网络安全",
                "纪元",
                "确保",
                "联合声明",
                "下一代",
                "至关重要",
                "国家",
                "政府",
                "一名",
                "总统",
                "通讯网",
                "2019",
                "09"
            ],
            "sj_name": "",
            "yxl_zb": 0,
            "djl": 0,
            "fwl": 0,
            "zfl": 0,
            "zmtrd": 0,
            "zmtcyd": 0,
            "xxs": 0
        },
        {"id":"3","source":"猪圈"}
]


# #插入原始数据，否则数据库不存在
# #插入列表数据
# mytable.insert_many(list)

#先查一下有没有id相同的数据
for i in list:
    if "id" in i:
        myquery = {"id":i["id"]}
        if (mytable.find_one(myquery)):
            print("已存在")
        else:
            mytable.insert_one(i)
    else:
        mytable.insert_one(i)

#显示表中所有数据
for x in mytable.find():
    print(x)

sourceList = []
for x in mytable.find():
    #得到所有的source

        if "source" in x and x["source"] not in sourceList:
            sourceList.append(x['source'])
print(sourceList)

st=[]#存储最终结果
for source in sourceList:
    myquery = {"source":source}
    num = 0
    for i in mytable.find(myquery):
        num = num + 1

    dict = {
        "type":"1",
        "source":source,
        "total":str(num)
    }

    st.append(dict)

myst.delete_many({})#hhh 辛亏清空数据库
mytotal.delete_many({})

#存入数据库
x = myst.insert_many(st)

#得到totalRow
dict = {}
dict["totalRow"] = 0
for x in myst.find():
    dict["totalRow"] = int(x["total"]) + dict["totalRow"]
#存储
mytotal.insert_one(dict)

for x in myst.find():
    print(x)

for x in mytotal.find():
    print(x)




