import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model pipeline
TARGET = "math score"
with open(f"models/{TARGET}_model.pkl", 'rb') as file:
    model_pipeline = pickle.load(file)

st.title("👨‍🏫🔢 Math Score Predictions")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Display the uploaded DataFrame
    st.write("Preview of uploaded data:")
    st.dataframe(df)
    
    if TARGET in df.columns:
        X_new = df.drop(columns=[TARGET])
    else:
        X_new = df

    # scatter plot of reading score vs writing score
    st.write("Scatter plot of reading score vs writing score:")
    st.scatter_chart(df, x="reading score", y="writing score", color="gender")
    
    if st.button("Predict Scores"):
        y_pred = model_pipeline.predict(X_new)
        
        st.write("Predicted Math Scores:")
        df["math score (pred)"] = y_pred.astype(int)
        st.dataframe(df)

        st.download_button(
        label="Download Predictions as CSV",
        data=df.to_csv(index=False),
        file_name="predicted_math_scores.csv",
        mime="text/csv"
    )