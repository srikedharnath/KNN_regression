# KNN_regression

# KNN Regression Project

## Project Overview
This project demonstrates the implementation of the K-Nearest Neighbors (KNN) Regression algorithm using Python and Streamlit.

The model predicts continuous numerical values based on the nearest neighboring data points.

---

## Machine Learning Type
- Supervised Learning
- Regression
- K-Nearest Neighbors Regression (KNN Regressor)

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Dataset
The project uses a regression dataset for prediction.

Example:
- Student Marks Prediction
- House Price Prediction
- Salary Prediction

---

## Features Used
Example input features:
- Study Hours
- Experience
- Area
- Age

---

## Target Variable
The target variable contains continuous numerical values such as:
- Marks
- Salary
- Price

---

## Algorithm Used
```python
KNeighborsRegressor()
```

KNN Regression predicts values based on the average of nearest neighboring data points.

---

## Project Workflow
1. Data Collection
2. Data Preprocessing
3. Train Test Split
4. Model Training
5. Prediction
6. Model Evaluation
7. Streamlit Deployment

---

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R2 Score

---

## Streamlit Application
The Streamlit app allows users to:
- Enter input values
- Predict output values
- View prediction results instantly

Run the app using:

```bash
streamlit run app.py
```

---

## Project Structure

```bash
knn_regression/
│
├── app.py
├── kNN_regression.ipynb
├── requirements.txt
└── README.md
```

---

## requirements.txt

```txt
streamlit
pandas
numpy
scikit-learn
```

---

## Future Improvements
- Add larger datasets
- Improve UI design
- Add graphs and visualizations
- Deploy using Streamlit Cloud

---

## Conclusion
This project demonstrates how the K-Nearest Neighbors Regression algorithm can be used for predicting continuous numerical values using Python and Streamlit.
