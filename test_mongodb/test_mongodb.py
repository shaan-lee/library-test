from pymongo import MongoClient
import pandas as pd

my_client = MongoClient("localhost:27017")
# print(my_client.list_database_names())

# mydb =my_client['test']
# mycol = mydb['testInsert']
# insert = mycol.insert_one({"name":"caa","test":"yes"})
# print(insert.inserted_id)
# print(my_client.list_database_names())

# find_one = mycol.find_one()
# print(find_one)

# find_all = mycol.find().sort("name")
# for x in find_all:
#    print(x)

# find_query = mycol.find({"name":{"$regex":"^a"}})
# for x in find_query:
#    print(x)

mydb = my_client[""]
mycol = mydb["data_by_language"]

# mycol.delete_many({})

# data = pd.read_csv("./kcopa_bigdata_by_language.csv",header=0)
# data_clean = data.dropna(subset=['site_name'],how='any',axis=0)
##data_frame = pd.DataFrame(data_clean).iloc[:,1:9]
# data_dict = data_frame.to_dict('index')s
# print("to-do : " ,len(list(data_dict)))

# for i in range(len(list(data_dict))):
#    data = data_dict[i]
#    if '운영' in data['is_active']:
#        data['is_active'] = True
#    else:
#        data['is_active'] = False
#    mycol.insert_one(data)

# one = mycol.find_one({"site_name":"pelisplus"})
# mycol.update_one({"site_name":one['site_name']},{"$set":{"update":one["update"]+"update2"}})

# tmp = {"test1":[1]}
# mycol.find_one_and_update({"site_name":"pelisplus"},{"$set":{"findOneAndUpdate":[tmp]}})
mydoc = mycol.find()
for i in mydoc:
    if "findOneAndUpdate" in i.keys():
        print(i)
        tmp = i["findOneAndUpdate"]
        print(tmp)
        tmp.append({"test2": [1, 2]})
        print(tmp)
        mycol.update_one({"_id": i["_id"]}, {"$set": {"findOneAndUpdate": tmp}})
