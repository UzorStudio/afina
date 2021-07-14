import pymongo
from bson import ObjectId


class UserNOffers():
    def __init__(self,classterMongo):
        self.classterMongo = classterMongo
        self.classter = pymongo.MongoClient(self.classterMongo)

    def regUser(self,usrId):
        db = self.classter["Fembot"]
        User = db["User"]
        post = {"usrId":usrId,"like":0,"dislike":0,"change":"","moder":"","postModer":""}
        User.insert_one(post)

    def setChange(self,usrId,change):
        db = self.classter["Fembot"]
        User = db["User"]
        User.update_one({"usrId":usrId},{"$set":{"change":change}})

    def setModer(self,usrId,moder):
        db = self.classter["Fembot"]
        User = db["User"]
        User.update_one({"usrId": usrId}, {"$set": {"moder": moder}})

    def getuser(self,usrId):
        db = self.classter["Fembot"]
        User = db["User"]
        return User.find_one({"usrId":usrId})

    def OfferCreate(self,usrId,offerData,type):
        """type: mem, cit, fac, tik, voc"""
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        User = db["User"]
        if type == "voc":
            post = {"usrId":usrId,"offerData":offerData,"type":type,"caption":"caption","app":False}
            User.update_one({"usrId":usrId},{"$set":{"moder":Offer.insert_one(post).inserted_id}})
        else:
            post = {"usrId": usrId, "offerData": offerData, "type": type, "caption": "caption", "app": False}
            Offer.insert_one(post)



    def AddOfferCaption(self,usrId,caption):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        User = db["User"]
        Offer.update_one({"_id":ObjectId(User.find_one({"usrId":usrId})["moder"])},{"$set":{"caption":caption,"app": True}})



    def setOfferApp(self,offerId,appNo):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        Offer.update_one({"_id":ObjectId(offerId)},{"$set":{"app":appNo}})


    def getAllOffer(self):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        of = []
        cursor = Offer.find({})
        for document in cursor:
            if document["app"] is False:
                of.append(document)
        return of



    def getCitOffer(self):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        of = []
        cursor = Offer.find({})
        for document in cursor:
            if document["type"] == "cit"  and document["app"] is True:
                of.append(document)
        return of

    def getTikOffer(self):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        of = []
        cursor = Offer.find({})
        for document in cursor:
            if document["type"] == "tik" and document["app"] is True:
                of.append(document)
        return of

    def getMemOffer(self):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        of = []
        cursor = Offer.find({})
        for document in cursor:
            if document["type"] == "mem" and document["app"] is True:
                of.append(document)
        return of

    def getFacOffer(self):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        of = []
        cursor = Offer.find({})
        for document in cursor:
            if document[type] == "fac":
                of.append(document)
        return of

    def getVocOffer(self):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        of = []
        cursor = Offer.find({})
        for document in cursor:
            if document["type"] == "voc":
                of.append(document)
        return of




    def DellOffer(self,offId):
        db = self.classter["Fembot"]
        Offer = db["Offer"]
        Offer.remove({"_id":offId})

    def NewPostImage(self,usrId,img):
        db = self.classter["Fembot"]
        Post = db["Posts"]
        User = db["User"]
        post ={"text":"","img":img,}
        id = Post.insert_one(post).inserted_id
        User.update_one({"usrId":usrId},{"$set":{"postModer":id}})

    def NewPostText(self,usrId,text):
        db = self.classter["Fembot"]
        Post = db["Posts"]
        User = db["User"]
        id = User.find_one({"usrId":usrId})["postModer"]
        Post.update_one({"_id":ObjectId(id)},{"$set":{"text":text}})

    def NewPostGet(self,usrId):
        db = self.classter["Fembot"]
        Post = db["Posts"]
        User = db["User"]
        return Post.find_one({"_id":ObjectId(User.find_one({"usrId":usrId})["postModer"])})

    def getalluser(self):
        db = self.classter["Fembot"]
        User = db["User"]

        usr= []

        cursor = User.find({})
        for document in cursor:
            usr.append(document)

        return usr

# if I124Q < 3:
#   i = 4Q
