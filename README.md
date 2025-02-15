

# Instagram Analytics Dashboard

Analyze your Instagram performance with ML-powered insights.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

The **Instagram Analytics Dashboard** is an interactive web application built with Streamlit that helps you analyze your Instagram performance through advanced data processing, interactive visualizations, and machine learning insights. Easily upload your Instagram CSV data and explore key metrics like total posts, average likes, engagement rate, and impressions—all in one intuitive dashboard.

## Features

- **Data Upload**: Seamlessly upload your Instagram data in CSV format.
- **Automated Data Processing**: Computes essential engagement metrics such as Total Posts, Avg. Likes, Avg. Engagement Rate, and Total Impressions.
- **Interactive Visualizations**: Explore your data with Plotly charts including:
  - Engagement Trends
  - Posting Time Heatmaps
  - Post Type Comparisons
- **ML-Powered Insights**: Train a machine learning model to assess engagement performance and view feature importance.
- **Downloadable Project Files**: Use the sidebar download button to get a ZIP archive containing essential project files (e.g., insta.py, README.md, and requirements.txt).

## Installation

Clone the Repository:

```bash
git clone https://github.com/yourusername/instagram-analytics-dashboard.git
cd instagram-analytics-dashboard
```

### Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure you have the following libraries installed:
- Streamlit
- Pandas
- Plotly

## Usage

Start the Application:

```bash
streamlit run insta.py
```

1. **Upload Your Data**: Click the file uploader to select your Instagram CSV data file.
2. **View Analytics**: The dashboard will display key metrics and interactive visualizations such as engagement trends, posting times, and post type comparisons.
3. **ML Insights**: The app trains a model to provide insights like R² Score, RMSE, and feature importance for engagement prediction.
4. **Download Project Files**: Use the sidebar download button to get a ZIP file of project essentials.

## Project Structure

```
instagram-analytics-dashboard/
├── insta.py                # Main application file for the Streamlit app
├── README.md               # Project documentation (this file)
├── requirements.txt        # List of Python dependencies
├── assets/
│   └── custom.css          # Custom CSS styles for the app
└── utils/
    ├── data_processor.py   # Processes Instagram data and computes engagement metrics
    ├── ml_models.py        # Contains the ML model for engagement prediction
    └── visualizations.py   # Generates interactive Plotly visualizations
```

Ensure the directory structure is maintained so that modules are correctly imported.

## Customization

- **Styling**: Modify `assets/custom.css` to tailor the visual appearance of the dashboard.
- **Data Processing & ML**: Update `utils/data_processor.py` and `utils/ml_models.py` to adjust data handling and prediction logic.
- **Visualizations**: Customize charts by editing `utils/visualizations.py` to better suit your analysis needs.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes.
4. Push the branch and open a pull request.


## Contact

For any questions or suggestions, please reach out at: sydney.abuto@gmail.com.
