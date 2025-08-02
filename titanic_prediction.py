import pandas as pd
from sklearn.model_selection import train_test_split
from src.preprocess import clean_data
from src.model import train_model, evaluate_model
from src.visualize import plot_correlation, plot_survival_by_sex

# Load data
df = pd.read_csv('Titanic-Dataset.csv')
print("✅ Dataset loaded!")

# Clean
df = clean_data(df)

# Visualize
plot_correlation(df)
plot_survival_by_sex(df)

# Split
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = train_model(X_train, y_train)

# Evaluate
evaluate_model(model, X_test, y_test)