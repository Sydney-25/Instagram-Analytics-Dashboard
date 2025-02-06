from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class EngagementPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        
    def train(self, features, target):
        X_train, X_test, y_train, y_test = train_test_split(
            features, target, test_size=0.2, random_state=42
        )
        
        self.model.fit(X_train, y_train)
        
        predictions = self.model.predict(X_test)
        metrics = {
            'R2 Score': r2_score(y_test, predictions),
            'RMSE': np.sqrt(mean_squared_error(y_test, predictions))
        }
        
        feature_importance = dict(zip(features.columns, 
                                    self.model.feature_importances_))
        
        return metrics, feature_importance
    
    def predict(self, features):
        return self.model.predict(features)
