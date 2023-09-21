import pymongo

def main():
    connection_string = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(connection_string)
    aviv_db = client["Aviv's_people"]
    family_collection = aviv_db["family_collection"]
    friends_collection = aviv_db["friends_collection"]
    army_collection = aviv_db["army_collection"]

    aviv_db['army_collection'].drop()
    aviv_db['friends_collection'].drop()
    aviv_db['family_collection'].drop()

    army_list = [{"name:":"Aviv","age:":20,"work:":"backend"},
                 {"name:":"Lihi","age:":21,"work:":"qa"},
                 {"name:":"Gabi","age:":22,"work:":"DevOps"},
                 {"name:":"Ori","age:":23,"work:":"front-end"},
                 {"name:":"Ido","age:":22,"work:":"developer"},
                 {"name:":"Yarden","age:":24,"work:":"DevOps"}]
    
    army_collection.insert_many(army_list)

    family_list = [{'name':'mother','age':45, 'role':'teacher'},
                        {'name':'father','age':46, 'role':'engineer'},
                        {'name':'brother','age':12, 'role':'school'},
                        {'name':'sister','age':24, 'role':'student'}]
    
    for family_member in family_list:
        family_collection.insert_one(family_member)

    friends_list = [{"_id": 1,'name':'Amit','age':20, 'role':'Waiter'},
                    {"_id": 2,'name':'Yonatan','age':24, 'role':'doctor'},
                    {"_id": 3,'name':'Noa','age':22, 'role':'student'},
                    {"_id": 4,'name':'Michal','age':21, 'role':'baker'}]
    
    for friend in friends_list:
        friends_collection.insert_one(friend)


    army_collection.delete_one({"name:":"Lihi"})

    dev_ops_friend = army_collection.find_one({'work:': 'DevOps','age:': {'$lt':23}})
    print()


    new_role = army_collection.find_one({"age:": dev_ops_friend["age:"], "_id": {"$ne": dev_ops_friend["_id"]}})
    army_collection.update_one({"_id" : dev_ops_friend["_id"]}, {"$set" : {"work:" : new_role["work:"]}})

    

    sorted_army_friends = army_collection.aggregate([{"$sort" : {"age:" : -1}},{"$out":"army_collection"}])


    delete_from_army = {"age:" : {"$gt" : 23}}
    moving_soldiers = army_collection.find(delete_from_army)
    new_friend = friends_collection.insert_many(moving_soldiers)
    army_collection.delete_many(delete_from_army)

    for collections in aviv_db.list_collection_names():
        for document in aviv_db[collections].find():
            print(document)



    
    

    


if __name__ == "__main__":
    main()