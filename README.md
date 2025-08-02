# 🚢 Titanic Survival Prediction

This project uses machine learning to predict whether a passenger survived the Titanic disaster based on various features like age, sex, passenger class, fare, and more.

---

## 📊 Dataset

- **Source:** [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- **File:** Titanic-Dataset.csv  
- The dataset contains details like:
  - Passenger class (Pclass)
  - Sex
  - Age
  - Fare
  - Embarked (Port of boarding)
  - Survived (0 = No, 1 = Yes)

---

## 🛠️ Technologies & Libraries

- **Language:** Python
- **Libraries Used:**
  - `pandas` – Data manipulation
  - `numpy` – Numerical operations
  - `matplotlib` and `seaborn` – Data visualization
  - `scikit-learn` – Machine Learning model and evaluation

---

## 🧠 Model Used

- ✅ **Random Forest Classifier**  
A robust ensemble model used for classification.  
It works well with both numerical and categorical features.

---

## 📈 Project Highlights

- Data cleaning: Handled missing values, dropped unnecessary columns
- Label encoding for categorical data (Sex, Embarked)
- Performed Exploratory Data Analysis:
  - Correlation heatmap
  - Survival vs Gender analysis
- Split data into training and testing sets (80:20)
- Trained model using Random Forest Classifier
- Evaluated using:
  - Accuracy score
  - Confusion matrix
  - Classification report

---

## 📊 Output Overview

- 📌 Correlation Matrix (EDA)
- 📌 Bar Plot: Survival by Gender
- 📌 Accuracy Score
- 📌 Confusion Matrix
- 📌 Precision, Recall, F1-score

---

## 🔮 Scope for Improvement

- Try other classification models (Logistic Regression, SVM, KNN)
- Use cross-validation for more robust performance
- Apply GridSearchCV for hyperparameter tuning
- Create a frontend using Streamlit for interactive predictions
- Save and load model using `pickle` or `joblib`

---