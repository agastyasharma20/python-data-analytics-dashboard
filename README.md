# Python Data Collection & Visualization Web App

## Overview
This is a Python-based web application built to demonstrate clean data collection, structured data processing, and clear data visualization.  
The focus of this project is on clarity, logical data flow, and maintainable structure, with complete source-code handover and documentation.

---

## Tech Stack
- Python  
- Flask  
- SQLite  
- Pandas  
- Plotly  
- HTML, CSS  

---

## What We’re Building
The application includes:
- Data collection through a web interface  
- Backend data handling and processing  
- Interactive data visualization dashboards  

The system is designed to clearly show how data moves from input → processing → visualization.

---

## Data Flow & Structure
- Input data is collected via web forms  
- Server-side validation ensures clean data  
- Data is stored and processed using a structured pipeline  
- Processed data is passed to the visualization layer  
- Visual insights are rendered using interactive charts  

The internal data flow is intentionally kept **clean, intuitive, and easy to understand**, with modular separation of concerns.

---

## Key Features
- Python-based backend development  
- Structured data collection and handling  
- Clean and logical data pipelines  
- Interactive data visualizations  
- Category-based filtering  
- CSV data export  
- JSON API endpoint for future integrations  

---

## Project Structure
python-data-dashboard/
├── app.py
├── config.py
├── models/
├── services/
├── routes/
├── templates/
├── static/
└── requirements.txt

The structure is modular and scalable, making it easy for another developer to understand and extend the codebase.

---

## Setup & Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


http://127.0.0.1:5000/
