from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db['UserNum']

UserNum.insert({
    'number_of_users':0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['number_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {'$set':{'number_of_users':new_num}})
        return str("hello user" + str(new_num))


def checkPostedData(postedData, functionName):
    if (functionName == 'add' or functionName == 'sub' or functionName == 'mul'):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif (functionName == "div"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200

class Add(Resource):
    #Here I'm gonna use POST request
    def post(self):
        postedData = request.get_json()

        #Here I.m gonna check the validity of posted data
        status_code = checkPostedData(postedData, 'add')
        if (status_code != 200):
            retJson = {
                'message':'ERROR! Somthing unusual happened',
                'status_code':status_code
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])

        ret = x + y
        retMap = {
            'message': ret,
            'status code': 200
        }
        return jsonify(retMap)

class Sub(Resource):
    def post(self):
        postedData = request.get_json()

        #Here I.m gonna check the validity of posted data
        status_code = checkPostedData(postedData, 'sub')
        if (status_code != 200):
            retJson = {
                'message':'ERROR! Somthing unusual happened',
                'status_code':status_code
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])

        ret = x - y
        retMap = {
            'message': ret,
            'status code': 200
        }
        return jsonify(retMap)

class Div(Resource):
    def post(self):
        postedData = request.get_json()

        #Here I.m gonna check the validity of posted data
        status_code = checkPostedData(postedData, 'div')
        if (status_code != 200):
            retJson = {
                'message':'ERROR! Somthing unusual happened',
                'status_code':status_code
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])

        ret = (x*1.0) / y
        retMap = {
            'message': ret,
            'status code': 200
        }
        return jsonify(retMap)

class Mul(Resource):
    def post(self):
        postedData = request.get_json()

        #Here I.m gonna check the validity of posted data
        status_code = checkPostedData(postedData, 'mul')
        if (status_code != 200):
            retJson = {
                'message':'ERROR! Somthing unusual happened',
                'status_code':status_code
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])

        ret = x * y
        retMap = {
            'message': ret,
            'status code': 200
        }
        return jsonify(retMap)

api.add_resource(Add, '/add')
api.add_resource(Sub, '/sub')
api.add_resource(Mul, '/mul')
api.add_resource(Div, '/div')
api.add_resource(Visit, '/hello')

@app.route('/')
def index():
    return 'hello_world1234567890'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
