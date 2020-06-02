import pymongo

def readMongoDB():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Albert"]#选择库
    mytable = mydb["Albert"]#选择表

    myst = mydb["statistics"]
    mytotal = mydb["totalRow"]

    visitCount = {
        "message": "请求成功",
        "code": 200,
    }
    visitCount['data'] = {}
    visitCount["data"]["resultList"] = []

    for x in mytotal.find({}, {"_id": 0, 'totalRow': 1}):
        visitCount["data"]["totalRow"] = x['totalRow']

    for x in myst.find({},{"_id":0,'type': 1, 'source': 1, 'total': 1}):
        visitCount["data"]["resultList"].append(x)

    return(visitCount)

if __name__ == '__main__':
    readMongoDB()