import os
import json
import requests
from datetime import datetime,timezone
from dotenv import load_dotenv
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler

load_dotenv()

# --- CONFIGURATION ---
API_KEY = os.getenv('API_KEY')
MONGO_URI = os.getenv('MONGO_URL')

client = MongoClient(MONGO_URI)
db = client['energy_db']
collection = db['raw_energy_data']

energy_sources = {
    "fuel": "petroleum/pri/gnd/data",
    "electricity": "electricity/retail-sales/data",
    "natural_gas": "natural-gas/pri/sum/data"
}

# --- THE INGESTION LOGIC ---
def run_pipeline():
    print(f" Pipeline started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    for name, route in energy_sources.items():
        url = f"https://api.eia.gov/v2/{route}"
        data_type = "price" if name == "electricity" else "value"
        facets = {"sectorid": ["RES"]} if name == "electricity" else {}
        
        header_params = {
            "frequency": "monthly" if name != "fuel" else "weekly",
            "data": [data_type],
            "facets": facets,
            "sort": [{"column": "period", "direction": "desc"}],
            "length": 1
        }

        try:
            response = requests.get(
                url, 
                params={"api_key": API_KEY},
                headers={"X-Params": json.dumps(header_params)}
            )
            
            if response.status_code == 200:
                data_list = response.json().get('response', {}).get('data', [])
                if data_list:
                    record = data_list[0]
                    record['commodity_type'] = name
                    record['ingested_at'] = datetime.now(timezone.utc)
                    
                    collection.insert_one(record)
                    print(f"{name.upper()} ingested.")
            else:
                print(f"{name.upper()} failed: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
            
    print("💤 Pipeline finished. Waiting for next interval...")

# --- THE SCHEDULER ---
if __name__ == "__main__":
    scheduler = BlockingScheduler()
    
    # Run once immediately when we start
    run_pipeline()
    
    # Schedule to run every 24 hours (or change hours=1 for testing)
    scheduler.add_job(run_pipeline, 'interval', hours=24)
    
    print("⏰ Scheduler is active. Press Ctrl+C to stop.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
