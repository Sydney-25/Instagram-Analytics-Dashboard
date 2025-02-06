import plotly.graph_objects as go
import plotly.express as px

class DashboardVisualizer:
    def __init__(self, data):
        self.data = data
        self.template = "plotly_dark"
        self.colors = {
            'primary': '#4285F4',
            'secondary': '#34A853',
            'accent': '#FBBC05'
        }

    def create_engagement_trend(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.data['Publish time'],
            y=self.data['Engagement Rate'],
            mode='lines+markers',
            name='Engagement Rate',
            line=dict(color=self.colors['primary'])
        ))
        fig.update_layout(
            template=self.template,
            title='Engagement Rate Trend Over Time',
            xaxis_title='Date',
            yaxis_title='Engagement Rate (%)',
            showlegend=True
        )
        return fig

    def create_posting_time_heatmap(self):
        hourly_data = self.data.pivot_table(
            values='Engagement Rate',
            index='Day',
            columns='Hour',
            aggfunc='mean'
        )
        
        fig = go.Figure(data=go.Heatmap(
            z=hourly_data.values,
            x=hourly_data.columns,
            y=hourly_data.index,
            colorscale='Blues'
        ))
        
        fig.update_layout(
            template=self.template,
            title='Best Posting Times (Engagement Rate)',
            xaxis_title='Hour of Day',
            yaxis_title='Day of Week'
        )
        return fig

    def create_post_type_comparison(self):
        post_type_metrics = self.data.groupby('Post type').agg({
            'Engagement Rate': 'mean',
            'Likes': 'mean',
            'Comments': 'mean'
        }).reset_index()

        fig = px.bar(
            post_type_metrics,
            x='Post type',
            y=['Engagement Rate', 'Likes', 'Comments'],
            barmode='group',
            color_discrete_sequence=[self.colors['primary'], 
                                   self.colors['secondary'], 
                                   self.colors['accent']]
        )
        
        fig.update_layout(
            template=self.template,
            title='Performance by Post Type',
            xaxis_title='Post Type',
            yaxis_title='Average Value'
        )
        return fig
