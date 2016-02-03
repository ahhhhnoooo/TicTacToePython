import pymongo

def add_record(timestamp,duration,winner):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['tictactoerecordsdb']
    colle = db['tictactoerecords']
    game_result = {
        "timestamp":timestamp,
        "duration":duration,
        "winner":winner
        }
    colle.insert_one(game_result)
    client.close()

def get_all_records():   
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['tictactoerecordsdb']
    colle = db['tictactoerecords']
    records = colle.find()
    client.close()
    return records

def remove_all_records():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['tictactoerecordsdb']
    db['tictactoerecords'].drop()
    client.close()