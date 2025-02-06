import pandas as pd
import numpy as np
from datetime import datetime

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.process_data()

    def process_data(self):
        # Convert publish time to datetime
        self.data['Publish time'] = pd.to_datetime(self.data['Publish time'])

        # Extract time components
        self.data['Hour'] = self.data['Publish time'].dt.hour
        self.data['Day'] = self.data['Publish time'].dt.day_name()
        self.data['Month'] = self.data['Publish time'].dt.month_name()

        # Calculate engagement rate
        self.data['Engagement Rate'] = (self.data['Likes'] + self.data['Comments']) / self.data['Impressions'] * 100

        # Clean numerical columns
        numeric_cols = ['Impressions', 'Reach', 'Likes', 'Comments', 'Saves', 'Shares']
        self.data[numeric_cols] = self.data[numeric_cols].fillna(0)

        # Process post type
        self.data['Post type'] = self.data['Post type'].fillna('Unknown')

    def get_engagement_metrics(self):
        metrics = {
            'Total Posts': len(self.data),
            'Average Likes': self.data['Likes'].mean(),
            'Average Comments': self.data['Comments'].mean(),
            'Average Engagement Rate': self.data['Engagement Rate'].mean(),
            'Total Impressions': self.data['Impressions'].sum()
        }
        return metrics

    def get_best_posting_times(self):
        hourly_engagement = self.data.groupby('Hour')['Engagement Rate'].mean()
        return hourly_engagement.sort_values(ascending=False)

    def get_post_type_analysis(self):
        return self.data.groupby('Post type').agg({
            'Engagement Rate': 'mean',
            'Likes': 'mean',
            'Comments': 'mean'
        }).round(2)

    def prepare_ml_features(self):
        features = self.data[['Hour', 'Likes', 'Comments', 'Shares', 'Saves']]
        target = self.data['Impressions']
        return features, target