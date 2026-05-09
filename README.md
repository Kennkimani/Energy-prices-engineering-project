⚡ Global Energy Price Data Engineering Platform
An automated data pipeline that ingests, stores, and visualizes real-time energy prices using the EIA Open Data API.
🏗️ ArchitectureSource:
 U.S. Energy Information Administration (EIA) APIOrchestration: APScheduler (Simulating enterprise Airflow orchestration)Storage: MongoDB Atlas (NoSQL Cloud Database)Backend: Flask (RESTful API to serve data)Dashboard: MongoDB Atlas Charts (Live Data Visualization)
🚀 FeaturesAutomated Ingestion:
  Python script fetches weekly fuel and monthly electricity/gas data.Data Quality: Metadata tagging and timestamping for ingestion tracking.RESTful API: Flask endpoint at /api/prices/latest for third-party integrations.Live Monitoring: Real-time dashboard showing commodity price trends.
🛠️ Setup & UsageEnvironment: 
  Create a .env file with your API_KEY and MONGO_URL.Run Pipeline: uv run ingest.py (Starts the 24-hour automated scheduler).Run API: uv run app.py (Exposes data at localhost:5000).
📊 Business Value
This platform eliminates manual CSV tracking, providing a "single source of truth" for energy market analysis and business forecasting