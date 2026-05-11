Key Highlights
 Data Pipeline: Ingestion → Validation → Multi-Source Normalization (EIA API + MongoDB Atlas).
 Automated Daily Pipeline: Fully scheduled ingestion engine using APScheduler to ensure real-time market snapshots     without manual intervention.
 Architecture: Robust ELT flow designed for high-availability energy market intelligence.
 Backend & API: Flask-powered REST API delivering filtered JSON payloads for downstream consumption.
 Live Analytics: Real-time MongoDB Atlas Charts dashboard with calculated field normalization for unified price  tracking.
 Data Engineering Focus: Schema mapping, metadata injection (lineage tracking), and cloud database optimization.
 Live Platform
 → https://kennkimani.github.io/Energy-prices-engineering-project/
 System Architecture
 This project simulates a real-world analytics backend for an energy intelligence startup:
 1.Extraction: Python services interface with the EIA Open Data API using advanced header-based parameterization to bypass URL encoding limitations.
 2.Storage: Data is persisted in a MongoDB Atlas NoSQL cluster, utilizing BSON for flexible handling of disparate energy commodity schemas.
 3.Orchestration: The system maintains a continuous "Heartbeat" to trigger daily updates, ensuring the dashboard reflects the latest global price shifts.
 4.Delivery: A Flask backend serves as the production bridge, providing a scalable interface for data retrieval.
Tech StackData:
 Python (Requests, Pandas, JSON)
 Database: MongoDB Atlas (NoSQL), PyMongo
 Orchestration: APScheduler (Production-ready Task Scheduling)
 Backend: Flask (REST API Development)
 Frontend: HTML5, CSS3, MongoDB Atlas Charts Embedding
 Deployment: GitHub Pages
Performance & Engineering Goals
 Zero-Touch Automation: Designed to run 24/7 with built-in error handling for API rate limits and connection failures.
 Unified Schema: Successfully merged different data structures (Fuel, Electricity, Natural Gas) into a single, queryable analytics view.
 Scalability: Built with a focus on real production workflows for Data Engineering and Backend Developer roles.
