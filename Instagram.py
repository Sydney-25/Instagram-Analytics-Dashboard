import streamlit as st
import pandas as pd
from utils.data_processor import DataProcessor
from utils.ml_models import EngagementPredictor
from utils.visualizations import DashboardVisualizer
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Instagram Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load custom CSS
def load_css():
    css_file = 'assets/custom.css'
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            body {
                font-family: sans-serif;
            }
            /* Default Streamlit CSS */
            .css-1d391kg {
                padding: 0px 5rem;
            }
            .css-2trqyj {
                font-size: 2rem;
            }
            </style>
        """, unsafe_allow_html=True)

load_css()

# Header
st.title("📊 Instagram Analytics Dashboard")
st.markdown("Analyze your Instagram performance with ML-powered insights")

# File upload
uploaded_file = st.file_uploader("Upload your Instagram data CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        processor = DataProcessor(data)
        visualizer = DashboardVisualizer(data)

        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        metrics = processor.get_engagement_metrics()

        with col1:
            st.markdown(
                """
                <div class="card">
                    <div class="metric-value">{:,.0f}</div>
                    <div class="metric-label">Total Posts</div>
                </div>
                """.format(metrics['Total Posts']),
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                """
                <div class="card">
                    <div class="metric-value">{:,.0f}</div>
                    <div class="metric-label">Avg. Likes</div>
                </div>
                """.format(metrics['Average Likes']),
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                """
                <div class="card">
                    <div class="metric-value">{:.2f}%</div>
                    <div class="metric-label">Avg. Engagement Rate</div>
                </div>
                """.format(metrics['Average Engagement Rate']),
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                """
                <div class="card">
                    <div class="metric-value">{:,.0f}</div>
                    <div class="metric-label">Total Impressions</div>
                </div>
                """.format(metrics['Total Impressions']),
                unsafe_allow_html=True
            )

        # Engagement Trends
        st.subheader("📈 Engagement Analysis")
        tab1, tab2, tab3 = st.tabs(["Engagement Trend", "Posting Times", "Post Types"])

        with tab1:
            st.plotly_chart(visualizer.create_engagement_trend(), use_container_width=True)

        with tab2:
            st.plotly_chart(visualizer.create_posting_time_heatmap(), use_container_width=True)

        with tab3:
            st.plotly_chart(visualizer.create_post_type_comparison(), use_container_width=True)

        # ML Insights
        st.subheader("🤖 ML-Powered Insights")

        features, target = processor.prepare_ml_features()
        predictor = EngagementPredictor()
        metrics, feature_importance = predictor.train(features, target)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
                <div class="card">
                    <h3>Model Performance</h3>
                    <p>R² Score: {:.2f}</p>
                    <p>RMSE: {:.2f}</p>
                </div>
                """.format(metrics['R2 Score'], metrics['RMSE']),
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                """
                <div class="card">
                    <h3>Feature Importance</h3>
                    <pre>{}</pre>
                </div>
                """.format('\n'.join([f'{k}: {v:.3f}' for k, v in feature_importance.items()])),
                unsafe_allow_html=True
            )

    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        st.info("Please ensure your CSV file has the required columns: Publish time, Likes, Comments, Impressions, Post type, etc.")
else:
    st.info("👆 Upload your Instagram data CSV file to get started")

    # Show sample metrics layout with placeholder data
    col1, col2, col3, col4 = st.columns(4)
    placeholder_metrics = [
        ("--", "Total Posts"),
        ("--", "Avg. Likes"),
        ("--", "Avg. Engagement Rate"),
        ("--", "Total Impressions")
    ]

    for col, (value, label) in zip([col1, col2, col3, col4], placeholder_metrics):
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
