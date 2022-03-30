from flask import Flask, Response, request
#use .\activate on VSC terminal in the Scripts dir to run further python commands
app = Flask(__name__)

#database connection

import pymongo
import json
from bson.objectid import ObjectId
try:

    mongo = pymongo.MongoClient(
        host="localhost", 
    port=27017,
    serverSelectionTimeoutMS = 1000
    )
#on Postman, POST requests are being sucessful for test using http://127.0.0.1:88/users 

#database creation

    db = mongo.company 


    mongo.server_info() #trigger exception if cannot connect to database
    
except:
    print("ERROR - Cannot connect to database")


##############################
#Routes
#Create
@app.route("/users", methods=["POST"])

def create_user():

    try:

        user = {"name":request.form["name"], 
        "lastName":request.form["lastname"]
        }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response=json.dumps(
                {"message":"user created","id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
        # for attr in dir(dbResponse):
        #     print(attr)

    except Exception as ex:
        print(ex)


#Read
@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])


        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
        )


    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message":"cannot read users"}),
            status=500,
            mimetype="application/json"
        )


#Update/Patch
@app.route("/users/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"name":request.form["name"]}}
        )
        # for attr in dir(dbResponse):
        #     print(f"{attr}")

        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message":"user updated"}),
                status=200,
                mimetype="application/json"
            )
        
        return Response(
            response=json.dumps(
                 {"message":"nothing due to update "}),
            status=200,
            mimetype="application/json"
         )
     


    except Exception as ex:

         return Response(
            response=json.dumps(
                {"message":"user update not avaiable"}),
            status=500,
            mimetype="application/json"
        )


#Delete
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id": ObjectId(id)})
        # for attr in dir(dbResponse):
        #     print(f"***{attr}***")
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message":"user deleted","id":f"{id}"}),
                 status=200,
                    mimetype="application/json"
            )

        return Response(
            response=json.dumps(
                {"message":"user not found"}),
            status=500,
            mimetype="application/json"
        )

    except Exception as ex:
        return Response(
            response=json.dumps(
                {"message":"cannot delete user"}),
            status=500,
            mimetype="application/json"
        )



############################## 


if __name__  == "__main__":

    app.run(port=88, debug=True)
    #port changed from 80 to 88 - maybe an oversight from previus laravel 8 CRUD also using port 80?



