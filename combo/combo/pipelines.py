# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


import pymongo

class ComboPipeline:
 
    def __init__(self):
    
        self.conn = pymongo.MongoClient(
        #  "mongodb+srv://maiworld:Iqbal123ars@cluster0.syyxe.mongodb.net/apkProject?retryWrites=true&w=majority"
        )

        db = self.conn["apkProject"]
        self.collection1= db["apk"]
        

    def process_item(self, item, spider):
        
        # name = self.collection1.find_one({"title":dict(item)["title"]})
        
       
       
        # if (name):
            
            
        #         print("already")
        # else:
        #     self.collection1.insert_one(dict(item))
     

      
        return item
