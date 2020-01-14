# mongo_connector with Docker
web_1  |     raise ServerSelectionTimeoutError( web_1  | pymongo.errors.ServerSelectionTimeoutError: db:27017: [Errno -2] Name or service not known

-------Here is my code ---------

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017/")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'number_of_users': 0
})

class Visit(Resource):
    def get():
        prev_num = UserNum.find({})[0]['number_of_users']
        new_num = prev_num + 1
        user_one.update({}, {"$set":{"users":new_user}})
        return str("Hello user" + str(new_num))
        
api.add_resource(Visit, '/hello')

@app.route('/')
def index():
    return 'hello_world1234567890'

if __name__=='__main__':
    app.run(host='0.0.0.0')   
    
  
--------------end------------------  


----------Issue I Got-----------

web_1  | app.py:13: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
web_1  |   UserNum.insert({
web_1  | Traceback (most recent call last):
web_1  |   File "app.py", line 13, in <module>
web_1  |     UserNum.insert({
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/collection.py", line 3181, in insert
web_1  |     return self._insert(doc_or_docs, not continue_on_error,
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/collection.py", line 610, in _insert
web_1  |     return self._insert_one(
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/collection.py", line 599, in _insert_one
web_1  |     self.__database.client._retryable_write(
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/mongo_client.py", line 1490, in _retryable_write
web_1  |     with self._tmp_session(session) as s:
web_1  |   File "/usr/local/lib/python3.8/contextlib.py", line 113, in __enter__
web_1  |     return next(self.gen)
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/mongo_client.py", line 1823, in _tmp_session
web_1  |     s = self._ensure_session(session)
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/mongo_client.py", line 1810, in _ensure_session
web_1  |     return self.__start_session(True, causal_consistency=False)
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/mongo_client.py", line 1763, in __start_session
web_1  |     server_session = self._get_server_session()
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/mongo_client.py", line 1796, in _get_server_session
web_1  |     return self._topology.get_server_session()
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/topology.py", line 482, in get_server_session
web_1  |     self._select_servers_loop(
web_1  |   File "/usr/local/lib/python3.8/site-packages/pymongo/topology.py", line 208, in _select_servers_loop
web_1  |     raise ServerSelectionTimeoutError(
web_1  | pymongo.errors.ServerSelectionTimeoutError: mongodb:27017: [Errno -2] Name or service not known
manthan_web_1 exited with code 1

------------end---------------

#python #mongodb #docker #api #linux
    
