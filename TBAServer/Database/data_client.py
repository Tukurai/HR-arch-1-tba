#data_client.py

from pymongo import MongoClient    
   
class DataClient:    
    def __init__(self, host='20.126.90.236', port=27017, database='text-based-adventure'):    
        self.client = MongoClient(host, port)    
        self.db = self.client[database]    
        self.collections = {    
            'planets': self.db['planets'],    
            'fortresses': self.db['fortresses'],    
            'floors': self.db['floors'],    
            'rooms': self.db['rooms'],    
            'items': self.db['items'],    
            'players': self.db['players'],    
            'enemies': self.db['enemies']    
        }    

    def update(self, collection_name, query, new_values):  
        if collection_name not in self.collections:  
            raise ValueError(f'Invalid collection name: {collection_name}')  
        update_result = self.collections[collection_name].update_one(query, {'$set': new_values})  
        print(f'Modified {update_result.modified_count} documents')  
        return update_result.modified_count  
  
    def delete(self, collection_name, query):  
        if collection_name not in self.collections:  
            raise ValueError(f'Invalid collection name: {collection_name}')  
        delete_result = self.collections[collection_name].delete_one(query)  
        print(f'Deleted {delete_result.deleted_count} documents')  
        return delete_result.deleted_count  
    
    def save(self, collection_name, data):    
        if collection_name not in self.collections:    
            raise ValueError(f'Invalid collection name: {collection_name}')    
        if isinstance(data, list):  
            insert_result = self.collections[collection_name].insert_many(data)  
            print(f'Inserted docs with ids {insert_result.inserted_ids}')  
            return insert_result.inserted_ids  
        else:  
            insert_result = self.collections[collection_name].insert_one(data)    
            print(f'Inserted doc with id {insert_result.inserted_id}')    
            return insert_result.inserted_id    
  
    def load(self, collection_name, query={}):    
        if collection_name not in self.collections:    
            raise ValueError(f'Invalid collection name: {collection_name}')    
        result = self.collections[collection_name].find(query)  
        return [doc for doc in result]  
    
    def load_single(self, collection_name, query={}):      
        if collection_name not in self.collections:      
            raise ValueError(f'Invalid collection name: {collection_name}')      
        result = self.collections[collection_name].find_one(query)    
        return result  # This will return a single document matching the query or None  
