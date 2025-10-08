from flask import Flask, jsonify, send_from_directory
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# --- Mock Data Simulation (Replaces Firestore/Database) ---
def generate_mock_reports(count=5):
    """Generates a list of mock solar report data."""
    reports = []
    site_names = ["Apex Solar Farm 1", "Desert Sun Array", "Industrial Rooftop 3", "Coastal Wind-Solar Hybrid", "Urban Microgrid Alpha"]
    
    for i in range(count):
        date = (datetime.now() - timedelta(days=random.randint(1, 60), hours=random.randint(0, 23))).isoformat()
        
        reports.append({
            "id": str(i + 1),
            "siteName": random.choice(site_names),
            "defectCount": random.randint(5, 150),
            "severity": random.choice(["Low", "Medium", "High", "Critical"]),
            "date": date,
            "panelCount": random.randint(800, 5000)
        })
        
    return reports

mock_data = generate_mock_reports()

# --- API Endpoints (Simulating Node I) ---

@app.route('/')
def serve_index():
    """Serves the main dashboard HTML file."""
    # Note: In a real environment, you'd use render_template, but here we serve it directly.
    return send_from_directory('.', 'index.html')

@app.route('/api/reports', methods=['GET'])
def get_reports():
    """Returns the list of solar inspection reports."""
    # Simulates fetching data from the PostgreSQL/PostGIS DB (Node H)
    return jsonify(mock_data)

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible outside the local machine if needed.
    # debug=True allows for automatic reloading during development.
    app.run(debug=True, host='0.0.0.0', port=5000)
