import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Data Visualization App")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📄 Data Preview")
    st.write(df.head())

    # Select column for visualization
    column = st.selectbox("Choose a column to visualize", df.columns)

    # Plot
    st.subheader(f"📈 Histogram of {column}")
    fig, ax = plt.subplots()
    ax.hist(df[column].dropna(), bins=20, color="skyblue", edgecolor="black")
    st.pyplot(fig)
