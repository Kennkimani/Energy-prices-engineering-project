from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app) # This allows your dashboard or other sites to talk to your API

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URL')
client = MongoClient(MONGO_URI)
db = client['energy_db']
collection = db['raw_energy_data']

@app.route('/api/v1/prices', methods=['GET'])
def get_prices():
    """
    Returns the latest price for a specific commodity or all of them.
    Usage: /api/v1/prices?type=fuel
    """
    commodity_type = request.args.get('type')
    
    if commodity_type:
        # Get latest for one specific type
        results = collection.find(
            {"commodity_type": commodity_type},
            {"_id": 0}
        ).sort("ingested_at", -1).limit(1)
    else:
        # Get latest for ALL types
        # We use aggregation to find the most recent record for each group
        pipeline = [
            {"$sort": {"ingested_at": -1}},
            {"$group": {
                "_id": "$commodity_type",
                "latest_record": {"$first": "$$ROOT"}
            }},
            {"$replaceRoot": {"newRoot": "$latest_record"}},
            {"$project": {"_id": 0}}
        ]
        results = collection.aggregate(pipeline)

    return jsonify(list(results))

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "database": "connected"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
