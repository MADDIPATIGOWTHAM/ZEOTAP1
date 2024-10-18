
### `config.py`

# Configuration settings for the weather monitoring system

API_KEY = 'b5679720c29f578aaae62a169240f26f'  # Replace with your OpenWeatherMap API key
# config.py
THRESHOLDS = {
    'temperature': 35,  # Temperature threshold in degrees Celsius
    'condition': 'Rain',  # Example condition for alerts
    'consecutive_updates': 2  # Number of consecutive updates to breach the threshold
}

