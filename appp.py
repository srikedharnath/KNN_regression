import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsRegressor


st.title("House Price Prediction using KNN Regression")

st.write("Enter house details below:")


df = pd.read_csv("Housing.csv")


le = LabelEncoder()

df['mainroad'] = le.fit_transform(df['mainroad'])
df['guestroom'] = le.fit_transform(df['guestroom'])
df['basement'] = le.fit_transform(df['basement'])
df['hotwaterheating'] = le.fit_transform(df['hotwaterheating'])
df['airconditioning'] = le.fit_transform(df['airconditioning'])
df['prefarea'] = le.fit_transform(df['prefarea'])
df['furnishingstatus'] = le.fit_transform(df['furnishingstatus'])


X = df.drop("price", axis=1)

y = df["price"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


model = KNeighborsRegressor(
    n_neighbors=5,
    metric='minkowski',
    p=2
)


model.fit(X_train, y_train)


area = st.number_input("Area")

bedrooms = st.number_input("Bedrooms")

bathrooms = st.number_input("Bathrooms")

stories = st.number_input("Stories")

mainroad = st.selectbox("Main Road", ["yes", "no"])

guestroom = st.selectbox("Guest Room", ["yes", "no"])

basement = st.selectbox("Basement", ["yes", "no"])

hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])

airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])

parking = st.number_input("Parking")

prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

mainroad = 1 if mainroad == "yes" else 0
guestroom = 1 if guestroom == "yes" else 0
basement = 1 if basement == "yes" else 0
hotwaterheating = 1 if hotwaterheating == "yes" else 0
airconditioning = 1 if airconditioning == "yes" else 0
prefarea = 1 if prefarea == "yes" else 0

furnishing_map = {
    "furnished": 0,
    "semi-furnished": 1,
    "unfurnished": 2
}

furnishingstatus = furnishing_map[furnishingstatus]


if st.button("Predict Price"):

    input_data = pd.DataFrame(
        [[
            area,
            bedrooms,
            bathrooms,
            stories,
            mainroad,
            guestroom,
            basement,
            hotwaterheating,
            airconditioning,
            parking,
            prefarea,
            furnishingstatus
        ]],
        columns=X.columns
    )

    
    input_data = scaler.transform(input_data)

   
    prediction = model.predict(input_data)

    
    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")