# Progalused

Programmeerimise alused (Programming Basics)

This repository contains basic Python programming examples and a Flask web application demonstrating car price history visualization.

## Web Application

The repository includes a Flask web application that displays car listing information with price history charts.

### Running the application

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

### Features

- **Home page**: Simple navigation to different sections
- **Hinnalugu (Price History)**: Displays car listing details with:
  - Car specifications (year, mileage, engine, etc.)
  - Price information in Estonian format
  - Interactive price history chart using custom SVG implementation
  - Recent price data table
  - Estonian language interface

The price history page demonstrates:
- Jinja2 templating
- SVG-based data visualization
- Responsive design
- Estonian localization
