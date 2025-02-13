
# Instagram Analytics Dashboard

A Streamlit-based analytics dashboard that provides ML-powered insights for Instagram performance data.

## Features

- Upload and analyze Instagram data in CSV format
- View key engagement metrics and trends
- Interactive visualizations including:
  - Engagement rate trends
  - Best posting times heatmap
  - Post type performance comparison
- ML-powered insights using Random Forest model
- Modern, dark-themed UI with Google-inspired design

## Requirements

- Python 3.11+
- Required packages listed in requirements.txt

## Usage

1. Upload your Instagram data CSV file (should include: Publish time, Likes, Comments, Impressions, Post type)
2. View automatically generated analytics and insights
3. Explore different visualization tabs for detailed analysis

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run main.py`

## Project Structure

```
├── assets/
│   └── custom.css         # Custom styling
├── utils/
│   ├── data_processor.py  # Data processing logic
│   ├── ml_models.py       # ML model implementation
│   └── visualizations.py  # Visualization components
└── main.py               # Main application
```
