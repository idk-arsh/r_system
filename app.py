import pandas as pd
from flask import Flask, request, render_template
from recommendation import UnifiedRecommendationSystem  # Ensure this import is correct

app = Flask(__name__)

# Load your dataset
data = pd.read_excel('./dataset.xlsx')
best_params = {'n_factors': 100, 'reg_all': 0.05}

# Initialize and train the recommendation system
rec_system = UnifiedRecommendationSystem(data, best_params)
rec_system.train_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        preferences = request.form.getlist('genre')
        
        if preferences:
            recommendations = rec_system.get_recommendations(preferences={'genres': preferences})
        else:
            recommendations = rec_system.get_recommendations()
        
        return render_template('home.html', recommendations=recommendations)
    else:
        return render_template('index.html')
    


