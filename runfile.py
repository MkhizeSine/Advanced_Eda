import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv
import os

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(page_title="EDA App", layout="wide")

st.title("📊 Exploratory Data Analysis App")
st.write("Upload a dataset and generate automated EDA reports.")

# ----------------------
# FILE UPLOAD
# ----------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# ----------------------
# LOAD DATA
# ----------------------
def load_data(file):
    return pd.read_csv(file, sep=';')

if uploaded_file is not None:
    df = load_data(uploaded_file)

    # ----------------------
    # BASIC EDA
    # ----------------------
    st.subheader("📌 Data Preview")
    st.dataframe(df.head(23))

    st.subheader("ℹ️ Data Info")
    st.write("Shape:", df.shape)
    st.write("Columns:", df.columns.tolist())

    st.subheader("📈 Statistical Summary")
    st.write(df.describe())

    st.subheader("❗ Missing Values")
    st.write(df.isnull().sum())

    # ----------------------
    # REPORT GENERATION
    # ----------------------
    st.subheader("📊 Generate Reports")

    col1, col2 = st.columns(2)

    # YDATA PROFILING
    with col1:
        if st.button("Generate YData Profiling Report"):
            with st.spinner("Generating report..."):
                profile = ProfileReport(df, title="EDA Report", explorative=True)
                profile.to_file("ydata_report.html")

            with open("ydata_report.html", "r", encoding="utf-8") as f:
                html_data = f.read()

            st.success("YData report generated!")
            st.components.v1.html(html_data, height=800, scrolling=True)

    # SWEETVIZ
    with col2:
        if st.button("Generate Sweetviz Report"):
            with st.spinner("Generating report..."):
                report = sv.analyze(df)
                report.show_html("sweetviz_report.html")

            with open("sweetviz_report.html", "r", encoding="utf-8") as f:
                html_data = f.read()

            st.success("Sweetviz report generated!")
            st.components.v1.html(html_data, height=800, scrolling=True)

else:
    st.info("👆 Upload a CSV file to begin analysis.")
