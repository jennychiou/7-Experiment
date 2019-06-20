from pymongo import MongoClient
from datetime import datetime
import json

'''
This class for store logs of user listening and survey results.
'''
class RecSysLogsToMongo():
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['recSys']
        self.logs = db['logs']
        self.survey = db['survey']

    def insert_log_to_mongodb(self, data):
        data = json.loads(data.decode('utf8'))
        data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.logs.insert_one(data)
        print('Insert data:', data)

    def insert_servey_results_to_mongodb(self, data):
        '''
        mongo search query:
            db.survey.find({"user":"plusone"}).sort({"_id":-1}).limit(1)
        '''
        data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.survey.insert_one(data)
        print('* Insert Survey Result from user', data['user'] +'.')