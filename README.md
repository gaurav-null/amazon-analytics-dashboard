# Amazon Analytics Dashboard

A modern, responsive analytics dashboard built with Dash and Plotly, featuring a sleek dark theme with neumorphic design elements.

## Overview

Nebula Analytics Dashboard is a web-based analytics platform that provides a visually striking interface for data visualization and business intelligence. Built with Python's Dash framework, it combines powerful data processing capabilities with an intuitive user interface.

## Features

- **Modern Dark Theme**: Sleek dark interface with gradient accents and neumorphic design elements
- **Responsive Layout**: Fully responsive design that works on desktop and mobile devices
- **Interactive Visualizations**: Dynamic charts and graphs powered by Plotly
- **Comprehensive Filtering**: Multiple filter options including date ranges, categories, devices, and price ranges
- **Real-time Updates**: Data refreshes automatically without page reloads
- **Bootstrap Integration**: Leverages Dash Bootstrap Components for consistent UI elements

## Requirements

- Python 3.7+
- Dash 2.0+
- Plotly 5.0+
- Pandas
- NumPy
- Dash Bootstrap Components
- Faker (for demo data generation)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/gaurav-null/amazon-analytics-dashboard.git
   cd nebula-analytics-dashboard
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to http://127.0.0.1:8050/

## Project Structure

```
nebula-analytics-dashboard/
├── app.py               # Main application file
├── assets/              # Static assets (CSS, images)
│   └── logo.png         # Dashboard logo
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Usage

1. **Filtering Data**:
   - Use the date picker to select a specific time range
   - Filter by product categories using the dropdown
   - Filter by device type (mobile, desktop, tablet)
   - Use the price range slider to filter products by price

2. **KPI Cards**:
   - View key performance indicators at a glance
   - Cards update dynamically based on selected filters

3. **Charts and Visualizations**:
   - Analyze trends over time with line charts
   - View distribution data with pie charts
   - All visualizations update automatically when filters change

- Inter font family for the clean typography
