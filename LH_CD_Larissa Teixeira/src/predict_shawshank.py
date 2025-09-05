import re
import numpy as np
import pandas as pd
import joblib

# Carregar modelo salvo
model = joblib.load("model_imdb_rating.pkl")

shaw = {
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': '1994',
    'Certificate': 'A',
    'Runtime': '142 min',
    'Genre': 'Drama',
    'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
    'Meta_score': 80.0,
    'Director': 'Frank Darabont',
    'Star1': 'Tim Robbins',
    'Star2': 'Morgan Freeman',
    'Star3': 'Bob Gunton',
    'Star4': 'William Sadler',
    'No_of_Votes': 2343110,
    'Gross': '28,341,469'
}

def parse_single(d):
    return {
        'Released_Year_num': pd.to_numeric(d['Released_Year'], errors='coerce'),
        'Certificate': d['Certificate'],
        'Runtime_min': float(re.search(r'(\d+)', str(d['Runtime'])).group(1)) if re.search(r'(\d+)', str(d['Runtime'])) else np.nan,
        'Genre': d['Genre'],
        'Meta_score': d['Meta_score'],
        'Director': d['Director'],
        'Star1': d['Star1'],
        'Star2': d['Star2'],
        'Star3': d['Star3'],
        'Star4': d['Star4'],
        'No_of_Votes': d['No_of_Votes'],
        'Gross_num': float(str(d['Gross']).replace(',','').replace('$','')) if d['Gross'] else np.nan,
        'Overview': d['Overview']
    }

X_new = pd.DataFrame([parse_single(shaw)])

pred = model.predict(X_new)[0]
print("Previsão de IMDb Rating para The Shawshank Redemption:", round(float(pred), 3))
